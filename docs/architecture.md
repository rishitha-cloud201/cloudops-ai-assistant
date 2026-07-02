# Architecture

CloudOps AI Assistant follows a simple operational troubleshooting workflow.

## Workflow

1. Kubernetes pod status data is collected.
2. Application logs are reviewed.
3. Python analysis identifies common failure patterns.
4. AI-style logic generates a troubleshooting summary.
5. An HTML incident report is created for documentation.

## Components

- `main.py` controls the workflow.
- `k8s_analyzer.py` checks pod health and restart patterns.
- `ai_summary.py` generates troubleshooting recommendations.
- `report_generator.py` creates a simple incident report.
- `samples/` contains example pod and log data.
