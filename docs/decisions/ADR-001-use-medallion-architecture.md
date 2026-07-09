# ADR-001: Use Medallion Architecture

## Status

Accepted

## Context

The platform needs to process customer support data from multiple sources and support analytics, auditability, reprocessing, and future AI use cases.

A single flat processed dataset would make it harder to distinguish raw data, cleaned data, and business-ready metrics.

## Decision

Use a Medallion Architecture with three layers:

- Bronze: raw ingested data
- Silver: cleaned and enriched data
- Gold: business-ready analytical datasets

## Alternatives Considered

### Single processed dataset

Simpler initially, but weak for auditability, reprocessing, and debugging.

### Traditional data warehouse only

Useful for analytics, but less flexible for raw data retention, semi-structured data, and future AI workflows.

## Consequences

### Benefits

- Clear separation between raw, cleaned, and business-ready data
- Easier debugging and reprocessing
- Better support for data quality checks
- Natural path toward lakehouse and Databricks implementation

### Trade-offs

- More layers to maintain
- More documentation required
- Slightly more initial setup