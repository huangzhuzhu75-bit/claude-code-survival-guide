import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_env import environment_summary, VARIABLES


class CheckEnvTests(unittest.TestCase):
    def test_no_secret_values_in_report(self):
        secrets = {"ANTHROPIC_API_KEY": "a-secret-never-print-me", "HTTPS_PROXY": "http://secret.example.com:1234"}
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, secrets):
            report = environment_summary(Path(folder))
            self.assertTrue(report["variables_present"]["ANTHROPIC_API_KEY"])
            self.assertTrue(report["variables_present"]["HTTPS_PROXY"])
            self.assertNotIn("a-secret-never-print-me", str(report))
            self.assertNotIn("secret.example.com", str(report))

    def test_missing_paths(self):
        with tempfile.TemporaryDirectory() as folder:
            report = environment_summary(Path(folder))
            self.assertFalse(report["claude_paths_present"][".claude"])
            self.assertFalse(report["claude_paths_present"][".claude.json"])


if __name__ == "__main__":
    unittest.main()
