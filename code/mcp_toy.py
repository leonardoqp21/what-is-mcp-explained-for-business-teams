"""A teaching model of the messages behind an MCP request, with a fake CRM.

Not an MCP SDK and not a real server. It shows the shape of tools/list and
tools/call (JSON-RPC 2.0) and where an approval gate sits.
"""
import json

CRM = {
    "accounts": {"A-100": {"id": "A-100", "name": "Acme", "open_deals": 2}},
    "contacts": {"C-7": {"id": "C-7", "email": "old@example.com"}},
}

TOOLS = [
    {"name": "find_account", "description": "Find an account by name", "writes": False},
    {"name": "update_contact_email", "description": "Change a contact's email", "writes": True},
]


class ToyServer:
    def handle(self, request, approved=False):
        """Handle one JSON-RPC style request (a dict). Return a response dict."""
        rid = request.get("id")
        method = request.get("method")
        params = request.get("params", {})
        if method == "tools/list":
            return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}}
        if method == "tools/call":
            return self._call(rid, params, approved)
        return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "method not found"}}

    def _call(self, rid, params, approved):
        name = params.get("name")
        args = params.get("arguments", {})
        tool = next((t for t in TOOLS if t["name"] == name), None)
        if tool is None:
            return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32602, "message": "unknown tool"}}
        if tool["writes"] and not approved:
            return {"jsonrpc": "2.0", "id": rid, "result": {"isError": True,
                    "content": "refused: this tool changes data and no approval was given"}}
        if name == "find_account":
            for acct in CRM["accounts"].values():
                if acct["name"].lower() == str(args.get("name", "")).lower():
                    return {"jsonrpc": "2.0", "id": rid, "result": {"content": acct}}
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": None}}
        if name == "update_contact_email":
            contact = CRM["contacts"].get(args.get("id"))
            if not contact:
                return {"jsonrpc": "2.0", "id": rid, "result": {"isError": True, "content": "no such contact"}}
            contact["email"] = args["email"]
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": "updated " + contact["id"]}}


def demo():
    s = ToyServer()
    steps = [
        ({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}, False),
        ({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
          "params": {"name": "find_account", "arguments": {"name": "Acme"}}}, False),
        ({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
          "params": {"name": "update_contact_email", "arguments": {"id": "C-7", "email": "new@example.com"}}}, False),
        ({"jsonrpc": "2.0", "id": 4, "method": "tools/call",
          "params": {"name": "update_contact_email", "arguments": {"id": "C-7", "email": "new@example.com"}}}, True),
    ]
    for req, approved in steps:
        print("->", json.dumps(req), "(approved)" if approved else "")
        print("<-", json.dumps(s.handle(req, approved=approved)))


if __name__ == "__main__":
    demo()
