#!/usr/bin/env python3
import json
from pathlib import Path

def merge_batch_classifications(batches_dir, output_file):
    """
    Fusionne tous les fichiers batch_XX_classifications.json
    en un seul fichier manual_classifications.json
    """

    # Trouver tous les fichiers de classification
    classification_files = sorted(batches_dir.glob('batch_*_classifications.json'))

    if not classification_files:
        print(f"ERREUR: Aucun fichier de classification trouve dans {batches_dir}")
        print(f"Les fichiers doivent suivre le pattern: batch_XX_classifications.json")
        return False

    print(f"Fichiers de classification trouves: {len(classification_files)}")

    # Fusionner toutes les classifications
    merged_classifications = {}

    for filepath in classification_files:
        filename = filepath.name
        print(f"- Fusion de {filename}")

        with open(filepath, 'r', encoding='utf-8') as f:
            batch_data = json.load(f)

        # Verifier que c'est bien un dictionnaire
        if not isinstance(batch_data, dict):
            print(f"  ATTENTION: {filename} n'est pas au bon format (dictionnaire attendu)")
            continue

        # Ajouter au dictionnaire fusionne
        for ticket_id, categories in batch_data.items():
            if ticket_id in merged_classifications:
                print(f"  ATTENTION: ticket_id {ticket_id} deja present, ecrasement")
            merged_classifications[ticket_id] = categories

        print(f"  -> {len(batch_data)} tickets ajoutes")

    # Sauvegarder le fichier fusionne
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_classifications, f, indent=2, ensure_ascii=False)

    print(f"\nFichier final cree: {output_file}")
    print(f"Total de tickets classifies: {len(merged_classifications)}")

    return True

if __name__ == '__main__':
    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent
    temp_dir = parent_dir / 'temp'

    batches_dir = temp_dir / 'batches'
    output_file = temp_dir / 'manual_classifications.json'

    if not batches_dir.exists():
        print(f"ERREUR: Le dossier {batches_dir} n'existe pas")
        exit(1)

    success = merge_batch_classifications(batches_dir, output_file)

    if success:
        print("\nFusion terminee avec succes !")
        print("Vous pouvez maintenant executer: python scripts/generate_final_html.py")
    else:
        print("\nEchec de la fusion")
        exit(1)
