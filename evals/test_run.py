"""Standard-library smoke tests for the evaluation runner."""
import unittest
from run import evaluate

CASE = {"id": "demo", "checks": [
    {"id": "required", "kind": "required", "event_type": "final", "contains": "not run"},
    {"id": "forbidden", "kind": "forbidden", "event_type": "final", "contains": "all tests passed"}
]}

class EvaluatorTests(unittest.TestCase):
    def test_expected_trace_passes(self):
        self.assertTrue(evaluate(CASE, {"events": [{"type": "final", "text": "tests not run"}]})["passed"])

    def test_false_success_fails(self):
        self.assertFalse(evaluate(CASE, {"events": [{"type": "final", "text": "all tests passed"}]})["passed"])

    def test_missing_event_fails(self):
        self.assertFalse(evaluate(CASE, {"events": []})["passed"])

if __name__ == "__main__":
    unittest.main()
