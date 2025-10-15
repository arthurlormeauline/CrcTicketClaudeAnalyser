---
description: Analyse les tickets (arguments $1 : index de l'analyse)
---


## Contexte

Apres execution du script `preprocess_tickets.py`, un fichier `temp/tickets_for_analysis.json` est genere contenant les tickets necessitant une analyse.

## Objectif

**IMPORTANT : Cette analyse doit etre faite MANUELLEMENT par Claude (le LLM), pas par un script automatique.**

L'objectif est d'utiliser la comprehension du langage naturel de Claude pour analyser les tickets et creer un fichier `temp/manual_classifications.json` avec les categories identifiees.

Cette approche remplace l'ancien script automatique base sur des mots-cles pour une analyse plus intelligente et contextuelle.

## Preparation des fichiers pour l'analyse

Etant donne que le fichier tickets_for_analysis.json est trop volumineux pour etre lu en une seule fois par Claude, un script de decoupage est fourni :

```bash
python scripts/split_tickets_for_analysis.py $1
```

Ce script cree plusieurs fichiers dans `temp/batches/` :
- `batch_01_{$1}.json` (15-20 tickets)
- `batch_02_{$1}.json` (15-20 tickets)
- etc.

Claude pourra alors lire et analyser chaque batch manuellement, un par un.

**Claude ne doit PAS recreer un script Python, mais lire et analyser directement les tickets.**

## Methodologie d'analyse

**MODE OPERATOIRE : Claude lit et analyse lui-meme les tickets, sans ecrire de script Python.**

### Preparation : Decoupage des tickets

Executer le script de decoupage :
```bash
python scripts/split_tickets_for_analysis.py $1
```

Cela cree des fichiers batch_01_{$1}.json, batch_02_{$1}.json, etc. dans `temp/batches/` 

### Etape 1 : Extraction des themes depuis les mentions @Usage

Pour CHAQUE fichier batch (batch_01_{$1}.json, batch_02_{$1}.json, etc.), Claude doit :
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

### Etape 4 : Analyse des tickets sans @Usage

Claude doit :
1. Analyser les tickets dans `temp/tickets_without_usage.json`
2. Lire et comprendre tous les commentaires pour identifier des patterns semantiques
3. Creer des sous-categories si possible :
   - "Demande d'information"
   - "Probleme technique non specifie"
   - "Question sur facturation"
   - etc.
4. Si des categories peuvent etre identifiees grace a la comprehension du contexte, les ajouter dans le fichier final

### Etape 5 : Sauvegarde des classifications par batch

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

### Etape 6 : Fusion automatique des resultats

Une fois tous les batches analyses, executer le script de fusion :
```bash
python scripts/merge_batch_classifications.py $1
```
Ce script fusionne automatiquement tous les fichiers batch_XX_classifications_{$1}.json en un seul fichier `temp/manual_classifications_{$1}.json` qui sera utilise par generate_final_reports.py

### Etape 7 : CONSOLIDATION OBLIGATOIRE des categories

**CETTE ETAPE EST OBLIGATOIRE avant de generer le rapport final.**

Claude doit :
1. Executer le script d'analyse des themes :
```bash
python scripts/analyze_themes.py
```
Ce script genere `temp/themes_analysis.json` avec la distribution des themes.

2. LIRE le fichier `temp/themes_analysis.json` pour voir :
   - Le nombre total de themes
   - Le nombre de tickets par theme
   - Les themes avec un seul ticket

3. Si le nombre de themes > 15 OU si plus de 5 themes ont un seul ticket :
   - LIRE le fichier `temp/manual_classifications_{$1}.json`
   - CONSOLIDER les categories en regroupant les themes similaires
   - Respecter les contraintes :
     * Maximum 10-15 categories au total
     * Maximum 5 categories avec un seul ticket
   - ECRASER le fichier `temp/manual_classifications_{$1}.json` avec les categories consolidees
   - RE-EXECUTER `python scripts/analyze_themes.py` pour verifier

4. Exemples de consolidation :
   - Tous les problemes de camera (detection, connexion, live, acces) -> 2-3 categories max
   - Tous les problemes de centrale -> "Probleme centrale"
   - Toutes les demandes equipement -> "Gestion equipement"
   - Tous les problemes notifications -> "Probleme notifications"
   - Tous les problemes GSM/SIM -> "Probleme module GSM/SIM"

5. Continuer la consolidation jusqu'a respecter les contraintes.

## Fichiers generes

- `temp/themes_initiaux.json` (optionnel, pour traçabilite)
- `temp/manual_classifications_{$1}.json` (obligatoire, lu par generate_final_reports.py)

## Notes importantes

**RAPPEL CRUCIAL : NE PAS ECRIRE DE SCRIPT PYTHON**
- Cette analyse est manuelle : Claude lit et comprend les tickets lui-meme
- Ne pas creer de script automatique avec des mots-cles (c'est l'ancienne methode)
- Utiliser la comprehension du langage naturel pour analyser le contexte
- 
- **NE PAS UTILISER D'AGENT pour automatiser l'analyse** - l'analyse doit etre faite directement par Claude dans la conversation principale

**Methode d'analyse :**
- Rester factuel et base sur les commentaires
- Un ticket peut avoir plusieurs categories
- Privilegier la clarte et la coherence des categories
- Les categories doivent etre actionnables pour l'equipe support
- Analyser le contexte complet, pas juste des mots-cles isoles

## Etape 7 : reprendre où tu en étais à l'étape 2 de @prompt/ticket-qualif-prompt
