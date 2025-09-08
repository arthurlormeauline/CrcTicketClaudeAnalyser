SIU-5700 : visionnage clip Sercomm


en base de donnée les event qui correspondent à des clips à visionner on le champ 
{ "type" : "clip" | "clip négatif" }

les eventId (depuis un dev récent) se terminent aussi par "-clip"
### data de test clip Sercomm : 
"clipid","uri","duration","size","eventid","datetimegateway","rank","iapeople"
"8e845ee9-5f0a-38c9-ac3b-5d74ce52ea85",
Sercomm/20250509/3C62F01B0FAE_people_5_10_20250509073525+0000_0.mp4,
15,
655599,
bf18a678-bf18-4a67-8bf1-8a678bf18a67,
2025-05-09 09:35:25.000 +0200,
0,

### Curl pour récupérer le clip auprès de Event
curl -X GET "https://event.dev.protectline.fr/v1/storage/bf18a678-bf18-4a67-8bf1-8a678bf18a67?uri=Sercomm%2F20250509%2F3C62F01B0FAE_people_5_10_20250509073525%2B0000_0.mp4" -H "accept: */*" -H "Authorization: token"


### URL de test
http://localhost:2003/main/customers/details/contracts/equipments/events/GBHCIDTUS000