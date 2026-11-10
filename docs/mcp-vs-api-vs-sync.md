# MCP, API, workflow automation and two-way sync: what each is for

| | What it is | Who or what drives it | Good for | Not for |
|---|---|---|---|---|
| **API** | How software talks to one system | Code | Precise, repeatable calls | Letting a person ask in plain language |
| **MCP** | A shared way for an AI assistant to discover and use tools | A person talking to an assistant | Questions, investigations, drafting changes, building integrations from a chat | Keeping two systems matching 24/7 |
| **Workflow automation** | A defined sequence of steps on a trigger | An event or schedule | Repeatable processes, alerts, approvals | Open-ended questions |
| **Two-way sync** | Continuous record-level consistency between systems | The sync engine | Making a CRM, an ERP and a database agree | One-off questions |
| **AI agent (Genie)** | An agent with a job description that acts across connected systems | A trigger or a request | Multi-step work with approvals and logs | Replacing your controls |

## How they fit together

- MCP is often the **front door**: you ask an assistant to build or fix the sync, the workflow or the agent.
- The **sync** keeps the data consistent. The assistant then queries a current copy in one database instead of calling each app on every question.
- The **workflow** or **agent** runs the repeatable parts with approvals and logs.
- The **API** is underneath all of it.

## Rule of thumb

- "Tell me / show me / draft": MCP.
- "Always do X when Y": a workflow.
- "These two systems must agree": a [two-way sync](https://www.stacksync.com/two-way-sync).
- "Handle this multi-step job and ask me before writes": an [agent](https://www.stacksync.com/ai-agents).
- "Run this exact call from code": an API.

Use `python code/should_i_use_mcp.py "<your job>"` for a first answer.
