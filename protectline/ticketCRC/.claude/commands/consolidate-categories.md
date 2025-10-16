---
description: Consolide les categories pour respecter la limite de 10-15 categories (arguments $1 : index de l'analyse)
---

## Objectif

Analyser les classifications generees par `/analyse-tickets` et les reconsolider pour respecter les contraintes :
- **Maximum 10 categories au total**
- **Maximum 5 categories avec un seul ticket dedans**

## Prerequis

La commande `/analyse-tickets` doit avoir ete executee au prealable.

## Methodologie

**IMPORTANT : Cette consolidation doit etre faite MANUELLEMENT par Claude, pas par un script automatique.**

### Etape 1 : Analyse des categories existantes

1. Lire le fichier `temp/manual_classifications_{$1}.json` genere par la fusion des batches
2. Extraire tous les themes uniques avec leur frequence
3. Identifier les themes qui peuvent etre regroupes semantiquement

### Etape 2 : Creation de la liste consolidee

Creer une liste de 10-15 categories GENERIQUES en regroupant les themes similaires.

Exemples de regroupement :
- "Probleme detection camera exterieure", "Probleme detection animaux", "Probleme detection faux positifs", "Detection faux positifs", "Absence detection humaine", "Detection animaux domestiques" -> **"Probleme detection camera"**
- "Probleme connexion camera", "Probleme connexion wifi", "Deconnexion recurrente camera", "Camera disconnection" -> **"Probleme connexion camera"**
- "Probleme acces camera application", "Probleme live camera", "Dysfonctionnement live camera", "Camera - Probleme live", "Dysfonctionnement streaming camera" -> **"Probleme acces video camera"**
- "Probleme module GSM", "Probleme module SIM", "Perte connexion - Carte SIM", "Dysfonctionnement connectivite GSM" -> **"Probleme module GSM/SIM"**
- Toutes les demandes de gestion d'equipement -> **"Gestion equipement"** (suppression, ajout, reintegration, nettoyage)
- Tous les problemes de notifications -> **"Probleme notifications"** (manquantes, defaillantes, erronees)
- Tous les problemes d'application -> **"Probleme application"** (mobile, affichage, synchronisation)

### Etape 3 : Reclassification de tous les tickets

Pour chaque ticket dans `temp/manual_classifications_{$1}.json` :
1. Lire les categories actuelles
2. Les mapper vers les nouvelles categories consolidees
3. Un ticket peut toujours avoir plusieurs categories si pertinent

### Etape 4 : Validation des contraintes

Verifier que :
- Le nombre total de categories est entre 10 et 15
- Maximum 5 categories ont un seul ticket
- Si les contraintes ne sont pas respectees, ajuster les regroupements

### Etape 5 : Sauvegarde du fichier consolide

Sauvegarder le resultat dans `temp/manual_classifications_{$1}.json` (ecrase l'ancien fichier).

Format identique :
```json
{
  "ticket_id": ["Categorie consolidee 1", "Categorie consolidee 2"],
  "autre_ticket_id": ["Categorie consolidee 1"]
}
```

## Notes importantes

- Cette etape est critique pour avoir des rapports exploitables
- Les categories doivent rester ACTIONNABLES pour l'equipe support
- Privilegier des categories larges mais coherentes
- Ne pas hesiter a fusionner agressivement les categories peu frequentes

## Prochaine etape

Une fois la consolidation terminee, executer `/generate-reports {$1}` pour regenerer les rapports finaux avec les categories consolidees.
