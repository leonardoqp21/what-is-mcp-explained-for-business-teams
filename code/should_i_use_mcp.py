"""Suggest MCP, a workflow, a two-way sync, an agent or an API script for a job.

Keyword heuristics for a first answer, not a decision.
Usage: python should_i_use_mcp.py "keep Salesforce and NetSuite customers identical"
"""
import re
import sys

RULES = [
    ("two-way sync", r"\b(keep|stay|always|continuous\w*|real[- ]?time|identical|consistent|match(ing)?|in sync|mirror)\b.*\b(systems?|crm|erp|salesforce|hubspot|netsuite|database|customers?|records?)\b|\bsync\b",
     "Systems must agree continuously: a two-way sync. MCP can help you set it up and fix it."),
    ("workflow", r"\b(whenever|every time|on a schedule|each (day|week|night)|trigger|alert|notify|when a)\b",
     "A repeatable step on a trigger: a workflow."),
    ("agent with approvals", r"\b(reconcile|multi[- ]step|onboard\w*|escalat\w*|approve before|then (create|update|post))\b",
     "Multi-step work with writes: an agent with approval steps and a log."),
    ("API script", r"\b(exact|bulk|nightly export|batch|millions?|performance|from code|cron)\b",
     "A precise, repeatable call from code: an API script."),
    ("MCP", r"\b(ask|which|show|list|find|why|explain|draft|summari[sz]e|investigate|compare|what)\b",
     "A question, an investigation or a draft for review: MCP with an assistant."),
]


def suggest(job):
    text = job.lower()
    hits = [(name, why) for name, pat, why in RULES if re.search(pat, text)]
    return hits or [("MCP", "No strong signal. Start with read-only questions through MCP.")]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    for name, why in suggest(" ".join(argv[1:])):
        print("- %s: %s" % (name, why))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
