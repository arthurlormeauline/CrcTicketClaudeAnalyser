import json
import sys
import os
from pathlib import Path

def load_data(data_dir):
    data_path = Path(data_dir)
    temp_dir = data_path / 'temp'

    with open(temp_dir / 'tickets_old.json', 'r', encoding='utf-8') as f:
        old_tickets = json.load(f)

    with open(temp_dir / 'tickets_for_analysis.json', 'r', encoding='utf-8') as f:
        analyzed_tickets = json.load(f)

    with open(temp_dir / 'manual_classifications.json', 'r', encoding='utf-8') as f:
        manual_classifications = json.load(f)

    manual_classifications = {int(k): v for k, v in manual_classifications.items()}

    return old_tickets, analyzed_tickets, manual_classifications

def extract_all_categories(old_tickets, analyzed_tickets, manual_classifications):
    categories = set(['Ticket ancien'])

    for ticket in analyzed_tickets:
        tid = ticket['ticket_id']
        if tid in manual_classifications:
            categories.update(manual_classifications[tid])

    return sorted(list(categories))

def create_classification_map(old_tickets, analyzed_tickets, manual_classifications):
    classification_map = {}

    for ticket in old_tickets:
        tid = ticket['ticket_id']
        classification_map[tid] = {
            'title': ticket.get('title', ''),
            'crm_url': ticket['crm_url'],
            'backoffice_url': ticket['backoffice_url'],
            'categories': ['Ticket ancien'],
            'creation_date': ticket.get('creation_date'),
            'has_usage_mention': ticket.get('has_usage_mention', True)
        }

    for ticket in analyzed_tickets:
        tid = ticket['ticket_id']
        if tid not in manual_classifications:
            print(f"ATTENTION: Ticket {tid} n'a pas de classification. Ignore.")
            continue

        cats = manual_classifications[tid]
        classification_map[tid] = {
            'title': ticket.get('title', ''),
            'crm_url': ticket['crm_url'],
            'backoffice_url': ticket['backoffice_url'],
            'categories': cats,
            'creation_date': ticket.get('creation_date'),
            'has_usage_mention': ticket.get('has_usage_mention', True)
        }

    return classification_map

def generate_html(classification_map, categories, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="fr">\n')
        f.write('<head>\n')
        f.write('    <meta charset="UTF-8">\n')
        f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('    <title>Classification des tickets CRC</title>\n')
        f.write('    <style>\n')
        f.write('        body {\n')
        f.write('            font-family: Arial, sans-serif;\n')
        f.write('            max-width: 1400px;\n')
        f.write('            margin: 0 auto;\n')
        f.write('            padding: 20px;\n')
        f.write('            background-color: #f5f5f5;\n')
        f.write('        }\n')
        f.write('        h1 {\n')
        f.write('            color: #333;\n')
        f.write('            border-bottom: 3px solid #007bff;\n')
        f.write('            padding-bottom: 10px;\n')
        f.write('        }\n')
        f.write('        .category-section {\n')
        f.write('            margin: 20px 0;\n')
        f.write('            background: white;\n')
        f.write('            border-radius: 5px;\n')
        f.write('            box-shadow: 0 2px 4px rgba(0,0,0,0.1);\n')
        f.write('        }\n')
        f.write('        .category-header {\n')
        f.write('            display: flex;\n')
        f.write('            justify-content: space-between;\n')
        f.write('            align-items: center;\n')
        f.write('            padding: 15px 20px;\n')
        f.write('            cursor: pointer;\n')
        f.write('            background: #007bff;\n')
        f.write('            color: white;\n')
        f.write('            border-radius: 5px;\n')
        f.write('            user-select: none;\n')
        f.write('        }\n')
        f.write('        .category-header:hover {\n')
        f.write('            background: #0056b3;\n')
        f.write('        }\n')
        f.write('        .category-title {\n')
        f.write('            font-size: 1.2em;\n')
        f.write('            font-weight: bold;\n')
        f.write('        }\n')
        f.write('        .category-count {\n')
        f.write('            font-size: 0.9em;\n')
        f.write('            opacity: 0.9;\n')
        f.write('        }\n')
        f.write('        .category-content {\n')
        f.write('            max-height: 0;\n')
        f.write('            overflow: hidden;\n')
        f.write('            transition: max-height 0.3s ease;\n')
        f.write('        }\n')
        f.write('        .category-content.active {\n')
        f.write('            max-height: 10000px;\n')
        f.write('        }\n')
        f.write('        .ticket-list {\n')
        f.write('            padding: 15px;\n')
        f.write('        }\n')
        f.write('        .ticket-item {\n')
        f.write('            background-color: #f9f9f9;\n')
        f.write('            margin: 5px 0;\n')
        f.write('            padding: 8px 12px;\n')
        f.write('            border-radius: 3px;\n')
        f.write('            border-left: 3px solid #007bff;\n')
        f.write('            font-size: 0.9em;\n')
        f.write('        }\n')
        f.write('        .ticket-item span {\n')
        f.write('            margin-right: 10px;\n')
        f.write('        }\n')
        f.write('        .ticket-id {\n')
        f.write('            font-weight: bold;\n')
        f.write('            color: #333;\n')
        f.write('        }\n')
        f.write('        a {\n')
        f.write('            color: #007bff;\n')
        f.write('            text-decoration: none;\n')
        f.write('            margin-right: 8px;\n')
        f.write('        }\n')
        f.write('        a:hover {\n')
        f.write('            text-decoration: underline;\n')
        f.write('        }\n')
        f.write('        .ticket-title {\n')
        f.write('            color: #666;\n')
        f.write('            font-style: italic;\n')
        f.write('        }\n')
        f.write('        .ticket-date {\n')
        f.write('            color: #888;\n')
        f.write('            font-size: 0.85em;\n')
        f.write('            margin-left: 10px;\n')
        f.write('        }\n')
        f.write('        .ticket-source {\n')
        f.write('            color: #999;\n')
        f.write('            font-size: 0.8em;\n')
        f.write('            font-style: italic;\n')
        f.write('            margin-left: 10px;\n')
        f.write('        }\n')
        f.write('        .toggle-icon {\n')
        f.write('            transition: transform 0.3s ease;\n')
        f.write('        }\n')
        f.write('        .toggle-icon.active {\n')
        f.write('            transform: rotate(90deg);\n')
        f.write('        }\n')
        f.write('    </style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('    <h1>Classification des tickets CRC</h1>\n\n')

        category_order = ['Ticket ancien', 'Sans @Usage'] + [cat for cat in sorted(categories) if cat not in ['Ticket ancien', 'Sans @Usage']]

        for idx, category in enumerate(category_order):
            if category not in categories:
                continue

            tickets_in_category = [tid for tid, info in classification_map.items() if category in info['categories']]

            tickets_in_category_sorted = sorted(
                tickets_in_category,
                key=lambda tid: classification_map[tid].get('creation_date') or '0000-00-00',
                reverse=True
            )

            f.write(f'    <div class="category-section">\n')
            f.write(f'        <div class="category-header" onclick="toggleCategory({idx})">\n')
            f.write(f'            <div>\n')
            f.write(f'                <span class="category-title">{category}</span>\n')
            f.write(f'                <span class="category-count">({len(tickets_in_category)} tickets)</span>\n')
            f.write(f'            </div>\n')
            f.write(f'            <span class="toggle-icon" id="icon-{idx}">&#9654;</span>\n')
            f.write(f'        </div>\n')
            f.write(f'        <div class="category-content" id="content-{idx}">\n')
            f.write(f'            <div class="ticket-list">\n')

            for ticket_id in tickets_in_category_sorted:
                info = classification_map[ticket_id]
                title = info.get('title', '')
                creation_date = info.get('creation_date', '')
                has_usage_mention = info.get('has_usage_mention', True)

                f.write(f'                <div class="ticket-item">\n')
                f.write(f'                    <span class="ticket-id">{ticket_id}</span>\n')
                if creation_date:
                    f.write(f'                    <span class="ticket-date">{creation_date}</span>\n')
                f.write(f'                    <a href="{info["crm_url"]}" target="_blank">CRM</a>\n')
                f.write(f'                    <a href="{info["backoffice_url"]}" target="_blank">Back-office</a>\n')
                if title:
                    f.write(f'                    <span class="ticket-title">{title}</span>\n')
                if not has_usage_mention:
                    f.write(f'                    <span class="ticket-source">(sans @usage)</span>\n')
                f.write(f'                </div>\n')

            f.write(f'            </div>\n')
            f.write(f'        </div>\n')
            f.write(f'    </div>\n\n')

        f.write('    <script>\n')
        f.write('        function toggleCategory(id) {\n')
        f.write('            const content = document.getElementById("content-" + id);\n')
        f.write('            const icon = document.getElementById("icon-" + id);\n')
        f.write('            content.classList.toggle("active");\n')
        f.write('            icon.classList.toggle("active");\n')
        f.write('        }\n')
        f.write('    </script>\n')
        f.write('</body>\n')
        f.write('</html>\n')

def cleanup_intermediate_files(data_dir):
    data_path = Path(data_dir)
    temp_dir = data_path / 'temp'

    if not temp_dir.exists():
        return

    print("\nNettoyage des fichiers intermediaires...")

    for file_path in temp_dir.iterdir():
        if file_path.is_file():
            os.remove(file_path)
            print(f"- {file_path.name} supprime")

    temp_dir.rmdir()
    print(f"- Dossier temp supprime")

def main():
    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent

    print("Chargement des donnees...")
    old_tickets, analyzed_tickets, manual_classifications = load_data(parent_dir)

    print(f"Tickets anciens: {len(old_tickets)}")
    print(f"Tickets analyses: {len(analyzed_tickets)}")
    print(f"Classifications chargees: {len(manual_classifications)}")

    print("\nExtraction des categories...")
    categories = extract_all_categories(old_tickets, analyzed_tickets, manual_classifications)
    print(f"Categories identifiees: {len(categories)}")
    for cat in categories:
        print(f"  - {cat}")

    print("\nCreation de la map de classification...")
    classification_map = create_classification_map(old_tickets, analyzed_tickets, manual_classifications)

    print(f"Total tickets classifies: {len(classification_map)}")

    output_path = parent_dir / 'tickets_classification_final.html'
    print(f"\nGeneration du HTML: {output_path.name}")
    generate_html(classification_map, categories, output_path)

    print("\nRecapitulatif par categorie:")
    category_counts = {cat: 0 for cat in categories}
    for info in classification_map.values():
        for cat in info['categories']:
            category_counts[cat] += 1

    for cat, count in category_counts.items():
        print(f"  {cat}: {count}")

    print(f"\nFichier HTML genere: {output_path}")

    cleanup_intermediate_files(parent_dir)
    print("\nTermine!")

if __name__ == '__main__':
    main()
