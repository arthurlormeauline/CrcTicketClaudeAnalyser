#!/usr/bin/env python3
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import TEMP_DIR, BATCHES_DIR

def merge_batch_classifications(batches_dir, output_file, index):
    """
    Fusionne tous les fichiers batch_XX_classifications_{index}.json
    en un seul fichier manual_classifications_{index}.json
    """

    # Trouver tous les fichiers de classification pour cet index
    pattern = f'batch_*_classifications_{index}.json'
    classification_files = sorted(batches_dir.glob(pattern))

    if not classification_files:
        print(f"ERREUR: Aucun fichier de classification trouve dans {batches_dir}")
        print(f"Les fichiers doivent suivre le pattern: batch_XX_classifications_{index}.json")
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
    if len(sys.argv) < 2:
        print("ERREUR: L'index d'analyse est requis")
        print("Usage: python scripts/merge_batch_classifications.py <index>")
        print("Exemple: python scripts/merge_batch_classifications.py 01")
        exit(1)

    index = sys.argv[1]

    batches_dir = BATCHES_DIR
    output_file = TEMP_DIR / f'manual_classifications_{index}.json'

    if not batches_dir.exists():
        print(f"ERREUR: Le dossier {batches_dir} n'existe pas")
        exit(1)

    success = merge_batch_classifications(batches_dir, output_file, index)

    if success:
        print("\nFusion terminee avec succes !")
        print(f"Fichier cree: {output_file}")
        print("Vous pouvez maintenant executer: python scripts/generate_final_reports.py")
    else:
        print("\nEchec de la fusion")
        exit(1)
