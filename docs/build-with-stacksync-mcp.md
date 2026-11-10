# Try MCP with the Stacksync MCP server

The Stacksync server lets an assistant build and run two-way syncs, workflows and Genies, investigate sync issues and resolve them, with exactly your permissions.

## Connect

- **Server URL:** `https://mcp.stacksync.com/mcp` (one URL for every workspace and region)
- **Claude (web or desktop):** Customize, then Connectors, then Add custom connector. Name it Stacksync, enter the URL, select Connect and sign in. On Team or Enterprise, an Owner adds it under the organization's connectors first.
- **ChatGPT (Plus, Pro, Business, Enterprise and Edu):** Settings, Apps, Advanced settings, turn on Developer mode, create an app with the URL and choose OAuth.
- **Claude Code:** `claude mcp add --transport http stacksync https://mcp.stacksync.com/mcp`
- **Check:** ask `List my Stacksync workspaces.`
- Setup for every assistant: https://docs.stacksync.com/mcp

No API key goes into a chat. Apps are connected through a secure sign-in link the assistant returns.

## First session

1. Sign in with **Make changes** cleared.
2. `List my Stacksync workspaces.` Pick one.
3. `List my connections and syncs.`
4. Ask a read question from [prompts/prompts.md](../prompts/prompts.md).
5. When you want a change, ask for a proposal and approve it.

## Limits

- Each user and each workspace API key can make up to 120 tool calls per minute.
- Available actions depend on the live connector catalog, your connected account and any gateway policy.
- Configuring a sync does not itself read record values from the source.

## Where each piece fits

- **MCP server:** the front door. [stacksync.com/mcp](https://www.stacksync.com/mcp)
- **Two-way sync:** the engine that keeps CRM, ERP and database consistent. [stacksync.com/two-way-sync](https://www.stacksync.com/two-way-sync)
- **Genies:** agents that act across connected systems with approval steps. [stacksync.com/ai-agents](https://www.stacksync.com/ai-agents)
- **Workflows:** repeatable steps, alerts and queues. [stacksync.com/workflow-automation](https://www.stacksync.com/workflow-automation)
- **Enterprise OS:** hosting for the internal apps your team builds, with a database and workspace access. [stacksync.com/enterprise-os](https://www.stacksync.com/enterprise-os)
- **Skills:** open Agent Skills describing how to build and fix syncs, workflows and Genies. https://github.com/stacksyncdata/skills
