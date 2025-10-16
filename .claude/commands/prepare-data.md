---
description: Prepare les donnees pour l'analyse (arguments $1 : index de l'analyse, --force : extraire tous les tickets)
---

Execute le script de preparation complete des donnees pour l'analyse des tickets.

Ce script regroupe automatiquement :
- Le pre-traitement des tickets (extraction, nettoyage)
- Le decoupage en batches pour l'analyse manuelle

Lance le script Python scripts/analyse/prepare_all.py avec :
- $1 : index d'analyse (par defaut 0)
- --force (optionnel) : extrait tous les tickets, meme ceux deja analyses (avec un champ 'issues' non vide)

Sans --force, seuls les tickets sans analyse ou avec un champ 'issues' vide sont extraits.
