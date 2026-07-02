# CloudOps AI Assistant

CloudOps AI Assistant is an AI-assisted Kubernetes troubleshooting tool designed for DevOps, SRE, and CloudOps workflows.

The project analyzes Kubernetes pod status, application logs, and failure patterns, then generates a structured troubleshooting summary with possible causes and recommended actions.

## Purpose

In real production environments, DevOps and SRE teams often investigate issues such as failed deployments, CrashLoopBackOff pods, image pull errors, and unhealthy services. This project demonstrates how Python automation and AI-assisted analysis can help reduce investigation time and improve incident response workflows.

## Features

- Kubernetes pod status analysis
- CrashLoopBackOff detection
- ImagePullBackOff detection
- Application log parsing
- AI-style troubleshooting summary
- HTML incident report generation
- Sample Kubernetes failure scenarios
- GitHub Actions Python validation workflow

## Technologies Used

- Python
- Kubernetes concepts
- Docker concepts
- YAML
- JSON
- GitHub Actions
- Linux
- AI-assisted operations

## Project Structure

```text
cloudops-ai-assistant/
├── src/
├── samples/
├── reports/
├── docs/
├── .github/workflows/
├── README.md
├── requirements.txt
└── .gitignore
```
