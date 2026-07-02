import json
from pathlib import Path

from k8s_analyzer import analyze_pod_status
from ai_summary import generate_ai_summary
from report_generator import generate_html_report


def main():
    base_path = Path(__file__).resolve().parent.parent

    with open(base_path / "samples" / "pod-status.json", "r", encoding="utf-8") as file:
        pod_data = json.load(file)

    with open(base_path / "samples" / "logs.txt", "r", encoding="utf-8") as file:
        logs = file.read()

    findings = analyze_pod_status(pod_data)
    summary = generate_ai_summary(pod_data, findings, logs)

    print(summary)

    report_path = generate_html_report(summary)
    print(f"\nHTML report generated: {report_path}")


if __name__ == "__main__":
    main()