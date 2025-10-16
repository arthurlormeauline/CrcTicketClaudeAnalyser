---
description: Workflow complet d'analyse des tickets CRC (arguments $1 : index de l'analyse)
---

Commande maitre qui orchestre le workflow complet d'analyse des tickets du centre d'appel.

## Workflow en 4 etapes

Le workflow se decompose en 4 etapes sequentielles :

### Etape 1 : Preparation des donnees

Execute la commande `/prepare-data $1 --force`

Cette etape prepare les donnees pour l'analyse :
- Pre-traitement des tickets (extraction, nettoyage)
- Decoupage en batches pour l'analyse manuelle

### Etape 2 : Analyse manuelle par Claude

Execute la commande `/analyse-tickets $1`

Cette etape est l'analyse manuelle par Claude :
- Lecture et comprehension des tickets
- Extraction des themes depuis les mentions @Usage
- Classification semantique basee sur le contexte
- Sauvegarde des classifications par batch

**IMPORTANT : Cette etape necessite une intervention manuelle de Claude pour analyser les tickets.**

### Etape 3 : Consolidation des categories

Execute la commande `/consolidate-categories $1`

Cette etape consolide les categories pour respecter les contraintes :
- Maximum 10-15 categories au total
- Maximum 5 categories avec un seul ticket
- Regroupement semantique des themes similaires
- Reclassification de tous les tickets

**IMPORTANT : Cette etape est critique pour avoir des rapports exploitables.**

### Etape 4 : Generation des rapports finaux

Execute la commande `/generate-reports $1`

Cette etape genere les rapports finaux :
- Fusion de toutes les classifications
- Analyse de la distribution des themes
- Generation des rapports HTML et JSON

## Utilisation

Lance les 4 commandes sequentiellement avec l'index d'analyse fourni (par defaut 0).

## Fichiers generes

- `temp/batches/` : Fichiers intermediaires de decoupage et classifications
- `output/tickets_classification_final.html` : Rapport HTML interactif
- `output/analyse_finale.json` : Donnees structurees JSON
