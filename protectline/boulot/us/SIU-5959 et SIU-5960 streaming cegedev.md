
jdd qa :  
- url front streaming cegedev (firefox) : 
    - https://tus-webrtc-cegedev.qa.protectline.fr/tus-webrtc-cegedev?contractId=GBHCIDTUS076
- url back : 
    - https://tus-webrtc-cegedev.qa.protectline.fr/v1/webrtc-cegedev/streaming-request/GBHCIDTUS076

- contrat GBHCIDTUS076
    - crow : Crow-0013A1259649
    - meari : 	Meari-703A2DA77BBA
    - Sercomm : Sercomm-3C62F01B3FA2	

- cid à ajouter (cf : ) : 
    - 3977 : Arrêt alarme panique
    - 1120 : SOS
    - 1978 : ???
    - 1111 : Detection de fumée
    - 1110 : fumée 

- message pour simuler alarme (topic teamusages.dataEnrichementCrow.alarm.send) : jamais réussi à simuler une alarme, message d'erreur dans le dataenricher 
''' 
com.jsoniter.spi.JsonException: readString: expect string or null, but ￂ, head: 5, peek: {                                                                                               ││ �, 
'''

{  
  "Crow-0013A12596DA_report": [  
    {  
      "_type": "report",  
      "_control_panel": "0013A12596DA",  
      "param1": 0,  
      "param2": 0,  
      "cid": 1120,  
      "panel_time": "2025-07-05T17:04:51.000Z",  
      "dateTimeTB": "2025-07-05T17:04:55.922Z",  
      "uuid": "cf64ca53-63c1-4be2-970d-25a7f9cc8389"  
    }  
  ]  
}

{
  "Crow-0013A1216FFB_report": [
    {
      "_type": "report",
      "_control_panel": "0013A1216FFB",
      "param1": 0,
      "param2": 0,
      "cid": 1110,
      "panel_time": "2025-09-18T14:42:25.139Z",
      "dateTimeTB": "2025-09-18T14:42:25.140Z",
      "uuid": "1367d1ec-6fc8-4a5a-b6a8-e6945070e950"
    }
  ]
}

-> passer directement par la DB

requête sql pour ajouter d'un coup tous les évènements correspondant aux nouveaux cid
INSERT INTO public."event"
(eventid, gatewayid, deviceid, datetimetb, datetimegateway, "source", "type", cid, "label", "location", usr, contractid)
VALUES('8d488e2b-c25f-4adc-8a57-e9366790f5bb-CTS', 'Sercomm-3C62F01B3FA2', 'Sercomm-3C62F01B3FA2', '2025-09-10 11:35:07.000', '2025-09-10 11:35:07.000', 'camera', 'SOS', '1120', 'appearance', 'TNR ', 'null', 'GBHCIDTUS076');
VALUES('9d488e2b-c25f-4adc-8a57-e9366790f5bb-CTS', 'Sercomm-3C62F01B3FA2', 'Sercomm-3C62F01B3FA2', '2025-09-10 11:35:07.000', '2025-09-10 11:35:07.000', 'camera', 'SOS', '1978', 'appearance', 'TNR ', 'null', 'GBHCIDTUS076');
VALUES('1d488e2b-c25f-4adc-8a57-e9366790f5bb-CTS', 'Sercomm-3C62F01B3FA2', 'Sercomm-3C62F01B3FA2', '2025-09-10 11:35:07.000', '2025-09-10 11:35:07.000', 'camera', 'SOS', '1120', 'appearance', 'TNR ', 'null', 'GBHCIDTUS076');
VALUES('2d488e2b-c25f-4adc-8a57-e9366790f5bb-CTS', 'Sercomm-3C62F01B3FA2', 'Sercomm-3C62F01B3FA2', '2025-09-10 11:35:07.000', '2025-09-10 11:35:07.000', 'camera', 'SOS', '1120', 'appearance', 'TNR ', 'null', 'GBHCIDTUS076');
VALUES('3d488e2b-c25f-4adc-8a57-e9366790f5bb-CTS', 'Sercomm-3C62F01B3FA2', 'Sercomm-3C62F01B3FA2', '2025-09-10 11:35:07.000', '2025-09-10 11:35:07.000', 'camera', 'SOS', '1120', 'appearance', 'TNR ', 'null', 'GBHCIDTUS076');