# Us en cours

SIU-6139 EventFe  ajout traçabilité

exemple appel traçabilité :

curl -X GET "https://event.dev.protectline.fr/v1/tracability?deviceId=Crow-0013A12596DA_0_0&limit=200" -H "accept: */*"

{
"uuid": "b7bffa44-a5ab-4674-bc25-cf6c972f2d00",
"deviceId": "Crow-0013A12596DA_0_0",
"reportDate": "2025-10-26 04:09:13.441",
"saveHistoryDate": "2025-10-17 06:20:11.171",
"sendTelesurveilleurDate": null,
"source": "smoke",
"type": "Alerte intrusion",
"notificationType": null,
"expectedMonitoringStation": "false",
"expectedNotification": "false",
"notificationDate": null,
"contractStatus": "",
"additionalInfos": null
}


