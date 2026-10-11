import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validator"))
from mrz_gate import check


def load_specimen(name):
    with (ROOT / "synthetic" / name).open(encoding="utf-8") as handle:
        return [line.rstrip("\n") for line in handle.readlines()[:2]]


class TestGate(unittest.TestCase):
    def test_valid_specimen_passes(self):
        ok, reasons = check(load_specimen("specimen_valid.txt"))
        self.assertTrue(ok, reasons)

    def test_degraded_specimen_fails(self):
        ok, reasons = check(load_specimen("specimen_degraded.txt"))
        self.assertFalse(ok)
        self.assertIn("date_of_birth:check_digit", reasons)
        self.assertIn("composite:check_digit", reasons)

    def test_wrong_shape_fails(self):
        self.assertFalse(check(["SHORT", "SHORT"])[0])

    def test_captured_run_matches_gate(self):
        with (ROOT / "runs" / "t2_degraded.json").open(encoding="utf-8") as handle:
            run = json.load(handle)
        self.assertFalse(run["gate"][0])
        self.assertEqual(run["uncertain_fields"], [])

    @unittest.skipUnless(shutil.which("swipl"), "SWI-Prolog is optional locally")
    def test_policy_refuses_ai_override(self):
        query = "consult('policy/evidence_gate.pl'), ai_authorised_to_override(false), halt."
        completed = subprocess.run(
            ["swipl", "-q", "-g", query], cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
