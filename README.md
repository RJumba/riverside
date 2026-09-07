# Riverside Hospital Workflow Automation

## Project Overview

This project models and automates the Riverside Hospital specialist referral process using i* modelling, BPMN and Camunda 8.

The workflow begins when a GP referral is received by Riverside Hospital and continues through referral validation, consultation scheduling, specialist consultation, optional laboratory investigation, final clinical outcome determination and communication of the final outcome to the patient and GP.

The project was developed as part of a workflow modelling and automation assessment.

---

## Project Objectives

The main objectives of the project are to:

- Model the Riverside Hospital socio-technical environment using i*.
- Develop Strategic Dependency and Strategic Rationale models.
- Model the current and operational business processes using BPMN.
- Implement the operational workflow in Camunda 8.
- Create user forms for the main human activities.
- Implement automated service tasks using Python job workers.
- Test the workflow, forms, gateways and automated service tasks.
- Document the implementation and testing results.

---

## Repository Structure

```text
riverside-hospital-workflow/
│
├── camunda/
│
├── docs/
│   └── process-scope-and-variables.md
│
├── models/
│   ├── bpmn/
│   │   ├── Riverside_AS_IS_Strategic.bpmn
│   │   └── Riverside_operational.bpmn
│   │
│   └── i-star/
│       ├── Strategic Dependency.drawio
│       └── Strategic Rationale.drawio
│
├── presentation/
│
├── service-tasks/
│   ├── check_referral_completeness.py
│   ├── generate_appointment_reference.py
│   └── generate_draft_outcome_letter.py
│
├── testing/
│   ├── evidence/
│   └── test-report.md
│
└── README.md