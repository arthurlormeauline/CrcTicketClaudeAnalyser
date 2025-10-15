import json
from pathlib import Path
from datetime import datetime
from collections import Counter

def generate_text_report():
    with open("temp/tickets_for_analysis.json", 'r', encoding='utf-8') as f:
        tickets = json.load(f)

    with open("temp/tickets_classifications.json", 'r', encoding='utf-8') as f:
        classifications = json.load(f)

    output = []
    output.append("=" * 80)
    output.append("ANALYSE DES TICKETS CRC - RAPPORT FINAL")
    output.append("=" * 80)
    output.append(f"Date de generation: {datetime.now().strftime('%d/%m/%Y a %H:%M')}")
    output.append("")

    output.append("STATISTIQUES GENERALES")
    output.append("-" * 80)
    output.append(f"Total tickets analyses: {len(tickets)}")
    output.append(f"Tickets classifies: {len(classifications)}")
    output.append(f"Themes identifies: {len(set(theme for themes in classifications.values() for theme in themes))}")
    output.append(f"Tickets avec mention @Usage: {sum(1 for t in tickets if t.get('has_usage_mention', False))}")
    output.append("")

    themes_stats = {}
    for ticket_id, themes in classifications.items():
        for theme in themes:
            if theme not in themes_stats:
                themes_stats[theme] = []
            themes_stats[theme].append(ticket_id)

    output.append("DISTRIBUTION DES THEMES")
    output.append("-" * 80)
    for theme, ticket_ids in sorted(themes_stats.items(), key=lambda x: len(x[1]), reverse=True):
        count = len(ticket_ids)
        percentage = (count / len(classifications)) * 100
        bar = "#" * int(percentage / 2)
        output.append(f"{theme:.<40} {count:>4} tickets ({percentage:>5.1f}%) {bar}")
    output.append("")

    tickets_by_id = {str(t["ticket_id"]): t for t in tickets}

    output.append("THEMES PRINCIPAUX - TOP 5")
    output.append("-" * 80)
    top_themes = sorted(themes_stats.items(), key=lambda x: len(x[1]), reverse=True)[:5]

    for i, (theme, ticket_ids) in enumerate(top_themes, 1):
        output.append(f"\n{i}. {theme.upper()} ({len(ticket_ids)} tickets)")
        output.append("   " + "-" * 76)

        for ticket_id in sorted(ticket_ids, reverse=True)[:5]:
            ticket = tickets_by_id.get(ticket_id, {})
            contract_id = ticket.get("contract_id", "N/A")
            crm_url = ticket.get("crm_url", "#")
            has_usage = "[USAGE]" if ticket.get("has_usage_mention", False) else ""
            output.append(f"   - Ticket #{ticket_id} {has_usage}")
            output.append(f"     Contrat: {contract_id}")
            output.append(f"     URL: {crm_url}")

        if len(ticket_ids) > 5:
            output.append(f"   ... et {len(ticket_ids) - 5} autres tickets")

    output.append("")

    usage_by_theme = {}
    for ticket_id, themes in classifications.items():
        ticket = tickets_by_id.get(ticket_id, {})
        has_usage = ticket.get("has_usage_mention", False)
        if has_usage:
            for theme in themes:
                usage_by_theme[theme] = usage_by_theme.get(theme, 0) + 1

    output.append("MENTIONS @USAGE PAR THEME")
    output.append("-" * 80)
    for theme in sorted(themes_stats.keys()):
        total = len(themes_stats[theme])
        with_usage = usage_by_theme.get(theme, 0)
        percentage = (with_usage / total * 100) if total > 0 else 0
        output.append(f"{theme:.<40} {with_usage:>3}/{total:<3} ({percentage:>5.1f}%)")
    output.append("")

    multi_theme_tickets = [(tid, themes) for tid, themes in classifications.items() if len(themes) > 1]
    output.append("TICKETS AVEC THEMES MULTIPLES")
    output.append("-" * 80)
    output.append(f"Nombre de tickets avec themes multiples: {len(multi_theme_tickets)}")
    output.append("")
    for ticket_id, themes in sorted(multi_theme_tickets, key=lambda x: len(x[1]), reverse=True)[:10]:
        output.append(f"Ticket #{ticket_id}: {', '.join(themes)}")
    output.append("")

    output.append("RECOMMANDATIONS")
    output.append("-" * 80)
    top_3_themes = sorted(themes_stats.items(), key=lambda x: len(x[1]), reverse=True)[:3]
    output.append("1. Prioriser les themes suivants pour resolution:")
    for theme, ticket_ids in top_3_themes:
        output.append(f"   - {theme} ({len(ticket_ids)} tickets)")
    output.append("")
    output.append("2. Analyser en detail les tickets avec @Usage pour identifier des bugs")
    output.append("3. Etudier les cas de themes multiples pour identifier des patterns")
    output.append("")

    output.append("=" * 80)
    output.append("FIN DU RAPPORT")
    output.append("=" * 80)

    report_text = "\n".join(output)

    output_file = Path("analyse_tickets_rapport_final.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(report_text)
    print(f"\nRapport texte sauvegarde dans: {output_file}")

if __name__ == "__main__":
    generate_text_report()
