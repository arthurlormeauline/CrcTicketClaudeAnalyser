# Sujet d'amélioration continue : MEP sans douleur

Objectif : CICD  ***continuous delivery - continuous integration***

## Etudier l'éxistant

Milestone : pouvoir faire des mise en QA et des MEP (étudier l'existant pour pouvoir proposer axes d'amélioration).

Voir tout ce qui est manuel et essayer de trouver des alternatives automatisées. 

## Mettre en place un poc

Mettre en place une application pour tester de nouvelles façon de faire : workflow github, flux etc.
La déployer en dev et en qa

## Techno à voir

Aumatisation de camunda ?

- voir avec Julien il y a déjà un repos qui existe avec déploiement automatique

Flux : comment on déploie réellement en dev et en qa

## Questions

### Flux

- Sur le projet flux, master correspond à dev ? (dans l'image du container ex : image: 549364733497.dkr.ecr.eu-west-3.amazonaws.com/device:develop-9ef8c2e473b6e5c283baf0cf6c9014a5b7efe59b)
- Tous les déploiements sont redéfinis dans flux patch, pourquoi ?