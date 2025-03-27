# A voir

## Glossaire

termes à préciser :  
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

## Brique fonctionel encore floue

        - mode de délégation temporaire (mvp tsb v2) : on envoie direct à cegedev, commercialement c'est ded

## Qu'est ce qu'on doit dev (principalement) + lien github ?

        - Thingsboard ?
        - installation
        - site
        - device
        - notification
        - event
        - télésurveillance
        - contracts
        - connecteurs ? lesquels :

## Observabilité

        - où sont les logs ? grafana, cloudwatch gère les alertes

## Outils annexes

        - Quels sont les outils annexes : jira (board), confluence crm ; y en a t il d'autre ?

## Testing

        - Puis faire moi même des test end to end ?

## Techo à voir

        - kafka
        - flux gitops
        - camunda
        - zookeeper : gestion des pods de kafka

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