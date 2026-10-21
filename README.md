# Data Annotation Quality Checker

A small Python project that checks the quality of a labeled text dataset.

## What it does
- Loads a CSV file containing text and labels.
- Checks for missing text or labels.
- Flags labels outside the approved label set.
- Finds duplicate text rows.
- Produces a short quality report.

This is a personal learning/sample project using fictional example data. It does not contain client or employer information.

## Requirements
- Python 3.9+
- No third-party packages required

## Run it
```bash
python quality_checker.py
```

By default, the script checks `sample_data.csv` and prints a report.

## Example labels
For this sample, the allowed sentiment labels are `positive`, `negative`, and `neutral`.

## Project structure
```text
rex-code-repository-sample/
├── README.md
├── quality_checker.py
├── sample_data.csv
└── test_quality_checker.py
```

## Limitations
This is a basic demonstration, not a production annotation platform. The rules and allowed labels should be adapted to the dataset's annotation guidelines.
