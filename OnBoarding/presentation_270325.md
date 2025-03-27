# Présentation

## Principale

- **Modules de réception** : point d'entrée, communique avec le matériel hardware chez les gens
  - **Mediator** : Crow et Sercom
  - **Reporter** : Crow et Sercom

  Chaque équipement a un **Mediator** et un **Reporter** :
  - **Mediator** : expose des API pour pouvoir communiquer avec (maintien de connexion, souvent propriétaire, WebSocket, etc.)
  - **Reporter** : permet au matériel de nous parler (protocole propriétaire, pour Sercom c'est du HTTP) : test de vie (heartbeat), alarme, etc.

- Les reporters postent dans des **queues Kafka** (service managé sur AWS : MSK).

- Chaque matériel a son format de communication →  
  - **Data Enricher** : récupère les queues Kafka des reporters et publie un événement identique pour tous (messages normalisés).  
    → Data Enricher republie dans une queue Kafka.

- **TB Kafka** : connecte Kafka à ThingsBoard.

- **ThingsBoard** : supporte le modèle de données ; persistance (BDD Postgres, RDS sur AWS) ; gère des objets et des règles :
  - **TB Node**
  - **TB UI**
  - **TB : JS exécuter**
  - **Zookeeper**

  **Concepts principaux** :
  - **Clients** : actifs = contrat
  - **Dispositif** : device
  - **Device Profile** : gère les profils des devices
  - **Chaînes de règle (Rule Chain)** : no/low code permettant de gérer du métier (aiguillage et métier)
  - **3 gros objets** : event, image et video

- **Microservices Business** : couche d'abstraction pour adapter les API ThingsBoard au format Protectline :
  - **Event**
  - **Télésurveillance**
  - **Notification**
  - **Device**
  - **Installation**

- **Camunda (BPM - Business Process Management)** :  
  Owné par toutes les équipes, gère tous les processus métiers (appels, SMS, appel Cegedev).

- **Streaming** : peer-to-peer, WebRTC (très complexe) ; 2 infrastructures :
  - Une pour **Meari** (solution clés en main).
  - Une pour **Sercom** (made in Protectline).

## Autre

- **Device Management** : campagne de mise à jour avec notion de planification (par exemple, mise à jour entre 2h et 3h).  
  4 microservices avec modèle persisté en base :
  - **API**
  - **UI** (Angular)
  - **Orchestrator**
  - **Traitement**

- **Scène** : gère des règles IoT maison connectée par client, personnalisable (ThingsBoard ne fait que du global).
  - Utilise **Gladys** (forké).

- **Smartplug** : géré par **TBMQTT** (fonctionne comme Mediator et Reporter).  
  TBMQTT fonctionne comme Reporter pour Smartplug et Meari.  
  Meari a son propre Mediator.