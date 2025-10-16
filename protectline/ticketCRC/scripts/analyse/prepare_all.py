#!/usr/bin/env python3
"""
Script de preparation complete des donnees pour l'analyse des tickets.
Regroupe tous les scripts de pre-traitement necessaires.
"""

import subprocess
import sys
import os
import argparse

def run_script(script_name, *args):
    """Execute un script Python et gere les erreurs."""
    print(f"\n{'='*80}")
    print(f"Execution de {script_name}...")
    print(f"{'='*80}\n")

    cmd = [sys.executable, f"scripts/analyse/{script_name}"] + list(args)
    result = subprocess.run(cmd, capture_output=False, text=True)

    if result.returncode != 0:
        print(f"\nERREUR lors de l'execution de {script_name}")
        sys.exit(1)

    print(f"\n{script_name} termine avec succes\n")

def main():
    """Prepare toutes les donnees pour l'analyse."""
    parser = argparse.ArgumentParser(description='Preparation des donnees pour analyse')
    parser.add_argument('index', nargs='?', default='0',
                        help='Index de l\'analyse (defaut: 0)')
    parser.add_argument('--force', action='store_true',
                        help='Extraire tous les tickets, meme ceux deja analyses')
    args = parser.parse_args()

    print("\n" + "="*80)
    print("PREPARATION DES DONNEES POUR ANALYSE")
    print("="*80 + "\n")

    # Etape 1 : Pre-traitement des tickets
    preprocess_args = []
    if args.force:
        preprocess_args.append("--force")
    run_script("preprocess_tickets.py", *preprocess_args)

    # Etape 2 : Decoupage en batches pour l'analyse
    run_script("split_tickets_for_analysis.py", args.index)

    print("\n" + "="*80)
    print("PREPARATION TERMINEE AVEC SUCCES")
    print("="*80)
    print("\nLes donnees sont pretes pour l'analyse manuelle par Claude.")
    print(f"Fichiers generes dans temp/batches/ avec l'index '{args.index}'")
    print("\nProchaine etape : executer /analyse-tickets\n")

if __name__ == "__main__":
    main()
