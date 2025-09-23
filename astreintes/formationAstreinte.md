# Formation astreinte

## v1

pour la V1  : sitv1prod sur aws, directement les instances ec2 (pas de k8)

on gère tout ce qui est aws rpg, gprs (le reste c'est offre etc.)

Dans la plupart des cas, des alarmes bloquées --> relancer la machine sur aws

peip : serveur de réception d'alarme

## V2

alarme cloudwatch 

-> maintenance msk : ça fouare mais c'est moins grave / faut juste attendre la fin de la maintenance, puis redémarrer le datajs (une fois par mois, les mardi soir vers 21h)
kubectl rollout restart deploy dataenricher-js 

après re démarrage de data js on regarde les topics : 
- teamusages.dataEnrichementCrow.heartbeat.save
- teamusages.dataEnrichement.heartbeatSercomm.send
si c'est dans les choux, on empty topic et on redémarre data js encore une  fois


### gateway dec

vie d'une alarme :

- gateway
- reporter crow
- kafka (topic crow alarm)  
- dataenricher
- kafka (topic output)
- ThingsBoard (via connecteur kafka transport) : BD
  - rule chain
    - event
    - telesurveillance
    - process camunda (intrusion/flood/smoke)

vie d'un heartbeat :

- gateway
- reporter crow
- kafka (topic data js)  
- datajs
- ThingsBoard : BD

si y a plus d'activité, "last activity" passe à false dans la bdd de tb

Il y a une api deviceManagement qui intérroge tb, pour compter le nombre de lastactivity à false

- un robot canary aws intérroge DeviceManagement et c'est celui qui déclenche le KO plus astreinte 

## robot alarm, flood, smoke (sur cloud watch)

génère des alarmes, flood, smoke toutes les 5 minutes et opère des vérifications

Les robots utiles "crow simulator" : micro service qui génère des alarmes crow

attaque directement

- kafka (topic crow alarm)

on peut checker toutes la chaîne (voir plus haut)
plus : checker event, telesurveillance, puis camunda

sur camunda : si offre est ko, ça pète tout (c'est une des première api qui appelé dans les process camunda)

c'est offre qui gère camunda

## cas récurents

- maintenance msk
- coupure cegedev
- free memory : souvent c'est "signaling" un service qu'il faut restart parce qu'il consome trop de mémoire
- qr code : caméra en pls (ou plus de batterie)
- free storage : médiator crow (souvent), bug connu, il dump de la mémoire
et il faut nétoyer de temps en temps (si ça arrive vendredi soir, on peut attendre lundi matin)
- lag sur les push : lié au distributeur (il faut les contacter, mail, teams)

si ça fouare sur loki, prometheus, aloi : osef, ça collecte juste des logs pour la système team, au pire
on essaye de redémmarer.
