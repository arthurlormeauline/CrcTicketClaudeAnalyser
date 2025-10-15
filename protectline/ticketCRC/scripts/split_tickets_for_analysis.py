#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def split_tickets_into_batches(input_file, output_dir, index, batch_size=15):
    """
    Decoupe le fichier tickets_for_analysis.json en plusieurs petits fichiers
    pour permettre a Claude de les lire et analyser manuellement
    """
    print(f"Chargement du fichier {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        tickets = json.load(f)

    # Tri par date de creation (du plus recent au plus ancien)
    print("Tri des tickets par date de creation...")
    tickets_sorted = sorted(
        tickets,
        key=lambda t: t.get('creation_date') or '1970-01-01',
        reverse=True
    )

    total_tickets = len(tickets_sorted)
    print(f"Total de tickets: {total_tickets}")

    # Creer le dossier de sortie
    output_dir.mkdir(parents=True, exist_ok=True)

    # Decouper en batches
    num_batches = (total_tickets + batch_size - 1) // batch_size
    print(f"Creation de {num_batches} batches de {batch_size} tickets maximum\n")

    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, total_tickets)
        batch = tickets_sorted[start_idx:end_idx]

        batch_filename = f"batch_{i+1:02d}_{index}.json"
        batch_path = output_dir / batch_filename

        with open(batch_path, 'w', encoding='utf-8') as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        print(f"Cree: {batch_filename} ({len(batch)} tickets)")

    print(f"\nTous les batches ont ete crees dans {output_dir}/")
    print(f"\nClaude peut maintenant lire et analyser chaque batch manuellement :")
    print(f"- Lire temp/batches/batch_01_{index}.json avec l'outil Read")
    print(f"- Analyser les mentions @Usage et le contexte")
    print(f"- Identifier les themes manuellement")
    print(f"- Passer au batch suivant")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERREUR: L'index d'analyse est requis")
        print("Usage: python scripts/split_tickets_for_analysis.py <index>")
        print("Exemple: python scripts/split_tickets_for_analysis.py 01")
        exit(1)

    index = sys.argv[1]

    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent
    temp_dir = parent_dir / 'temp'

    input_file = temp_dir / 'tickets_for_analysis.json'
    output_dir = temp_dir / 'batches'

    if not input_file.exists():
        print(f"ERREUR: Le fichier {input_file} n'existe pas")
        print("Executez d'abord: python scripts/preprocess_tickets.py")
        exit(1)

    split_tickets_into_batches(input_file, output_dir, index, batch_size=15)
