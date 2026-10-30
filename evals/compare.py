#!/usr/bin/env python3
"""Compare recorded baseline and treatment agent runs. No agent execution."""
import argparse
import json
from pathlib import Path

REQUIRED = ("task_id", "variant", "accepted", "elapsed_seconds", "retries",
            "reviewer", "evidence_url", "model", "recorded_at")

def summarize(records):
    if not isinstance(records, list) or not records:
        raise ValueError("Expected a nonempty list of run records")
    groups = {}
    for row in records:
        if not isinstance(row, dict) or any(k not in row for k in REQUIRED):
            raise ValueError("Every run requires: " + ", ".join(REQUIRED))
        if row.get("synthetic") is not False:
            raise ValueError("Empirical reports require synthetic=false")
        if row["variant"] not in ("baseline", "treatment"):
            raise ValueError("variant must be baseline or treatment")
        if type(row["accepted"]) is not bool:
            raise ValueError("accepted must be boolean")
        if not isinstance(row["elapsed_seconds"], (int, float)) or isinstance(row["elapsed_seconds"], bool) or row["elapsed_seconds"] < 0:
            raise ValueError("elapsed_seconds must be nonnegative")
        if type(row["retries"]) is not int or row["retries"] < 0:
            raise ValueError("retries must be nonnegative integer")
        if any(not isinstance(row[k], str) or not row[k].strip() for k in ("task_id", "reviewer", "evidence_url", "model", "recorded_at")):
            raise ValueError("Missing provenance fields")
        key = (row["task_id"], row["variant"])
        if key in groups:
            raise ValueError("Duplicate task/variant pair; use separate experiment files for repeats")
        groups[key] = row
    tasks = sorted({task for task, _ in groups})
    pairs = [(groups[(t, "baseline")], groups[(t, "treatment")]) for t in tasks
             if (t, "baseline") in groups and (t, "treatment") in groups]
    if not pairs:
        raise ValueError("At least one paired baseline/treatment task is required")
    result = {"paired_tasks": len(pairs), "unpaired_tasks": len(tasks) - len(pairs),
              "warning": "Descriptive results only; not causal evidence or statistical significance."}
    for idx, variant in enumerate(("baseline", "treatment")):
        rows = [p[idx] for p in pairs]
        summary = {"accepted": sum(r["accepted"] for r in rows),
                   "acceptance_rate": sum(r["accepted"] for r in rows) / len(rows),
                   "mean_elapsed_seconds": sum(r["elapsed_seconds"] for r in rows) / len(rows),
                   "total_retries": sum(r["retries"] for r in rows)}
        if all(type(r.get("cost_usd")) in (int, float) and r["cost_usd"] >= 0 for r in rows):
            summary["total_cost_usd"] = round(sum(r["cost_usd"] for r in rows), 6)
        else:
            summary["total_cost_usd"] = None
        result[variant] = summary
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("records", help="JSON list of real agent run records")
    args = parser.parse_args()
    try:
        print(json.dumps(summarize(json.loads(Path(args.records).read_text(encoding="utf-8"))), indent=2))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

if __name__ == "__main__":
    main()
