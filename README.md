# Description

Cet outils permet d'analyser un fichier backup json fournis par l'application "usages-tickets" en utilisant claude qualifier les tickets en fonciton de problème/thème.

## Utilisation

Placer le json dans input/ puis ouvrir claude dans un terminal et lancer la commande slash "/ticket"
Normalement tout devrait être automatique et n'a pas besoin d'intervention humaine, mais comme on utilise claude, il faut quand même rester pas loin pour éventuellement lui ajouter des droits ou lui demander de continuer
s'il s'arrête sans raison.

À la fin le rapport est dans "output/" sous forme de page html à ouvrir dans un navigateur
