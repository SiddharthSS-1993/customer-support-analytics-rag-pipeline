# Customer Support Intelligence Platform

## Current Status

### Completed

- Repository foundation
- Product Requirements Document
- High-Level Design
- ADR-001: Layered Data Platform Architecture
- ADR-002: Synthetic Data Generation
- Enterprise synthetic data generation framework
- Configurable Bronze ingestion framework

## Current Data Sources

| Dataset | Status |
|----------|--------|
| customers.csv | ✅ |
| products.csv | ✅ |
| agents.csv | ✅ |
| sla_policies.csv | ✅ |
| support_tickets.csv | ✅ |


### Current Bronze Capabilities

- Configuration-driven ingestion
- Multi-dataset processing
- Centralized logging
- Reusable file utilities
- Pipeline orchestration


### In Progress

- Bronze data validation for quality framework


### Upcoming

- Silver transformation layer
- Gold analytics layer
- DuckDB analytics
- PySpark migration
- Databricks deployment
- RAG assistant


## Architecture

Raw Data Sources
        ↓
Bronze Layer
        ↓
Silver Layer
        ↓
Gold Layer
        ↓
Analytics / AI