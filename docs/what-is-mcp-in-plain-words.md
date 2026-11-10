# What is MCP, in plain words

## The problem it solves

An AI assistant is good with words and has no view into your business. Your CRM, ERP and databases each have their own way of being asked things. Connecting every assistant to every system with custom work does not scale: three assistants and ten systems is thirty connections.

MCP, the Model Context Protocol, is an **open standard** for that connection. Its own documentation compares it to a USB-C port: one standard plug instead of a drawer of cables. A system gets one MCP server, and any assistant that speaks MCP can use it.

## The three parts

| Part | Plain meaning | Example |
|---|---|---|
| **Client** (inside a host app) | The assistant you talk to | Claude, ChatGPT, Cursor |
| **Server** | A small service in front of one system or platform | A CRM server, a database server, the Stacksync server |
| **The system** | Where your data actually lives | Salesforce, NetSuite, PostgreSQL |

When someone says "we added an MCP", they mean they added an MCP **server** to the assistant.

## The three kinds of capability a server offers

| Kind | Plain meaning | Example |
|---|---|---|
| **Tools** | Things the assistant can **do** | Find an account. Update a contact. Run a sync |
| **Resources** | Things the assistant can **read** | A file, a record, a schema |
| **Prompts** | **Ready-made instructions** a person can pick | "Summarize this account" |

Tools are where the risk and most of the value sit. A read tool looks things up. A write tool changes your data.

## What happens when you ask a question

1. You ask in plain language.
2. The assistant asks the server what tools it has.
3. The assistant picks one and fills in its inputs.
4. The server runs it against the system, with your permissions.
5. The result goes back to the assistant, which explains it to you.

The assistant does not hold your password. In a well-set-up server you sign in once through your browser (OAuth), and the server acts as you. See [how-a-request-flows.md](how-a-request-flows.md).

## What MCP is not

- **Not an AI model.** It is the connection, not the brain.
- **Not a database or a copy of your data.** Each answer comes from a live call.
- **Not a sync.** It does not keep two systems matching. See [mcp-vs-api-vs-sync.md](mcp-vs-api-vs-sync.md).
- **Not a security product.** It carries whatever permissions the connected account has.
- **Not the Microsoft Certified Professional exam.**

## Where it comes from

MCP is open source. Anthropic introduced it in November 2024, and assistants and developer tools from many vendors now support it. The reference documentation is at https://modelcontextprotocol.io.
