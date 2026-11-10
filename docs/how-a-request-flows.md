# How one request flows through MCP

The request: "Which open deals over 50k have no next step? Draft a nudge for each owner. Do not send anything."

```mermaid
sequenceDiagram
    participant U as You
    participant A as AI assistant (client)
    participant S as MCP server
    participant C as CRM
    U->>A: Ask in plain language
    A->>S: tools/list (what can you do?)
    S-->>A: find_deals (read), update_deal (write)
    A->>S: tools/call find_deals {min_amount: 50000, no_next_step: true}
    S->>C: API call as you, with your permissions
    C-->>S: 7 deals
    S-->>A: result
    A-->>U: Table of 7 deals and 3 draft nudges
    Note over U,A: Nothing was changed or sent
```

## What each step protects

| Step | Control to look for |
|---|---|
| Sign-in | OAuth in the browser. No password or key in the chat |
| `tools/list` | You can see which tools exist. Turn write tools off |
| `tools/call` | Inputs are visible. A good client shows them before a write |
| The system call | The CRM enforces your role. The server cannot see more than you can |
| The answer | Ask the assistant to say what it could not see |

## A write, for comparison

```mermaid
sequenceDiagram
    participant U as You
    participant A as AI assistant
    participant S as MCP server
    A->>U: Proposal: set next step on deal D-4 to "Call Tuesday"
    U->>A: Approve
    A->>S: tools/call update_deal {id: D-4, next_step: "Call Tuesday"}
    S-->>A: updated
    A-->>U: Done. Read it back to confirm.
```

Two habits: **propose, then approve, then read back.**

## The wire format, briefly

MCP messages are JSON-RPC 2.0. Two you will see: `tools/list` and `tools/call`. `python code/mcp_toy.py` prints both against a fake CRM.
