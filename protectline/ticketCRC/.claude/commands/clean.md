---
description: Nettoie tous les fichiers temporaires et de sortie
---

Execute le script de nettoyage qui supprime tous les fichiers dans :
- `temp/` (fichiers temporaires)
- `temp/batches/` (fichiers de batches)
- `output/` (rapports generes)

Cette commande est utile pour repartir de zero avant de lancer une nouvelle analyse complete.

**ATTENTION : Cette action est irreversible. Tous les fichiers seront definitivement supprimes.**

Lance le script Python `scripts/clean.py`.

## Utilisation

Utilise cette commande avant de relancer le workflow complet `/ticket` pour s'assurer qu'aucun fichier obsolete n'interfere avec la nouvelle analyse.
