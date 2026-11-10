# Ten prompts for business users

Connect an assistant to one system first, read-only. Every prompt says what not to do. Replace the `<ANGLE BRACKETS>`. Check them with `python code/should_i_use_mcp.py` or read them as a model for your own.

## Orientation

### 1. What can you do here
```text
List the tools you have from this connection. For each one, say whether it only reads or can change data. Do not call any of them.
```

### 2. What can you not see
```text
For the account I am signed in with, tell me which objects and fields you can read, and which you cannot. Do not change anything.
```

## CRM

### 3. Stuck deals
```text
List open deals over <AMOUNT> with no activity in <N> days. Group by owner and return a table with owner, account, amount and last activity. Do not change or send anything.
```

### 4. Duplicate contacts
```text
Find contacts that share an email. Show the pairs and the fields that differ. Do not merge. Propose which to keep and why.
```

### 5. Call prep
```text
For <ACCOUNT>, list open deals, the last five activities and the main contacts. Say what you could not see.
```

## ERP

### 6. Received but not billed
```text
List purchase orders with receipts and no vendor bill. Total by vendor, sorted by amount. Do not change anything.
```

### 7. A proposed change
```text
Propose the exact field changes to set <FIELD> to <VALUE> on <RECORD>. Show before and after. Do not apply until I approve.
```

## Sync and workflows

### 8. Why did it fail
```text
Find the sync or workflow called <NAME>, read its current issues and group them by cause. Show affected records. Propose the smallest fix. Do not retry, revert or ignore anything yet.
```

### 9. Design, do not build
```text
Inspect my <CRM> and <ERP> connections and propose a two-way sync for <OBJECT>. List field mappings, which side owns each field and what would happen on a conflict. Do not create it.
```

### 10. Check your own answer
```text
For the answer above, list the records you read, the filters you used and anything you assumed. I want to verify it by hand.
```
