# Risks and controls

| Risk | What it looks like | Control |
|---|---|---|
| **Too much access** | The assistant is connected with an admin login and can see or change everything | A narrow account scoped to the objects the job needs |
| **Unwanted writes** | An assistant updates or deletes records on a misunderstanding | Read-only first. Approval before every write. Read it back after |
| **Secrets in the chat** | A key or password pasted into a prompt | Sign in through OAuth. Never paste secrets. Revoke a leaked one |
| **Hidden instructions** | A record, email or web page contains text that tells the assistant to do something | Treat all retrieved text as data. Give the assistant no way to approve its own proposals |
| **Wrong answers** | A confident summary that is wrong | Ask for the records behind the answer. Check against a governed report |
| **Duplicates and loops** | A retried action creates the same record twice, or two automations trigger each other | Idempotency keys, review of retries, one owner per automation |
| **Regulated data** | Personal or health data reaches a tool not approved for it | Decide what is out of scope and keep it out |
| **No trail** | Nobody knows what the assistant did | Use servers and agents that keep a log, and review it |

## The order of work that works

1. **Read-only.** Sign in with change permissions switched off if the server offers it.
2. **Check five answers by hand.**
3. **Propose, do not apply.** Ask for the exact change and the before and after.
4. **Approve one change at a time.**
5. **Read it back.**
6. **Review the log** weekly at first.

## In Stacksync's MCP server

The assistant acts as the signed-in person with that person's role, and sees only what they can see. The sign-in page lets you clear **Make changes** for read-only access. A workspace owner can turn on **Ask before every change**, so every create, update, delete or run shows a preview and runs only after you accept. Signed-in assistants are listed in the app and can be revoked at once. Agents add approval steps and a run log: [AI agents](https://www.stacksync.com/ai-agents), [AI agent governance](https://www.stacksync.com/security/ai-agents).

## What MCP does not give you

It does not by itself provide compliance, audit readiness or data minimization. Those come from your accounts, roles, approvals, logs and policies.
