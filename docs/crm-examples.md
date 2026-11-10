# MCP with a CRM: Salesforce and HubSpot style examples

All examples assume a connected account with the right to read the objects involved. What an assistant can do depends on the actions the server offers and on your role. Stacksync's own guides list per-app limits: [Salesforce](https://www.stacksync.com/mcp/salesforce).

## 1. Find stuck deals (read)

```text
List open opportunities over 50,000 with no activity in 14 days. Group by owner. Return a table with owner, account, amount and last activity date. Do not change or send anything.
```
Why it works: one read, a clear filter, a defined output.

## 2. Prepare a call (read)

```text
For the account <ACCOUNT>, list the open opportunities, the last five activities and the primary contacts. Say what you could not see.
```

## 3. Clean up duplicates (read, then a reviewed write)

```text
Find contacts with the same email in two records. Show me the pairs and which fields differ. Do not merge. Propose which record to keep and why.
```
Merging is a write that is hard to undo. Review every pair.

## 4. Design an alert (no data touched)

```text
Inspect my CRM and Slack connections and propose a workflow that posts a closed-won deal to a channel I choose. Show the message with placeholders. Do not activate it.
```

## 5. Investigate a failed sync

```text
Find my Salesforce syncs and read their current issues. Group failures by cause and show affected record ids. Propose the smallest fix. Do not retry or revert yet.
```

## Limits to expect

- A read-only account cannot write, whatever the assistant is asked.
- Some objects cannot be read or written through a given connector. Check the connector's published support list.
- Custom objects and fields need checking against the live schema.
- Per-field sync direction and association settings may need the product's web app rather than the assistant.
- An assistant answering from a query is not a report you can audit. For numbers that matter, keep a governed report.
