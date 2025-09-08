
Définition de la version
- pour chaque service / process camunda / rule chain / consule : on définie une version et les tickets associés à tester

## Camunda

On télécharge la version de dev, et pour chaque bloque on modifie la version.
On upload la nouvelle version via API.
Ce process peut être automatisé, car le bpmn peut être modifié directement via script (le bpmn est un xml --> il suffit de trouver où la version est définie pour pouvoir la modifier sans passer par la IHM)

## Thingsboard rule chains

Pas de solution pour l'instant. Les changements dans les rule chains se font manuellement pour chaque environnement.

## Consul


## Code

