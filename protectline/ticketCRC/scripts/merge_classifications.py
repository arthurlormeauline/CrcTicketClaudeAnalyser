import json
import os
from pathlib import Path

def merge_classifications():
    batch_dir = Path("temp/batches")
    merged_classifications = {}

    for batch_file in sorted(batch_dir.glob("batch_*_classifications.json")):
        with open(batch_file, 'r', encoding='utf-8') as f:
            batch_data = json.load(f)
            merged_classifications.update(batch_data)

    output_file = Path("temp/tickets_classifications.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_classifications, f, ensure_ascii=False, indent=2)

    print(f"Classification fusionnees: {len(merged_classifications)} tickets")

    themes_count = {}
    for themes in merged_classifications.values():
        for theme in themes:
            themes_count[theme] = themes_count.get(theme, 0) + 1

    print("\nDistribution des themes:")
    for theme, count in sorted(themes_count.items(), key=lambda x: x[1], reverse=True):
        print(f"  {theme}: {count}")

if __name__ == "__main__":
    merge_classifications()
