import json
import shutil
from pathlib import Path
from datetime import datetime

def generate_structured_json():
    with open("temp/tickets_for_analysis.json", 'r', encoding='utf-8') as f:
        tickets = json.load(f)

    try:
        with open("temp/tickets_old.json", 'r', encoding='utf-8') as f:
            old_tickets = json.load(f)
        tickets.extend(old_tickets)
    except FileNotFoundError:
        pass

    with open("temp/tickets_classifications.json", 'r', encoding='utf-8') as f:
        classifications = json.load(f)

    themes_stats = {}
    for ticket_id, themes in classifications.items():
        for theme in themes:
            if theme not in themes_stats:
                themes_stats[theme] = []
            themes_stats[theme].append(ticket_id)

    distribution = []
    for theme, ticket_ids in sorted(themes_stats.items(), key=lambda x: len(x[1]), reverse=True):
        count = len(ticket_ids)
        percentage = (count / len(classifications)) * 100
        distribution.append({
            "theme": theme,
            "count": count,
            "percentage": round(percentage, 1),
            "ticket_ids": sorted(ticket_ids, reverse=True)
        })

    top_3_themes = distribution[:3]
    recommendations = [
        {
            "priorite": 1,
            "titre": f"Prioriser la resolution du theme '{top_3_themes[0]['theme']}'",
            "description": f"Avec {top_3_themes[0]['count']} tickets ({top_3_themes[0]['percentage']}%), ce theme represente la problematique la plus frequente et necessite une attention immediate.",
            "actions": [
                "Analyser les causes profondes des incidents",
                "Identifier les patterns communs entre les tickets",
                "Mettre en place des actions correctives ciblees",
                "Former les equipes sur les bonnes pratiques de resolution"
            ]
        },
        {
            "priorite": 2,
            "titre": f"Traiter le theme '{top_3_themes[1]['theme']}'",
            "description": f"{top_3_themes[1]['count']} tickets ({top_3_themes[1]['percentage']}%) concernent ce theme. Une action systematique est necessaire.",
            "actions": [
                "Creer un processus standardise de traitement",
                "Automatiser les taches repetitives si possible",
                "Documenter les procedures pour les equipes CRC",
                "Suivre l'evolution du nombre de tickets dans le temps"
            ]
        },
        {
            "priorite": 3,
            "titre": f"Adresser le theme '{top_3_themes[2]['theme']}'",
            "description": f"{top_3_themes[2]['count']} tickets ({top_3_themes[2]['percentage']}%) relevent de cette categorie.",
            "actions": [
                "Evaluer l'impact sur l'experience client",
                "Identifier les ameliorations possibles du systeme",
                "Communiquer avec les equipes techniques concernees",
                "Mettre en place un suivi regulier"
            ]
        },
        {
            "priorite": 4,
            "titre": "Analyser les tickets avec mentions @Usage",
            "description": f"{sum(1 for t in tickets if t.get('has_usage_mention', False))} tickets ({round(sum(1 for t in tickets if t.get('has_usage_mention', False)) / len(tickets) * 100, 1)}%) contiennent une mention @Usage, indiquant une necessite d'intervention technique.",
            "actions": [
                "Identifier les bugs recurrents remontes a l'equipe Usage",
                "Ameliorer la collaboration CRC-Usage",
                "Reduire le temps de resolution des tickets escalades",
                "Former les equipes CRC pour eviter les escalades inutiles"
            ]
        },
        {
            "priorite": 5,
            "titre": "Suivre l'evolution des themes dans le temps",
            "description": "Mettre en place une analyse periodique pour mesurer l'efficacite des actions correctives.",
            "actions": [
                "Realiser cette analyse mensuellement",
                "Comparer l'evolution des volumes par theme",
                "Ajuster les priorites en fonction des tendances",
                "Partager les resultats avec toutes les equipes concernees"
            ]
        }
    ]

    structured_data = {
        "date_analyse": datetime.now().isoformat(),
        "statistiques": {
            "total_tickets_analyses": len(tickets),
            "tickets_classifies": len(classifications),
            "themes_identifies": len(themes_stats),
            "tickets_avec_usage": sum(1 for t in tickets if t.get("has_usage_mention", False))
        },
        "distribution_themes": distribution,
        "recommandations": recommendations
    }

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "analyse_finale.json", 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, ensure_ascii=False, indent=2)

    print(f"Fichier JSON structure genere: output/analyse_finale.json")
    return structured_data

def generate_html_with_json(structured_data):
    with open("temp/tickets_for_analysis.json", 'r', encoding='utf-8') as f:
        tickets = json.load(f)

    try:
        with open("temp/tickets_old.json", 'r', encoding='utf-8') as f:
            old_tickets = json.load(f)
        tickets.extend(old_tickets)
    except FileNotFoundError:
        pass

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
        .ticket-date {{
            color: #888;
            font-size: 13px;
            margin-left: 10px;
        }}
        .backoffice-link {{
            color: #28a745;
            text-decoration: none;
            font-size: 13px;
            margin-left: 10px;
        }}
        .backoffice-link:hover {{
            text-decoration: underline;
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
        .recommendations {{
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .recommendation-card {{
            background: #f8f9fa;
            padding: 15px;
            margin: 15px 0;
            border-left: 4px solid #28a745;
            border-radius: 4px;
        }}
        .recommendation-title {{
            color: #28a745;
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
        }}
        .recommendation-description {{
            color: #555;
            margin-bottom: 10px;
        }}
        .recommendation-actions {{
            list-style: none;
            padding-left: 20px;
        }}
        .recommendation-actions li {{
            padding: 5px 0;
            color: #666;
        }}
        .recommendation-actions li:before {{
            content: "\\2022";
            color: #28a745;
            font-weight: bold;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }}
        .json-section {{
            background: white;
            padding: 20px;
            margin: 30px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .json-content {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
        }}
        pre {{
            margin: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
    </style>
</head>
<body>
    <h1>Analyse des Tickets CRC - Rapport Final</h1>
    <p class="report-date">Genere le: {datetime.now().strftime("%d/%m/%Y a %H:%M")}</p>

    <div class="stats">
        <div class="stat-card">
            <h3>Total Tickets</h3>
            <div class="stat-number">{structured_data['statistiques']['total_tickets_analyses']}</div>
        </div>
        <div class="stat-card">
            <h3>Tickets Classifies</h3>
            <div class="stat-number">{structured_data['statistiques']['tickets_classifies']}</div>
        </div>
        <div class="stat-card">
            <h3>Themes Identifies</h3>
            <div class="stat-number">{structured_data['statistiques']['themes_identifies']}</div>
        </div>
        <div class="stat-card">
            <h3>Tickets avec @Usage</h3>
            <div class="stat-number">{structured_data['statistiques']['tickets_avec_usage']}</div>
        </div>
    </div>

    <h2>Distribution des Themes</h2>
    <div class="chart-container">
"""

    max_count = max(item['count'] for item in structured_data['distribution_themes'])
    for item in structured_data['distribution_themes']:
        bar_width = (item['count'] / max_count) * 100
        html += f"""
        <div class="bar">
            <div class="bar-label">{item['theme']}</div>
            <div class="bar-fill" style="width: {bar_width}%;">
                {item['count']} ({item['percentage']}%)
            </div>
        </div>
"""

    html += """
    </div>

    <h2>Recommandations</h2>
    <div class="recommendations">
"""

    for rec in structured_data['recommandations']:
        html += f"""
        <div class="recommendation-card">
            <div class="recommendation-title">Priorite {rec['priorite']}: {rec['titre']}</div>
            <div class="recommendation-description">{rec['description']}</div>
            <ul class="recommendation-actions">
"""
        for action in rec['actions']:
            html += f"                <li>{action}</li>\n"
        html += """            </ul>
        </div>
"""

    html += """
    </div>

    <h2>Details par Theme</h2>
"""

    tickets_by_id = {str(t["ticket_id"]): t for t in tickets}

    for item in structured_data['distribution_themes']:
        theme = item['theme']
        ticket_ids = item['ticket_ids']

        tickets_with_dates = []
        for ticket_id in ticket_ids:
            ticket = tickets_by_id.get(ticket_id, {})
            date = ticket.get("first_usage_date", ticket.get("creation_date", ""))
            tickets_with_dates.append((ticket_id, ticket, date if date else "9999-99-99"))

        tickets_with_dates.sort(key=lambda x: x[2], reverse=True)

        html += f"""
    <div class="theme-section">
        <div class="theme-header">
            <div class="theme-title">{theme}</div>
            <div class="theme-count">{item['count']} tickets ({item['percentage']}%)</div>
        </div>
        <ul class="ticket-list">
"""
        for ticket_id, ticket, date in tickets_with_dates:
            contract_id = ticket.get("contract_id", "N/A")
            crm_url = ticket.get("crm_url", "#")
            backoffice_url = ticket.get("backoffice_url", "#")
            date_display = date if date and date != "9999-99-99" else ""

            html += f"""
            <li class="ticket-item">
                <a href="{crm_url}" target="_blank" class="ticket-link">Ticket #{ticket_id}</a>
                <span class="contract-id">- Contrat: {contract_id}</span>"""

            if date_display:
                html += f"""
                <span class="ticket-date">({date_display})</span>"""

            if backoffice_url != "#":
                html += f"""
                <a href="{backoffice_url}" target="_blank" class="backoffice-link">[Back-office]</a>"""

            html += """
            </li>
"""
        html += """
        </ul>
    </div>
"""

    unclassified_tickets = []
    for ticket in tickets:
        ticket_id = str(ticket.get("ticket_id"))
        if ticket_id not in classifications:
            date = ticket.get("first_usage_date", ticket.get("creation_date", ""))
            unclassified_tickets.append((ticket_id, ticket, date if date else "9999-99-99"))

    if unclassified_tickets:
        unclassified_tickets.sort(key=lambda x: x[2], reverse=True)
        html += f"""
    <h2>Tickets Anciens (sans details de classification)</h2>
    <div class="theme-section">
        <div class="theme-header">
            <div class="theme-title">Tickets sans commentaires detailles</div>
            <div class="theme-count">{len(unclassified_tickets)} tickets</div>
        </div>
        <ul class="ticket-list">
"""
        for ticket_id, ticket, date in unclassified_tickets:
            contract_id = ticket.get("contract_id", "N/A")
            crm_url = ticket.get("crm_url", "#")
            backoffice_url = ticket.get("backoffice_url", "#")
            date_display = date if date and date != "9999-99-99" else ""

            html += f"""
            <li class="ticket-item">
                <a href="{crm_url}" target="_blank" class="ticket-link">Ticket #{ticket_id}</a>
                <span class="contract-id">- Contrat: {contract_id}</span>"""

            if date_display:
                html += f"""
                <span class="ticket-date">({date_display})</span>"""

            if backoffice_url != "#":
                html += f"""
                <a href="{backoffice_url}" target="_blank" class="backoffice-link">[Back-office]</a>"""

            html += """
            </li>
"""

        html += """
        </ul>
    </div>
"""

    html += f"""
    <h2>Donnees Structurees (JSON)</h2>
    <div class="json-section">
        <p>Les donnees completes de cette analyse sont disponibles au format JSON ci-dessous:</p>
        <div class="json-content">
            <pre>{json.dumps(structured_data, ensure_ascii=False, indent=2)}</pre>
        </div>
    </div>

</body>
</html>
"""

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "tickets_classification_final.html", 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Rapport HTML genere: output/tickets_classification_final.html")

def cleanup_temp_folder():
    temp_dir = Path("temp")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
        print(f"Dossier temp/ supprime")

def main():
    print("Generation des rapports finaux...")
    print("-" * 80)

    structured_data = generate_structured_json()
    print()

    generate_html_with_json(structured_data)
    print()

    # cleanup_temp_folder()  # Desactive pour garder les fichiers temporaires
    print("Fichiers temporaires conserves dans temp/")
    print()

    print("=" * 80)
    print("Rapports finaux generes avec succes dans output/:")
    print("  - output/tickets_classification_final.html (rapport HTML interactif)")
    print("  - output/analyse_finale.json (donnees structurees)")
    print("=" * 80)

if __name__ == "__main__":
    main()
