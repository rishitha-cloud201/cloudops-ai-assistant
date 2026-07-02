def generate_html_report(summary, output_path="reports/incident-report.html"):
    html_content = f"""
    <html>
    <head>
        <title>CloudOps AI Assistant Report</title>
    </head>
    <body>
        <h1>CloudOps AI Assistant Incident Report</h1>
        <pre>{summary}</pre>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    return output_path