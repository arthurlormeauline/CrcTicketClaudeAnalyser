---
description: Analyse manuelle des tickets par Claude (arguments $1 : index de l'analyse)
---

## Objectif

**IMPORTANT : Cette analyse doit etre faite MANUELLEMENT par Claude (le LLM), pas par un script automatique.**

Utiliser la comprehension du langage naturel pour analyser les tickets et creer les classifications dans `temp/batches/batch_XX_classifications_{$1}.json`.

## Prerequis

La commande /prepare-data doit avoir ete executee au prealable pour generer les fichiers batch dans `temp/batches/`.

## Methodologie d'analyse

**MODE OPERATOIRE : Claude lit et analyse lui-meme les tickets, sans ecrire de script Python.**

**IMPERATIF : Claude doit traiter TOUS les batches jusqu'au bout sans s'arreter. L'analyse doit etre complete avant de demander confirmation a l'utilisateur.**


### Etape 1 : Extraction des themes depuis les mentions @Usage


Pour CHAQUE fichier batch (batch_01_{$1}.json, batch_02_{$1}.json, etc.), Claude doit **EN UTILISANT UN AGENT TASK**
1. LIRE le fichier batch complet avec l'outil Read
2. Pour chaque ticket dans le batch :
   a. Lire les mentions @Usage presentes dans usage_mentions
   b. Comprendre le CONTEXTE de chaque phrase contenant @Usage
   c. En deduire un ou plusieurs themes bases sur la COMPREHENSION SEMANTIQUE (pas des mots-cles)
   d. IMPORTANT : Utiliser des categories GENERIQUES des le depart pour eviter trop de fragmentation
      - Preferer "Probleme camera" plutot que "Probleme camera exterieure nuit"
      - Preferer "Probleme connexion" plutot que "Probleme connexion wifi camera interieure"
   e. Noter le ticket_id et les themes identifies
3. Passer au batch suivant

Important : Claude NE DOIT PAS ecrire de script Python pour cette etape. Il doit lire et analyser avec sa comprehension du langage naturel.
**Important** : Claude doit traiter batch par batch. Pas besoin de lire tout les batch avant d'analyser le premier, l'analyse d'un batch peut se faire en ne chargeant que le batch courant dans le context.
**C'est pour ça que Claude doit utiliser un agent, pour avoir son contexte clair uniquement dédié à l'analyse du batch**


### Etape 2 : Regroupement et consolidation des themes

Claude doit IMPERATIVEMENT :
1. Analyser tous les themes extraits a l'etape 1
2. Identifier les themes similaires qui peuvent etre regroupes grace a la comprehension semantique
3. Creer une liste de categories finales avec les CONTRAINTES suivantes :
   - **Maximum 10-15 categories au total**
   - **Maximum 5 categories avec un seul ticket dedans**
   - Les categories doivent etre GENERIQUES et ACTIONNABLES
4. Exemples de regroupement :
   - "Probleme detection camera exterieure", "Probleme detection animaux", "Probleme detection faux positifs" -> "Probleme detection camera"
   - "Probleme connexion camera", "Probleme connexion wifi", "Probleme deconnexions" -> "Probleme connexion"
   - "Probleme acces camera application", "Probleme live camera", "Probleme consultation videos" -> "Probleme acces video camera"
   - "Probleme module GSM", "Probleme module SIM", "Probleme carte SIM" -> "Probleme module GSM/SIM"
   - Toutes les demandes de gestion d'equipement -> "Gestion equipement" (suppression, ajout, reintegration)
   - Tous les problemes de notifications -> "Probleme notifications"

### Etape 3 : Validation par analyse complete

Claude doit :
1. Pour chaque ticket, relire TOUS les commentaires (pas seulement ceux avec @Usage)
2. Verifier que la categorie attribuee est coherente avec l'ensemble des echanges
3. Utiliser la comprehension du contexte pour ajuster si necessaire
4. Un ticket peut avoir plusieurs categories si pertinent

### Etape 4 : Sauvegarde des classifications par batch

Pour CHAQUE batch analyse, Claude doit sauvegarder ses classifications dans un fichier JSON :
- `temp/batches/batch_01_classifications_{$1}.json`
- `temp/batches/batch_02_classifications_{$1}.json`
- etc.

Format de chaque fichier :
```json
{
  "ticket_id": ["Categorie 1", "Categorie 2"],
  "autre_ticket_id": ["Categorie 1"]
}
```

## Notes importantes

**RAPPEL CRUCIAL : NE PAS ECRIRE DE SCRIPT PYTHON**
- Cette analyse est manuelle : Claude lit et comprend les tickets lui-meme
- Ne pas creer de script automatique avec des mots-cles (c'est l'ancienne methode)
- Utiliser la comprehension du langage naturel pour analyser le contexte
- **NE PAS UTILISER D'AGENT pour automatiser l'analyse** - l'analyse doit etre faite directement par Claude dans la conversation principale

**Methode d'analyse :**
- Rester factuel et base sur les commentaires
- Un ticket peut avoir plusieurs categories
- Privilegier la clarte et la coherence des categories
- Les categories doivent etre actionnables pour l'equipe support
- Analyser le contexte complet, pas juste des mots-cles isoles

## Prochaine etape

Une fois tous les batches analyses et sauvegardes, executer la commande /generate-reports pour fusionner les classifications et generer les rapports finaux.
