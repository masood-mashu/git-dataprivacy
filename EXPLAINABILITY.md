# Explainability, Auditability & Decision Logic: GitDataPrivacy

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitDataPrivacy**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitDataPrivacy** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Corporate**: Corporate RoPA registers and data mapping catalogs (OneTrust, Collibra).
- **Database**: Database table retention policies and timestamp metadata.
- **European**: European Commission Adequacy Decisions and Standard Contractual Clause templates.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **validate_ropa_record**: Uses `ropa-record-validator` to calculate validates mandatory gdpr article 30 required fields in processing activity record.
   - **enforce_retention_schedule**: Uses `retention-schedule-enforcer` to calculate flags records exceeding lawful maximum retention duration in days.
   - **audit_cross_border_transfer**: Uses `cross-border-transfer-auditor` to calculate verifies adequacy decision or executed scc agreement for international transfers.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When a processing activity or data asset is audited, the agent executes ropa_record_validator, retention_schedule_enforcer, and cross_border_transfer_auditor. If lawful basis is documented and retention compliant, it issues APPROVED. If retention policy is missing specific deletion triggers, it issues NEEDS_REVIEW. If unshielded transfers of special category data occur, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on statutory privacy regulations.
- **Does**: Does not physically wipe production database tables without dual-key DPO approval.
- **Assumes**: Assumes privacy notices provided to data subjects are transparent and unambiguous.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
