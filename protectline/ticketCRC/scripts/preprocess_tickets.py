import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_usage_mentions(ticket_id, ticket_details):
    usage_mentions = []
    if str(ticket_id) in ticket_details:
        detail = ticket_details[str(ticket_id)]
        if 'details' in detail and 'ticketComment' in detail['details']:
            comments = detail['details']['ticketComment']
            for comment in comments:
                comment_text = comment.get('comment', '')
                comment_text_lower = comment_text.lower()
                if '@usage' or '@usages' in comment_text_lower:
                    usage_mentions.append({
                        'date': comment.get('createdAt'),
                        'text': comment_text
                    })
    return usage_mentions

def get_all_comments(ticket_id, ticket_details):
    comments = []
    if str(ticket_id) in ticket_details:
        detail = ticket_details[str(ticket_id)]
        if 'details' in detail and 'ticketComment' in detail['details']:
            for comment in detail['details']['ticketComment']:
                comments.append(comment.get('comment', ''))
    return comments

def get_ticket_title(ticket_id, ticket_details):
    if str(ticket_id) in ticket_details:
        detail = ticket_details[str(ticket_id)]
        if 'ticket' in detail and 'details' in detail['ticket'] and 'ticketDetail' in detail['ticket']['details']:
            return detail['ticket']['details']['ticketDetail'].get('title', '')
    return ''

def get_ticket_creation_date(ticket_id, ticket_details):
    if str(ticket_id) in ticket_details:
        detail = ticket_details[str(ticket_id)]
        if 'ticket' in detail and 'details' in detail['ticket'] and 'ticketDetail' in detail['ticket']['details']:
            created_at = detail['ticket']['details']['ticketDetail'].get('createdAt')
            if created_at:
                return datetime.fromtimestamp(created_at / 1000)

        if 'details' in detail and 'ticketComment' in detail['details']:
            comments = detail['details']['ticketComment']
            if comments:
                first_comment_date = min(comment.get('createdAt', float('inf')) for comment in comments)
                if first_comment_date != float('inf'):
                    return datetime.fromtimestamp(first_comment_date / 1000)
    return None

def is_old_ticket(usage_mentions):
    if not usage_mentions:
        return False

    now = datetime.now()
    three_months_ago = now - timedelta(days=90)

    first_usage_date = min(mention['date'] for mention in usage_mentions)
    first_usage_datetime = datetime.fromtimestamp(first_usage_date / 1000)

    return first_usage_datetime < three_months_ago

def preprocess_tickets(data):
    tickets = data['tickets']
    ticket_details = data['ticketDetails']

    old_tickets = []
    need_analysis = []

    for ticket in tickets:
        ticket_id = ticket['ticketId']
        contract_id = ticket['subscriptionCode']

        usage_mentions = get_usage_mentions(ticket_id, ticket_details)
        all_comments = get_all_comments(ticket_id, ticket_details)
        ticket_title = get_ticket_title(ticket_id, ticket_details)
        creation_date = get_ticket_creation_date(ticket_id, ticket_details)

        ticket_data = {
            'ticket_id': ticket_id,
            'contract_id': contract_id,
            'title': ticket_title,
            'crm_url': f'https://crm.teamoffre.prod.protectline.fr/main/tickets/edit/{ticket_id}',
            'backoffice_url': f'https://back-office-fe.teamusages.prod.internal/dashboard?contractId={contract_id}',
            'creation_date': creation_date.strftime('%Y-%m-%d') if creation_date else None,
            'has_usage_mention': len(usage_mentions) > 0
        }

        if usage_mentions and is_old_ticket(usage_mentions):
            first_date = datetime.fromtimestamp(min(m['date'] for m in usage_mentions) / 1000)
            ticket_data['first_usage_date'] = first_date.strftime('%Y-%m-%d')
            old_tickets.append(ticket_data)
        else:
            if usage_mentions:
                ticket_data['usage_mentions'] = [m['text'] for m in usage_mentions]
            ticket_data['all_comments'] = all_comments
            need_analysis.append(ticket_data)

    return old_tickets, need_analysis

def save_results(old_tickets, need_analysis, output_dir):
    output_path = Path(output_dir)
    temp_dir = output_path / 'temp'
    temp_dir.mkdir(exist_ok=True)

    with open(temp_dir / 'tickets_old.json', 'w', encoding='utf-8') as f:
        json.dump(old_tickets, f, indent=2, ensure_ascii=False)

    with open(temp_dir / 'tickets_for_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(need_analysis, f, indent=2, ensure_ascii=False)

    with open(temp_dir / 'tickets_for_llm_analysis.txt', 'w', encoding='utf-8') as f:
        for idx, ticket in enumerate(need_analysis, 1):
            f.write(f"{'='*80}\n")
            f.write(f"TICKET {idx}/{len(need_analysis)} - ID: {ticket['ticket_id']}\n")
            if not ticket['has_usage_mention']:
                f.write(f"[TICKET SANS @USAGE - A ANALYSER QUAND MEME]\n")
            f.write(f"{'='*80}\n")
            f.write(f"CRM: {ticket['crm_url']}\n")
            f.write(f"BackOffice: {ticket['backoffice_url']}\n")
            if ticket.get('creation_date'):
                f.write(f"Date creation: {ticket['creation_date']}\n")
            f.write(f"\n")

            if ticket.get('usage_mentions'):
                f.write(f"--- MENTIONS @Usage ---\n")
                for mention in ticket['usage_mentions']:
                    f.write(f"{mention}\n\n")
            else:
                f.write(f"--- PAS DE MENTION @Usage ---\n\n")

            f.write(f"--- TOUS LES COMMENTAIRES ---\n")
            for i, comment in enumerate(ticket['all_comments'], 1):
                f.write(f"[{i}] {comment}\n\n")

            f.write(f"\n")

if __name__ == '__main__':
    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent
    input_dir = parent_dir / 'input'

    if not input_dir.exists():
        print("Erreur: Le dossier 'input' n'existe pas")
        sys.exit(1)

    json_files = list(input_dir.glob('*.json'))
    if not json_files:
        print("Erreur: Aucun fichier *.json trouve dans le dossier input/")
        sys.exit(1)

    if len(json_files) > 1:
        print("Plusieurs fichiers JSON trouves. Veuillez specifier lequel utiliser:")
        for i, f in enumerate(json_files, 1):
            print(f"{i}. {f.name}")
        sys.exit(1)

    json_path = json_files[0]
    print(f"Utilisation du fichier: {json_path.name}")

    print("\nChargement des donnees...")
    data = load_data(json_path)

    print("Pre-traitement en cours...")
    old_tickets, need_analysis = preprocess_tickets(data)

    tickets_with_usage = sum(1 for t in need_analysis if t['has_usage_mention'])
    tickets_without_usage = sum(1 for t in need_analysis if not t['has_usage_mention'])

    print(f"\nResultats du pre-traitement:")
    print(f"- Tickets anciens (>3 mois): {len(old_tickets)}")
    print(f"- Tickets a analyser:")
    print(f"  * Avec @Usage: {tickets_with_usage}")
    print(f"  * Sans @Usage: {tickets_without_usage}")
    print(f"  * Total a analyser: {len(need_analysis)}")
    print(f"- Total general: {len(old_tickets) + len(need_analysis)}")

    print("\nSauvegarde des resultats...")
    save_results(old_tickets, need_analysis, parent_dir)

    print("\nFichiers crees dans temp/:")
    print("- tickets_old.json (tickets anciens)")
    print("- tickets_for_analysis.json (tous les tickets a analyser, avec et sans @Usage)")
    print("- tickets_for_llm_analysis.txt (version lisible)")
