# ADR-002: Use Synthetic Data Generation

## Status

Accepted

## Context

The Customer Support Intelligence Platform requires realistic datasets for development, testing, and demonstration.

Using production customer data is not appropriate because of privacy, security, and regulatory concerns.

Public datasets often do not match the domain model or business requirements of the platform. They also provide limited control over data quality scenarios, relationships between entities, and dataset size.

The platform must also support testing at multiple scales without increasing the size of the Git repository.

## Decision

The platform will generate synthetic enterprise datasets using a configurable data generation framework.

The framework will produce realistic datasets for:

- Customers
- Products
- Support Agents
- SLA Policies
- Support Tickets

Small sample datasets may be committed to the repository for demonstration purposes.

Large generated datasets will remain outside source control and can be recreated at any time.

## Alternatives Considered

### Use public datasets

Advantages

- No development effort.
- Real-world data characteristics.

Disadvantages

- Limited control over schema and relationships.
- Difficult to extend as project requirements evolve.
- May not represent the required business domain.

### Commit large CSV files

Advantages

- Immediately available after cloning.

Disadvantages

- Increases repository size.
- Difficult to maintain.
- Poor Git history.
- Not suitable for generating multiple data volumes.

## Consequences

### Benefits

- Reproducible datasets.
- Complete control over business entities.
- Configurable dataset sizes.
- Ability to simulate data quality issues.
- Lightweight Git repository.

### Trade-offs

- Additional code to maintain.
- Generated data is synthetic rather than reflecting real production distributions.