# Scalable Ads Performance Debugging & Validation System

## Overview
This project is a self-initiated, end-to-end technical solution designed to simulate how large-scale advertising systems are debugged and validated. The system identifies discrepancies in ad performance data (clicks, impressions, and conversions), prioritizes issues by severity, and stores results for scalable analysis.

The project mirrors real-world Solutions Engineering workflows, where one-off debugging scripts are transformed into reusable, data-driven tools.

---

## Problem Statement
In advertising platforms, customers often report issues such as:
- Ads receiving clicks but no recorded conversions
- Campaigns generating impressions but no user engagement
- Missing or inconsistent tracking data

Manually investigating these issues does not scale. This project demonstrates how such problems can be automatically detected, prioritized, and analyzed using Python and SQL.

---

## System Architecture

CSV Ads Performance Data
↓
Python Validation Engine
↓
Issue Classification (Severity-Based)
↓
SQLite Database
↓
SQL Queries & Debug Insights


---

## Key Features
- **Automated Validation:** Detects inconsistencies across clicks, impressions, and conversions.
- **Severity-Based Prioritization:** Classifies issues as HIGH or MEDIUM based on potential business impact.
- **Persistent Storage:** Stores validation results in a relational database for reuse and analysis.
- **SQL Analytics:** Enables querying issue patterns and prioritization trends.
- **Scalable Design:** Structured to support extension to additional rules, datasets, or outputs.

---

## Technology Stack
- **Python 3** – Core validation and orchestration logic
- **SQLite** – Lightweight relational database for issue persistence
- **SQL** – Querying and analytical insights
- **CSV** – Simulated input data
- **Git/GitHub** – Version control

 attachment 

---

Design Considerations

The system separates validation logic from persistence to improve maintainability.

Severity-based classification allows prioritization of high-impact issues.

SQLite is used for simplicity; the design can be extended to production databases.

The solution focuses on reusability rather than one-off debugging.
