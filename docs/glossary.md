# Glossary

- **MCP (Model Context Protocol):** an open standard for connecting AI applications to external systems.
- **MCP server:** a service in front of a system that tells an assistant what it may do and read, and runs those requests.
- **MCP client:** the part of an assistant that talks to servers.
- **Host:** the app you use, such as Claude or an editor, which contains the client.
- **Tool:** an action a server offers, such as "find an account". Read tools look up; write tools change data.
- **Resource:** something an assistant can read, such as a file or a record.
- **Prompt (MCP):** a ready-made instruction a person can choose.
- **JSON-RPC:** the message format MCP uses. `tools/list` and `tools/call` are two messages.
- **OAuth:** sign-in through your browser, so the assistant never holds your password.
- **Remote server:** one you reach by URL. A local server runs on your own machine.
- **System of record:** where the official version of a record lives, for example the CRM.
- **Two-way sync:** continuous consistency of records between systems, within the field mappings and write permissions you set.
- **Workflow:** a defined sequence of steps on a trigger.
- **AI agent (Genie):** an agent with a job description that acts across connected systems, with approval steps and a log.
- **Approval step:** a pause with the full payload until a person approves, rejects or edits.
- **Read-only:** the account or tool can look but not change.
- **Idempotency key:** a label that stops the same action from being applied twice.
