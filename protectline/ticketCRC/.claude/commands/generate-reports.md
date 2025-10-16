---
description: Genere les rapports finaux (arguments $1 : index de l'analyse)
---

Execute le script de generation complete des rapports finaux.

Ce script regroupe automatiquement :
- La fusion de toutes les classifications des batches
- L'analyse de la distribution des themes
- La consolidation des categories si necessaire
- La generation des rapports HTML et JSON finaux

Lance le script Python scripts/generate/generate_all.py avec l'index d'analyse fourni en argument (par defaut 0).

## Prerequis

Les commandes /prepare-data et /analyse-tickets doivent avoir ete executees au prealable.

## Fichiers generes

Les rapports finaux sont crees dans `output/` :
- `tickets_classification_final.html` - Rapport HTML interactif
- `analyse_finale.json` - Donnees structurees JSON

Les fichiers intermediaires sont conserves dans `temp/` pour tracabilite.
