def analyze_pod_status(pod_data):
    findings = []

    status = pod_data.get("status", "")
    restart_count = pod_data.get("restart_count", 0)

    if status == "CrashLoopBackOff":
        findings.append("Pod is in CrashLoopBackOff state, indicating repeated container startup failure.")

    if status == "ImagePullBackOff":
        findings.append("Pod is unable to pull the container image. Verify image name, tag, and registry access.")

    if restart_count >= 5:
        findings.append(f"High restart count detected: {restart_count}. Review application logs and health checks.")

    if not findings:
        findings.append("No critical Kubernetes pod issues detected.")

    return findings