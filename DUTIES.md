# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitDataPrivacy** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitDataPrivacy Automation Engine`
* **Responsibilities**:
  * Audits database data schemas, verifies lawful processing records, and flags over-retained assets.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitDataPrivacy Verification & Policy Enforcer`
* **Responsibilities**:
  * Validates third-party data processor DPA agreements and international transfer impact assessments.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Data Protection Officer (DPO) / Chief Privacy Officer (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
