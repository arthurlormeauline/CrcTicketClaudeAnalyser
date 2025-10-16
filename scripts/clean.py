#!/usr/bin/env python3
"""
Script de nettoyage des fichiers temporaires et de sortie.
Supprime tous les fichiers dans temp/, temp/batches/ et output/.
"""

import shutil
import sys
from pathlib import Path

# Ajouter le repertoire parent au path pour importer config
sys.path.insert(0, str(Path(__file__).parent))
from config import TEMP_DIR, BATCHES_DIR, OUTPUT_DIR

def clean_directory(directory, description):
    """Supprime tous les fichiers dans un repertoire."""
    if not directory.exists():
        print(f"  {description}: repertoire inexistant, rien a nettoyer")
        return 0

    files_count = 0
    for item in directory.iterdir():
        if item.is_file():
            item.unlink()
            files_count += 1
        elif item.is_dir():
            shutil.rmtree(item)
            files_count += 1

    print(f"  {description}: {files_count} element(s) supprime(s)")
    return files_count

def main():
    """Nettoie tous les fichiers temporaires et de sortie."""
    print("\n" + "="*80)
    print("NETTOYAGE DES FICHIERS TEMPORAIRES ET DE SORTIE")
    print("="*80 + "\n")

    total_deleted = 0

    # Nettoyer temp/batches/
    total_deleted += clean_directory(BATCHES_DIR, "temp/batches/")

    # Nettoyer temp/ (mais garder le dossier batches/)
    if TEMP_DIR.exists():
        files_count = 0
        for item in TEMP_DIR.iterdir():
            if item.is_file():
                item.unlink()
                files_count += 1
            elif item.is_dir() and item.name != "batches":
                shutil.rmtree(item)
                files_count += 1
        print(f"  temp/: {files_count} element(s) supprime(s)")
        total_deleted += files_count
    else:
        print(f"  temp/: repertoire inexistant, rien a nettoyer")

    # Nettoyer output/
    total_deleted += clean_directory(OUTPUT_DIR, "output/")

    print("\n" + "="*80)
    print(f"NETTOYAGE TERMINE : {total_deleted} element(s) supprime(s) au total")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
