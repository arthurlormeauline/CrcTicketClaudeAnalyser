#!/usr/bin/env python3
import json
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import TEMP_DIR

def analyze_themes(index='0'):
    """Analyse les themes et identifie les categories principales"""

    # Charger les classifications
    classifications_file = TEMP_DIR / f"manual_classifications_{index}.json"
    if not classifications_file.exists():
        # Fallback sur le fichier sans index
        classifications_file = TEMP_DIR / "tickets_classifications.json"

    with open(classifications_file, 'r', encoding='utf-8') as f:
        classifications = json.load(f)

    # Compter les themes
    theme_counter = Counter()
    for ticket_id, themes in classifications.items():
        for theme in themes:
            theme_counter[theme] += 1

    print(f"=== ANALYSE DES THEMES ===\n")
    print(f"Total de tickets: {len(classifications)}")
    print(f"Total de themes uniques: {len(theme_counter)}\n")

    # Trier par frequence
    print("=== THEMES PAR FREQUENCE ===\n")
    for theme, count in theme_counter.most_common():
        percentage = (count / len(classifications)) * 100
        print(f"{count:3d} ({percentage:5.1f}%) - {theme}")

    # Grouper par categories semantiques
    categories = {
        "Detection Camera": [],
        "Connexion Camera": [],
        "Live/Video Camera": [],
        "Appairage Camera": [],
        "Infrarouge Camera": [],
        "Autres Problemes Camera": [],
        "Notifications": [],
        "Module GSM/SIM": [],
        "Centrale": [],
        "Supervision": [],
        "Demandes Equipement": [],
        "Problemes Application": [],
        "Alarme/Intrusion": [],
        "Autres": []
    }

    for theme, count in theme_counter.items():
        theme_lower = theme.lower()

        if "detection" in theme_lower and "camera" in theme_lower:
            categories["Detection Camera"].append((theme, count))
        elif "connexion" in theme_lower and "camera" in theme_lower:
            categories["Connexion Camera"].append((theme, count))
        elif "live" in theme_lower or "video" in theme_lower or "clip" in theme_lower or "ecran noir" in theme_lower:
            categories["Live/Video Camera"].append((theme, count))
        elif "appairage" in theme_lower and "camera" in theme_lower:
            categories["Appairage Camera"].append((theme, count))
        elif "infrarouge" in theme_lower:
            categories["Infrarouge Camera"].append((theme, count))
        elif "camera" in theme_lower:
            categories["Autres Problemes Camera"].append((theme, count))
        elif "notification" in theme_lower:
            categories["Notifications"].append((theme, count))
        elif "gsm" in theme_lower or "sim" in theme_lower:
            categories["Module GSM/SIM"].append((theme, count))
        elif "centrale" in theme_lower:
            categories["Centrale"].append((theme, count))
        elif "supervision" in theme_lower:
            categories["Supervision"].append((theme, count))
        elif "demande" in theme_lower and ("suppression" in theme_lower or "ajout" in theme_lower or "reintegration" in theme_lower):
            categories["Demandes Equipement"].append((theme, count))
        elif "application" in theme_lower or "affichage" in theme_lower:
            categories["Problemes Application"].append((theme, count))
        elif "alarme" in theme_lower or "intrusion" in theme_lower or "declenchement" in theme_lower:
            categories["Alarme/Intrusion"].append((theme, count))
        else:
            categories["Autres"].append((theme, count))

    print("\n\n=== GROUPEMENT PAR CATEGORIES ===\n")

    total_tickets = len(classifications)
    for category, themes in categories.items():
        if themes:
            category_count = sum(count for _, count in themes)
            category_percentage = (category_count / total_tickets) * 100
            print(f"\n{category} - {category_count} tickets ({category_percentage:.1f}%)")
            print("-" * 60)
            for theme, count in sorted(themes, key=lambda x: x[1], reverse=True):
                percentage = (count / total_tickets) * 100
                print(f"  {count:3d} ({percentage:5.1f}%) - {theme}")

    # Sauvegarder l'analyse
    output = {
        "total_tickets": len(classifications),
        "total_themes": len(theme_counter),
        "themes_by_frequency": [{"theme": theme, "count": count} for theme, count in theme_counter.most_common()],
        "categories": {
            category: [{"theme": theme, "count": count} for theme, count in themes]
            for category, themes in categories.items()
            if themes
        }
    }

    output_file = TEMP_DIR / "themes_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n\nAnalyse sauvegardee dans: {output_file}")

if __name__ == "__main__":
    index = sys.argv[1] if len(sys.argv) > 1 else '0'
    analyze_themes(index)
