# Prompt pour qualifier les tickets CRC

## Objectif

Analyser et classifier les tickets du centre d'appel contenus dans le fichier JSON du dossier `input/`.

## Structure des dossiers

- `input/` : Fichier JSON source contenant les tickets
- `output/` : Fichiers de sortie (HTML et JSON final)
- `prompt/` : Documentation et instructions d'analyse
- `scripts/` : Scripts Python de traitement
- `temp/` : Fichiers intermediaires (cree automatiquement)

## Scripts disponibles

Deux scripts Python sont disponibles dans le dossier `scripts/` :

1. `preprocess_tickets.py` - Pre-traitement automatique (lit depuis input/)

2. `generate_final_reports.py` - Generation des rapports finaux (ecrit dans output/)


## Structure des donnees

Dans le JSON source (input/) :
- `tickets[]` contient les informations de base des tickets
- `ticketDetails[]` contient les details incluant les commentaires
- Les commentaires sont dans : `ticketDetails->details->ticketComment[].comment`
- Le contractId est dans : `ticketDetails->ticket->details->ticketDetails->subscriptionCode`

URLs generees pour chaque ticket :
- CRM : `https://crm.teamoffre.prod.protectline.fr/main/tickets/edit/{ticketId}`
- Back-office : `https://back-office-fe.teamusages.prod.internal/dashboard?contractId={contractId}`

## Categories proposees

Categories deterministes (automatiques) :
- Sans @Usage : tickets sans mention @Usage dans les commentaires
- Ticket ancien : premiere mention @Usage date de plus de 3 mois

Categories necessitant analyse LLM (basees sur les commentaires) :
- Demande de suppression
- Demande de verification de materiel
- Autres categories a identifier (max 10 categories au total)

## Workflow

### Etape 1 : Pre-traitement
```bash
python scripts/preprocess_tickets.py
```
Cree le dossier `temp/` avec les fichiers intermediaires

### Etape 2 : Analyse manuelle par Claude
Consulter le fichier `prompt/instructions-analyse-tickets.md` pour la methodologie detaillee.


### Etape 3 : Generation des rapports finaux
```bash
python scripts/generate_final_reports.py
```
- Genere le fichier HTML final `output/tickets_classification_final.html`
- Genere le fichier JSON structure `output/analyse_finale.json` contenant:
  - Distribution des themes par ordre decroissant
  - Recommandations strategiques
- Le fichier JSON est integre a la fin du HTML dans une section dediee
- Conserve le dossier `temp/` pour tracabilite




