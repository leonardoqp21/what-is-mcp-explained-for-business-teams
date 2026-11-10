import json
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import mcp_toy
import should_i_use_mcp as sm

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


class Toy(unittest.TestCase):
    def setUp(self):
        mcp_toy.CRM["contacts"]["C-7"]["email"] = "old@example.com"
        self.s = mcp_toy.ToyServer()

    def call(self, name, args, approved=False):
        return self.s.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                              "params": {"name": name, "arguments": args}}, approved=approved)

    def test_list_marks_writes(self):
        r = self.s.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
        tools = {t["name"]: t["writes"] for t in r["result"]["tools"]}
        self.assertEqual(tools, {"find_account": False, "update_contact_email": True})

    def test_read_needs_no_approval(self):
        r = self.call("find_account", {"name": "acme"})
        self.assertEqual(r["result"]["content"]["id"], "A-100")

    def test_write_refused_without_approval(self):
        r = self.call("update_contact_email", {"id": "C-7", "email": "x@example.com"})
        self.assertTrue(r["result"]["isError"])
        self.assertEqual(mcp_toy.CRM["contacts"]["C-7"]["email"], "old@example.com")

    def test_write_with_approval(self):
        r = self.call("update_contact_email", {"id": "C-7", "email": "x@example.com"}, approved=True)
        self.assertEqual(r["result"]["content"], "updated C-7")
        self.assertEqual(mcp_toy.CRM["contacts"]["C-7"]["email"], "x@example.com")

    def test_unknown_method_and_tool(self):
        self.assertEqual(self.s.handle({"id": 9, "method": "nope"})["error"]["code"], -32601)
        self.assertEqual(self.call("nope", {})["error"]["code"], -32602)

    def test_responses_are_json(self):
        json.dumps(self.s.handle({"id": 1, "method": "tools/list"}))


class Chooser(unittest.TestCase):
    def names(self, job):
        return [n for n, _ in sm.suggest(job)]

    def test_sync(self):
        self.assertIn("two-way sync", self.names("keep Salesforce and NetSuite customers identical all day"))

    def test_question(self):
        self.assertIn("MCP", self.names("ask which deals are stuck and draft nudges"))

    def test_workflow(self):
        self.assertIn("workflow", self.names("notify sales whenever a deal closes"))

    def test_fallback(self):
        self.assertEqual(self.names("xyzzy"), ["MCP"])


class Hygiene(unittest.TestCase):
    def test_no_em_dash_and_no_one_way(self):
        for base, _, files in os.walk(ROOT):
            if "__pycache__" in base:
                continue
            for f in files:
                if f == "REPO-NOTES.md" or not f.endswith((".md", ".py", ".txt", ".sh", ".mmd")):
                    continue
                with open(os.path.join(base, f), encoding="utf-8") as fh:
                    body = fh.read()
                self.assertNotIn(chr(0x2014), body, f)
                if f != "test_code.py":
                    self.assertNotIn("one-way sync", body.lower(), f)

    def test_docs_exist_for_readme_links(self):
        import re
        with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
            links = re.findall(r"\]\(((?:docs|diagrams|prompts|code)/[^)#]*)\)", fh.read())
        self.assertTrue(links)
        for l in links:
            self.assertTrue(os.path.exists(os.path.join(ROOT, l.rstrip("/"))), l)


if __name__ == "__main__":
    unittest.main()
