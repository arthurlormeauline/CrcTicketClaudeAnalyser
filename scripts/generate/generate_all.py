#!/usr/bin/env python3
"""
Script de generation complete des rapports finaux.
Regroupe tous les scripts de generation et consolidation necessaires.
"""

import subprocess
import sys
import os
import shutil

def run_script(script_name, *args):
    """Execute un script Python et gere les erreurs."""
    print(f"\n{'='*80}")
    print(f"Execution de {script_name}...")
    print(f"{'='*80}\n")

    cmd = [sys.executable, f"scripts/generate/{script_name}"] + list(args)
    result = subprocess.run(cmd, capture_output=False, text=True)

    if result.returncode != 0:
        print(f"\nERREUR lors de l'execution de {script_name}")
        sys.exit(1)

    print(f"\n{script_name} termine avec succes\n")

def main():
    """Genere tous les rapports finaux."""
    print("\n" + "="*80)
    print("GENERATION DES RAPPORTS FINAUX")
    print("="*80 + "\n")

    # Recuperer l'index d'analyse
    index = sys.argv[1] if len(sys.argv) > 1 else "0"

    # Etape 1 : Fusion des classifications de tous les batches
    # IMPORTANT: Ne pas refusionner si le fichier consolide existe deja
    consolidated_file = f"temp/manual_classifications_{index}.json"
    if os.path.exists(consolidated_file):
        print(f"\nFichier consolide trouve: {consolidated_file}")
        print("Utilisation du fichier consolide existant (pas de refusion des batches)")
    else:
        print(f"Fusion des classifications pour l'index '{index}'...")
        run_script("merge_batch_classifications.py", index)

    # Etape 2 : Analyse de la distribution des themes
    print("Analyse de la distribution des themes...")
    run_script("analyze_themes.py", index)

    # Etape 3 : Copier le fichier de classification avec le bon nom
    # Le script generate_final_reports cherche tickets_classifications.json
    src = f"temp/manual_classifications_{index}.json"
    dst = "temp/tickets_classifications.json"
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"\nCopie de {src} vers {dst}")

    # Etape 4 : Generation des rapports finaux (HTML + JSON)
    print("Generation des rapports finaux...")
    run_script("generate_final_reports.py")

    print("\n" + "="*80)
    print("GENERATION TERMINEE AVEC SUCCES")
    print("="*80)
    print("\nRapports generes dans output/ :")
    print("  - tickets_classification_final.html (rapport HTML interactif)")
    print("  - analyse_finale.json (donnees structurees)")
    print("\nFichiers intermediaires conserves dans temp/\n")

if __name__ == "__main__":
    main()
