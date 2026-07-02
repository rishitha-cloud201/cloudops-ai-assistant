def generate_ai_summary(pod_data, findings, logs):
    summary = []

    summary.append("AI-Assisted Troubleshooting Summary")
    summary.append("-----------------------------------")
    summary.append(f"Namespace: {pod_data.get('namespace')}")
    summary.append(f"Pod: {pod_data.get('pod_name')}")
    summary.append(f"Status: {pod_data.get('status')}")
    summary.append("")

    summary.append("Key Findings:")
    for finding in findings:
        summary.append(f"- {finding}")

    summary.append("")
    summary.append("Log Analysis:")
    if "database" in logs.lower():
        summary.append("- Logs indicate possible database connectivity failure.")
    if "timeout" in logs.lower():
        summary.append("- Timeout errors detected. Check service networking, DNS, and backend availability.")
    if "startup failed" in logs.lower():
        summary.append("- Application startup failure detected. Review configuration and dependency health.")

    summary.append("")
    summary.append("Recommended Actions:")
    summary.append("- Check recent deployment changes.")
    summary.append("- Review Kubernetes events for the affected pod.")
    summary.append("- Validate ConfigMaps, Secrets, and environment variables.")
    summary.append("- Verify service connectivity and database availability.")
    summary.append("- Confirm readiness and liveness probe configuration.")

    return "\n".join(summary)