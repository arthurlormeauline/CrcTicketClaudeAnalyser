# Notes

## Glossaire

        - Gateway :  materiel qui parle à notre si (boitier centrale crow par exemple)
        - Sengrid (envoie de mail), Twilio (brocker de notification), OBS (sms conversationel)
        - apk (mobile) : extension des appli mobile
        - hw, fw, sw : hardware firmware software
        - MQTT : technologie de queue un comme kafka ; voir aussi TBMQTT -> outil fournis par thingsboard, type transport
        permet de parler à la smartplug
        - RFP camera, RFP Tap : demande de nouveau materiel (appel offre)
        - APN (lié au paramétrage sim) : configuration pour communiquer en data (url login mdp)
        - niveau RSSI : niveau radio, niveau wifi
        - TB (exemple : https://protectline.atlassian.net/wiki/spaces/STU/pages/1674215425/Hebdo+RUN) : ThingsBoard
        - ws : web socket
        - mode de délégation temporaire (mvp tsb v2) : process quasi legacy. on envoie direct à cegedev, commercialement c'est dead

## Qu'est ce qu'on doit dev (principalement) + lien github ?

- Mediator crow : ext
- reporter crow : ext

- Mediator Sercomm : **gh à venir**
- Reporter Sercomm : **gh à venir**

- Mediator Meari : **gh à venir**

- data enricher : https://github.com/protectline/DataEnricher
- data enricher crow ???????? : https://github.com/protectline/dataenricher-crow

- Tb kafka : **gh à venir**

- Device Management :https://github.com/protectline/DeviceManagement 
- Device Management data transport : https://github.com/protectline/devicemanagement-data-transport
- Device Management orchestrator : https://github.com/protectline/devicemanagement-orchestrator
- Device Management UI (FE) : https://github.com/protectline/devicemanagement-fe (intégré au CRM, ou en direct onglet "parc")

- Device Management api : **gh à venir**
- Deviec Management ordre : **gh à venir**
- Device Management traitement : **gh à venir**

- Event service : https://github.com/protectline/event (event fe ???????? : https://github.com/protectline/event-fe)
- Télésurveillance service : https://github.com/protectline/telesurveillance
- Notification service : https://github.com/protectline/notifications
- Device service : https://github.com/protectline/device
- Installation service : https://github.com/protectline/installation
- Scene : https://github.com/protectline/scene
- Signalisation (pour le streaming) : https://github.com/protectline/signalingServer

## Techo à voir

- kafka
- flux,  gitops, gitlab
- camunda
- zookeeper : gestion des pods de kafka

## Testing

Compte en QA avec données event (à chercher dans le crm):  GBHCIDTUS0102

## cycle de vie US

- chris analyse
- grooming
- ready for dev
- en cours (attribué)
- ready for review (PR)
- review par Emna, ou Julien
- on merge en dev
- test en dev (critère acceptance)
- un autre dev fait les même test sur dev
- ready for release
- release fait par Julien
- QA par Loic
- MEP : mise en prod par Julien

une branche par feature
