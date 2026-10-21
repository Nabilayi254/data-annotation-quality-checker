"""Validate a simple CSV dataset used for text-labeling practice."""

import csv
from collections import Counter
from pathlib import Path

ALLOWED_LABELS = {"positive", "negative", "neutral"}


def check_dataset(csv_path):
    """Return a quality report for rows with 'text' and 'label' columns."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    issues = []
    seen_text = set()
    total = 0
    label_counts = Counter()

    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"text", "label"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV must contain 'text' and 'label' columns.")

        for line_number, row in enumerate(reader, start=2):
            total += 1
            text = (row.get("text") or "").strip()
            label = (row.get("label") or "").strip().lower()

            if not text:
                issues.append(f"Row {line_number}: missing text.")
            if not label:
                issues.append(f"Row {line_number}: missing label.")
            elif label not in ALLOWED_LABELS:
                issues.append(
                    f"Row {line_number}: unsupported label '{label}'."
                )
            else:
                label_counts[label] += 1

            normalized_text = text.casefold()
            if normalized_text and normalized_text in seen_text:
                issues.append(f"Row {line_number}: duplicate text.")
            elif normalized_text:
                seen_text.add(normalized_text)

    return {
        "rows_checked": total,
        "label_counts": dict(sorted(label_counts.items())),
        "issues": issues,
        "passed": len(issues) == 0,
    }


def main():
    report = check_dataset("sample_data.csv")
    print("DATA ANNOTATION QUALITY REPORT")
    print(f"Rows checked: {report['rows_checked']}")
    print(f"Valid label counts: {report['label_counts']}")
    print(f"Result: {'PASS' if report['passed'] else 'REVIEW NEEDED'}")
    print("Issues:")
    if report["issues"]:
        for issue in report["issues"]:
            print(f"- {issue}")
    else:
        print("- No issues found.")


if __name__ == "__main__":
    main()
