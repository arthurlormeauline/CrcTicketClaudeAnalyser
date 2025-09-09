# Analyse des données usages par IA

--> on met tout sur mongo, les données crow. 
Qu'est ce qu'on pourrait faire avec toutes ces données ? 

Utilisation algo qui marche pas trop mal.

Pour l'instant nos data sont pas ouf (par exemple si un champ est bizarre on élimine le contrat, 
on a perdu 40% de nos contrats : problème de date, problème de label, des désactivations/activations qui se 
succèdent).

La donnée vient des "events" --> a refacto, il faut que notre data soit plus clean.

par exemple on peut analyser la dégradation des piles en fonction de plein d'info (région, type 
d'équipement, position du device)

--> le but de tout ça c'est de créer un modèle d'IA pour prédire si une alarme est un faux positif ou non. 

--> besoin de log de device : - pour l'instant 50% du parc est "loggé" parce que log viennent forcément d'action backend (il n'y pas de scan automatique du parc).


