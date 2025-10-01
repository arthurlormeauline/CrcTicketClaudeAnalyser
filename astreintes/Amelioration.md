# Amélioration astreinte

## Etat des lieux

- Peut on avoir un historique des derniers incidents, et notamment par tranches horraires 
et par gravité ?
    - y a t il un système de monitoring et/ou de persistence des incidents ?
- Quelles sont les aspects les plus douloureux des astreintes 
- Où est la doc, est elle complète ?

--> Message teams envoyé : attente de réponse de Julien, Chris et Emna

## Formation cloudwatch par Julien


## Les outils 

- Editer la liste des outils nécessaires au débuggage lors de la gestion d'incident. 
- peut on automatiser : 
    - savoir si tout mes outils sont là et fonctionne (par exemple un script pourrait checker si tout est bien installer sur le système).
- Une doc clair par outils, pour diagnostiquer la santé de l'outils, la gestion de la vie de l'outil (installation, désinstallation, upgrage)

- accès k8s prod
- accès aws prod
- accès v1


## Les processes

- Une doc clair pour chaque type d'incident sur la marche à suivre. 

- Un processus clair pour qualifier les incidents en fonction du niveau de graviter (comment je peux savoir une ou deux minutes max le niveau de gravité).

- Un processus clair pour savoir, sur chaque type d'incident, si mes actions se concrétise par une amélioration du système (monitoring du système)

- Un processus clair pour savoir quand "escalader" l'incident.



## Retours d'expérience

- Un processus clair pour rendre compte à chaque incident de :
    - cause de l'incident
    - ce qui a été engagé : 
        - par exemple si je redémmare un pod, comment persister cet évènnement ?
    - le résultat (pour chaque action noté si cela a été bénéfique et/ou si cela a régler l'incident).
    - ce qui aurait pu être mieux, si on a besoin de modifier des choses (update des robots, dev, nouveau dashboard etc.)