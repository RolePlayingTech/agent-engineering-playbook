#!/usr/bin/env python3
"""Offline, dependency-free evaluator for manually captured agent traces."""
import argparse
import json
from pathlib import Path

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def evaluate(case, trace):
    checks = []
    for rule in case["checks"]:
        event_type = rule["event_type"]
        matches = [e for e in trace.get("events", []) if e.get("type") == event_type]
        if "contains" in rule:
            matches = [e for e in matches if rule["contains"] in str(e.get("text", ""))]
        found = bool(matches)
        passed_check = found if rule["kind"] == "required" else not found
        checks.append({"id": rule["id"], "passed": passed_check})
    return {"case_id": case["id"], "trace_id": trace.get("id", "unknown"),
            "passed": all(c["passed"] for c in checks), "checks": checks,
            "note": "Checks assess recorded evidence only; they cannot establish full task correctness."}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("case")
    parser.add_argument("trace")
    parser.add_argument("--output", help="Optional JSON result path")
    args = parser.parse_args()
    result = evaluate(load(args.case), load(args.trace))
    rendered = json.dumps(result, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    raise SystemExit(0 if result["passed"] else 1)

if __name__ == "__main__":
    main()
