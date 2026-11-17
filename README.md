# BigQuery Partition and Cluster Cost Lab

Compares estimated scanned rows for full scans versus partition-filtered analytical queries.  
Includes BigQuery DDL and query examples illustrating date partitioning and customer clustering.

## Problem

Analytics queries may scan unnecessary historical partitions when filters are missing.

## Solution and design

Demonstrate a partition-aware design and calculate a reproducible local approximation of records scanned.

**Stack:** BigQuery SQL, partitioning, clustering, cost awareness

## Quick start

Requires Python 3.11+ (standard library only for the local demo).

```bash
python main.py
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the same tests on pushes and pull requests.

## Project layout

- `main.py`: core processing and a small command-line demonstration
- `data/`, `seeds/`, `models/`, `sql/`, `infra/`, `dags/` or `powerbi/`: included only where relevant
- `tests/`: fixture-based expected-value and repeatability checks

## Engineering decisions

- Narrow scope, realistic field names, and synthetic reproducible inputs
- No credentials, customer records, patient data, API tokens, or paid cloud resources
- Visible business logic and deterministic fixtures rather than screenshots of unverifiable dashboards

## Limits and next iteration

Scanned-row counts are a teaching proxy, not BigQuery bytes billed. Use EXPLAIN and INFORMATION_SCHEMA for real workload measurements.

A production hardening path would add larger-scale fixtures, alerting, operational runbooks, robust error handling, and integration tests against the real deployment target.

## Portfolio integrity

This is an independently reproducible **portfolio demonstration**, not a claim that these files are employer code or that a cloud workload has been deployed. The fixture data is synthetic.
