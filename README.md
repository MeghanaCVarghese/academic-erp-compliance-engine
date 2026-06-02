# Academic Administration & ERP Workflow Automation (Digii Simulation)

A Python-based compliance automation engine that mimics core data logic modules of standard university ERP systems like **Digii (CollPoll)**. This project demonstrates how technical automation can streamline the student lifecycle, enforce regulatory policies, and reduce manual verification overhead in a University Registrar's Office.

## 📌 Project Overview
In higher education administration, verifying student eligibility for final examinations is a massive, multi-departmental bottleneck. The Assistant Registrar's office must manually cross-reference data from:
1. **Academic Cell:** Verifying class attendance thresholds (e.g., minimum 75% attendance).
2. **Finance Department:** Checking outstanding tuition fees and pending dues.
3. **Admissions/Onboarding:** Reviewing missing mandatory registration documents.

This project builds an automated data pipeline that handles this verification instantly, achieving zero margin for error and reducing manual processing time by an estimated **80%**.

## 🛠️ Tech Stack & Skills
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy
- **Concepts:** Data Validation, Relational Logic, Business Process Automation, Regulatory Compliance Reporting, Records Management

## ⚙️ Core Workflow Modules Simulated
- **Student Lifecycle Management:** Processes core student registry attributes dynamically (IDs, departments, statuses).
- **Regulatory Policy Enforcement:** Programmatically flags or detains student records falling below compliance thresholds (e.g., `< 75%` attendance or active financial dues).
- **Cross-Departmental Actionable Reporting:** Automatically splits and exports localized, clean CSV outputs tailored for separate institutional wings (Finance, Exam Cell, and Department Heads).

## 📊 Sample Executive Compliance Report Output
When executed, the system generates an instant bird's-eye view for senior academic leadership to assess institutional readiness:

```text
--- REGISTRAR'S OFFICE COMPLIANCE REPORT ---
Total Enrolled Students: 50
Approved for Hall Tickets: 32 (64.0%)
Flagged / Detained Students: 18 (36.0%)
--------------------------------------------
Reports successfully exported as clean CSVs for institutional workflows!
