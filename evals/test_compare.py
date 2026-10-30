import unittest
from compare import summarize

def record(task, variant, accepted=True, **kwargs):
    return dict(task_id=task, variant=variant, accepted=accepted, elapsed_seconds=10,
                retries=0, reviewer="reviewer", evidence_url="https://example.org/log",
                model="test-model", recorded_at="2026-10-30", synthetic=False, **kwargs)

class ComparisonTests(unittest.TestCase):
    def test_paired_summary(self):
        report = summarize([record("a", "baseline", False), record("a", "treatment")])
        self.assertEqual(report["paired_tasks"], 1)
        self.assertEqual(report["baseline"]["accepted"], 0)
        self.assertEqual(report["treatment"]["accepted"], 1)
        self.assertIsNone(report["treatment"]["total_cost_usd"])

    def test_reject_synthetic(self):
        r = record("a", "baseline")
        r["synthetic"] = True
        with self.assertRaises(ValueError):
            summarize([r, record("a", "treatment")])

    def test_reject_unpaired(self):
        with self.assertRaises(ValueError):
            summarize([record("a", "baseline")])

    def test_reject_duplicates(self):
        with self.assertRaises(ValueError):
            summarize([record("a", "baseline"), record("a", "baseline"), record("a", "treatment")])

    def test_reject_missing_evidence(self):
        r = record("a", "baseline")
        r["evidence_url"] = ""
        with self.assertRaises(ValueError):
            summarize([r, record("a", "treatment")])

if __name__ == "__main__":
    unittest.main()
