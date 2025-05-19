# Kubernetes Command Line Tools

## Eksctl
**Description:** Outil CLI pour créer et gérer des clusters Amazon EKS (Elastic Kubernetes Service).  
**Utilisation:** Simplifie la gestion des clusters Kubernetes sur AWS.  
**Cas d'utilisation courants:**
- Créer un cluster EKS : `eksctl create cluster`
- Supprimer un cluster EKS : `eksctl delete cluster`
- Ajouter des nœuds à un cluster existant

---

## Kubectl
**Description:** CLI officielle pour interagir avec les clusters Kubernetes.  
**Utilisation:** Gérer les ressources Kubernetes (pods, services, déploiements, etc.).  
**Cas d'utilisation courants:**
- Lister les pods : `kubectl get pods`
- Appliquer un fichier de configuration : `kubectl apply -f deployment.yaml`
- Déboguer un pod : `kubectl logs <pod-name>`

---

## Kubectl-convert
**Description:** Plugin pour convertir des fichiers de configuration Kubernetes entre différentes versions d'API.  
**Utilisation:** Facilite la migration entre versions Kubernetes.  
**Cas d'utilisation courants:**
- Convertir un fichier YAML vers une version plus récente : `kubectl convert -f config.yaml --output-version apps/v1`
- Vérifier la compatibilité des ressources avec une version d'API spécifique

---

## Kubens
**Description:** Outil CLI pour changer rapidement de namespace Kubernetes.  
**Utilisation:** Simplifie la navigation entre namespaces.  
**Cas d'utilisation courants:**
- Changer de namespace : `kubens <namespace>`
- Lister les namespaces disponibles : `kubens`

---

## Kubectx
**Description:** Outil CLI pour changer rapidement de contexte Kubernetes.  
**Utilisation:** Gérer plusieurs clusters Kubernetes.  
**Cas d'utilisation courants:**
- Changer de contexte : `kubectx <context>`
- Lister les contextes disponibles : `kubectx`

---

## Kubelet
**Description:** Composant Kubernetes qui s'exécute sur chaque nœud et gère les pods.  
**Utilisation:** Assure que les conteneurs sont en cours d'exécution sur un nœud.  
**Cas d'utilisation courants:**
- Surveiller l'état des pods sur un nœud
- Gérer les configurations locales des nœuds

---

## Fzf
**Description:** Outil CLI interactif pour la recherche fuzzy dans le terminal.  
**Utilisation:** Recherche rapide dans des fichiers, commandes ou listes.  
**Cas d'utilisation courants:**
- Rechercher une commande dans l'historique : `history | fzf`
- Naviguer dans un répertoire : `ls | fzf`

---

## Flux
**Description:** Outil GitOps pour déployer des applications sur Kubernetes à partir de dépôts Git.  
**Utilisation:** Automatisation des déploiements Kubernetes via Git.  
**Cas d'utilisation courants:**
- Synchroniser un cluster avec un dépôt Git
- Déployer des mises à jour automatiquement après un commit

---

## Fluxctl
**Description:** CLI pour interagir avec Flux.  
**Utilisation:** Gérer et déboguer les déploiements Flux.  
**Cas d'utilisation courants:**
- Forcer une synchronisation : `fluxctl sync`
- Lister les workloads gérés par Flux : `fluxctl list-workloads`

---

## Stern
**Description:** Outil CLI pour suivre les logs de plusieurs pods Kubernetes en temps réel.  
**Utilisation:** Déboguer des applications distribuées.  
**Cas d'utilisation courants:**
- Suivre les logs d'un déploiement : `stern <deployment-name>`
- Filtrer les logs par conteneur ou namespace

---

## Helm
**Description:** Gestionnaire de packages pour Kubernetes.  
**Utilisation:** Installer, mettre à jour et gérer des applications Kubernetes via des charts.  
**Cas d'utilisation courants:**
- Installer une application : `helm install <release-name> <chart>`
- Mettre à jour une application : `helm upgrade <release-name> <chart>`
- Supprimer une application : `helm uninstall <release-name>`

---

## Krew
**Description:** Gestionnaire de plugins pour kubectl.  
**Utilisation:** Installer et gérer des extensions pour kubectl.  
**Cas d'utilisation courants:**
- Installer un plugin : `kubectl krew install <plugin-name>`
- Lister les plugins installés : `kubectl krew list`

---

## Kubeseal
**Description:** Outil pour chiffrer des secrets Kubernetes à l'aide de SealedSecrets.  
**Utilisation:** Sécuriser les secrets dans des dépôts Git.  
**Cas d'utilisation courants:**
- Chiffrer un secret : `kubeseal < secret.yaml > sealedsecret.yaml`
- Déployer un SealedSecret dans un cluster

---

## Jq
**Description:** Outil CLI pour manipuler et interroger des données JSON.  
**Utilisation:** Extraire et transformer des données JSON.  
**Cas d'utilisation courants:**
- Filtrer une clé JSON : `cat file.json | jq '.key'`
- Formater un JSON : `cat file.json | jq`

---

## Yq
**Description:** Outil CLI pour manipuler et interroger des données YAML.  
**Utilisation:** Similaire à jq, mais pour YAML.  
**Cas d'utilisation courants:**
- Modifier une clé YAML : `yq e '.key = "value"' file.yaml`
- Convertir YAML en JSON : `yq e -j file.yaml`