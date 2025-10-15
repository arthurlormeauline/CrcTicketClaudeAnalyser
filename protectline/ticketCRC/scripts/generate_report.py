import json
from pathlib import Path
from datetime import datetime

def generate_html_report():
    with open("temp/tickets_for_analysis.json", 'r', encoding='utf-8') as f:
        tickets = json.load(f)

    with open("temp/tickets_classifications.json", 'r', encoding='utf-8') as f:
        classifications = json.load(f)

    themes_stats = {}
    for ticket_id, themes in classifications.items():
        for theme in themes:
            if theme not in themes_stats:
                themes_stats[theme] = []
            themes_stats[theme].append(ticket_id)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analyse des Tickets CRC - Rapport Final</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #007bff;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
            border-bottom: 2px solid #ddd;
            padding-bottom: 8px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stat-card h3 {{
            margin-top: 0;
            color: #007bff;
        }}
        .stat-number {{
            font-size: 36px;
            font-weight: bold;
            color: #333;
        }}
        .theme-section {{
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .theme-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        .theme-title {{
            color: #007bff;
            font-size: 20px;
            font-weight: bold;
        }}
        .theme-count {{
            background: #007bff;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
        }}
        .ticket-list {{
            list-style: none;
            padding: 0;
        }}
        .ticket-item {{
            padding: 10px;
            margin: 5px 0;
            background: #f8f9fa;
            border-left: 4px solid #007bff;
            border-radius: 4px;
        }}
        .ticket-link {{
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }}
        .ticket-link:hover {{
            text-decoration: underline;
        }}
        .contract-id {{
            color: #666;
            font-size: 14px;
        }}
        .report-date {{
            color: #888;
            font-style: italic;
        }}
        .chart-container {{
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .bar {{
            display: flex;
            align-items: center;
            margin: 10px 0;
        }}
        .bar-label {{
            min-width: 200px;
            font-weight: bold;
        }}
        .bar-fill {{
            height: 30px;
            background: linear-gradient(90deg, #007bff, #0056b3);
            border-radius: 4px;
            display: flex;
            align-items: center;
            padding: 0 10px;
            color: white;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Analyse des Tickets CRC - Rapport Final</h1>
    <p class="report-date">Genere le: {datetime.now().strftime("%d/%m/%Y a %H:%M")}</p>

    <div class="stats">
        <div class="stat-card">
            <h3>Total Tickets</h3>
            <div class="stat-number">{len(tickets)}</div>
        </div>
        <div class="stat-card">
            <h3>Tickets Classifies</h3>
            <div class="stat-number">{len(classifications)}</div>
        </div>
        <div class="stat-card">
            <h3>Themes Identifies</h3>
            <div class="stat-number">{len(themes_stats)}</div>
        </div>
        <div class="stat-card">
            <h3>Tickets avec @Usage</h3>
            <div class="stat-number">{sum(1 for t in tickets if t.get("has_usage_mention", False))}</div>
        </div>
    </div>

    <h2>Distribution des Themes</h2>
    <div class="chart-container">
"""

    max_count = max(len(tickets) for tickets in themes_stats.values())
    for theme, ticket_ids in sorted(themes_stats.items(), key=lambda x: len(x[1]), reverse=True):
        count = len(ticket_ids)
        percentage = (count / len(classifications)) * 100
        bar_width = (count / max_count) * 100
        html += f"""
        <div class="bar">
            <div class="bar-label">{theme}</div>
            <div class="bar-fill" style="width: {bar_width}%;">
                {count} ({percentage:.1f}%)
            </div>
        </div>
"""

    html += """
    </div>

    <h2>Details par Theme</h2>
"""

    tickets_by_id = {str(t["ticket_id"]): t for t in tickets}

    for theme, ticket_ids in sorted(themes_stats.items(), key=lambda x: len(x[1]), reverse=True):
        html += f"""
    <div class="theme-section">
        <div class="theme-header">
            <div class="theme-title">{theme}</div>
            <div class="theme-count">{len(ticket_ids)} tickets</div>
        </div>
        <ul class="ticket-list">
"""
        for ticket_id in sorted(ticket_ids, reverse=True):
            ticket = tickets_by_id.get(ticket_id, {})
            contract_id = ticket.get("contract_id", "N/A")
            crm_url = ticket.get("crm_url", "#")
            html += f"""
            <li class="ticket-item">
                <a href="{crm_url}" target="_blank" class="ticket-link">Ticket #{ticket_id}</a>
                <span class="contract-id">- Contrat: {contract_id}</span>
            </li>
"""
        html += """
        </ul>
    </div>
"""

    html += """
</body>
</html>
"""

    output_file = Path("tickets_classification_final.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Rapport HTML genere: {output_file}")
    print(f"Ouvrir avec un navigateur pour visualiser le rapport complet")

if __name__ == "__main__":
    generate_html_report()
