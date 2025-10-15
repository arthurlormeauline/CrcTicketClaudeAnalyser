import json
from datetime import datetime
from pathlib import Path

def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_first_comment_date(ticket_id, ticket_details):
    if str(ticket_id) in ticket_details:
        detail = ticket_details[str(ticket_id)]
        if 'details' in detail and 'ticketComment' in detail['details']:
            comments = detail['details']['ticketComment']
            if comments:
                first_comment_date = min(comment.get('createdAt', float('inf')) for comment in comments)
                if first_comment_date != float('inf'):
                    return datetime.fromtimestamp(first_comment_date / 1000).strftime('%Y-%m-%d')
    return None

script_dir = Path(__file__).parent
parent_dir = script_dir.parent

json_files = [f for f in parent_dir.glob('*.json') if f.name.startswith('backup-')]
if not json_files:
    print("Erreur: Aucun fichier backup-*.json trouve")
    exit(1)

backup_file = json_files[0]
print(f"Utilisation du fichier: {backup_file.name}")

data = load_data(backup_file)
ticket_details = data['ticketDetails']

tickets_file = parent_dir / 'temp' / 'tickets_for_analysis.json'
with open(tickets_file, 'r', encoding='utf-8') as f:
    tickets = json.load(f)

print(f"Ajout des dates aux {len(tickets)} tickets...")

updated_count = 0
for ticket in tickets:
    ticket_id = ticket['ticket_id']
    date = get_first_comment_date(ticket_id, ticket_details)
    if date:
        ticket['creation_date'] = date
        updated_count += 1

with open(tickets_file, 'w', encoding='utf-8') as f:
    json.dump(tickets, f, indent=2, ensure_ascii=False)

print(f"Dates ajoutees pour {updated_count} tickets sur {len(tickets)}")
print(f"Fichier mis a jour: {tickets_file}")
