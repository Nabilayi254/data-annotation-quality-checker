"""Basic unit tests for the data annotation quality checker."""

import tempfile
import unittest
from pathlib import Path

from quality_checker import check_dataset


class QualityCheckerTests(unittest.TestCase):
    def test_valid_dataset_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.csv"
            path.write_text(
                "text,label\nGreat service,positive\nJust okay,neutral\n",
                encoding="utf-8",
            )
            report = check_dataset(path)
            self.assertTrue(report["passed"])
            self.assertEqual(report["rows_checked"], 2)

    def test_invalid_label_is_flagged(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.csv"
            path.write_text(
                "text,label\nVery good,excellent\n",
                encoding="utf-8",
            )
            report = check_dataset(path)
            self.assertFalse(report["passed"])
            self.assertTrue(any("unsupported label" in issue for issue in report["issues"]))

    def test_duplicate_text_is_flagged(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicates.csv"
            path.write_text(
                "text,label\nSame text,positive\nsame text,neutral\n",
                encoding="utf-8",
            )
            report = check_dataset(path)
            self.assertTrue(any("duplicate text" in issue for issue in report["issues"]))


if __name__ == "__main__":
    unittest.main()
