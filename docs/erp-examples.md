# MCP with an ERP: NetSuite style examples

ERPs are where mistakes cost money, so the rule is stricter: **read first, propose writes, approve each one.** Stacksync's NetSuite guide lists per-object limits: [NetSuite](https://www.stacksync.com/mcp/netsuite).

## 1. Received but not billed (read)

```text
List purchase orders that have item receipts but no vendor bill. Total the unbilled amount by vendor and sort by amount. Do not change anything.
```

## 2. Explain a transaction (read)

```text
For sales order <NUMBER>, show the header, the line items and the related invoices and payments. Say if a related record is missing.
```
In NetSuite, transaction lines are nested inside the parent transaction. They are not separate records you can write on their own.

## 3. Prepare a customer update (reviewed write)

```text
Find the customer with internal id <ID>. Propose the exact field changes needed to set the billing email to <EMAIL>. Show the before and after. Do not apply until I approve.
```

## 4. Plan a reporting copy (design only)

```text
Inspect my NetSuite and PostgreSQL connections and propose a read-only copy of sales orders for reporting. Keep the parent transaction id and the nested line items. Do not create it yet.
```

## 5. Check an invoice agent's work

An invoice reconciliation agent reads vendor invoices and purchase orders, proposes matches and waits for a person before anything posts. MCP is how you build and inspect it. See [AI agents](https://www.stacksync.com/ai-agents) for approval steps and run logs.

## Limits to expect

- A readable record type is not automatically writable. Some are read-only (saved searches) and some writes are on request.
- Concurrency limits in the ERP apply to every integration together.
- Do not let an assistant guess a purchase order, change bank details or create vendors.
- Use a role limited to the objects the job needs.
