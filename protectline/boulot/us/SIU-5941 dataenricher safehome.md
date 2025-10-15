SIU-5941 : DataEnricher Safehome

input de test :
contractId : OSDEVICE3TNR
gateway : Safehome-235711131719TNR 

topic d'entrée : teamusages.dataEnrichementSafehome.alarm.send


## CONTRAT ACTIVE : 
### 1. activation :

{
"metadata": {
"messageId": "123456789",
"callerId": "tus.callerId",
"messageType": "messageType",
"deviceName": "Safehome-235711131719TNR"
},
"dateTimeDevice" : "2025-10-14 00:07:55.000 +0200" ,
"dateTimeIOTGateway" : "2025-10-14 00:07:55.000 +0200" ,
"cid" : "app-arm-rfid",
"user" : "Celine",
"source" : "Safehome-001399AAAAADTNR_R_5549463",
"uuid": "2be8abcf-e493-4af1-816b-4a5d6bd134d5k"
}

#### a. sendTelemetry : 
{
"cid" : "app-arm-rfid",
"dateTimeTB" : "",
"dateTimeGateway" : "2025-10-14 00:07:55.000 +0200",
"eventID" : "2be8abcf-e493-4af1-816b-4a5d6bd134d5k",
"label" : "appearance",
"deviceId" : "Safehome-001399AAAAADTNR_R_5549463",
"location" : "default",
"type" : "Activation par badge",
"gatewayId" : "Safehome-235711131719TNR",
"user" : "Celine",
"token" : "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJubE44VC13bDJCekRxNFZuZzY0U3lOUjdNYVFYUXBmR3dISS1jSjRCVFFnIn0.eyJleHAiOjE3NTkzNjc0ODEsImlhdCI6MTc1OTMzMTQ4MSwianRpIjoiYzMzZTY4ODktOTMzYy00MTUwLWI1OGYtYTEwN2IxOTA1YWVjIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay0yMS5kZXYucHJvdGVjdGxpbmUuZnIvcmVhbG1zL1Byb3RlY3RsaW5lIiwiYXVkIjpbImNhbXVuZGEtaWRlbnRpdHktc2VydmljZSIsInVzYWdlLXNpZ25hbGluZy1zZXJ2ZXIiLCJ1c2FnZS1nbGFkeXMiLCJhY2NvdW50Il0sInN1YiI6IjhiOTU0NjIwLTk3MWItNDk3MC1hZjVjLTlkNjI5ZTk3NWZkYyIsInR5cCI6IkJlYXJlciIsImF6cCI6InVzYWdlLWRhdGFlbnJpY2hlciIsInNlc3Npb25fc3RhdGUiOiI3YTVmZDAzNC05YWM1LTQzNTctOWY0Mi0xZGJlOGQwZmFhNzUiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJVQUQiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InVzYWdlLXNpZ25hbGluZy1zZXJ2ZXIiOnsicm9sZXMiOlsidW1hX3Byb3RlY3Rpb24iXX0sInVzYWdlLWdsYWR5cyI6eyJyb2xlcyI6WyJhZG1pbi1nbGFkeXMiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGNhbXVuZGEtcmVzdC1hcGkgdGJfY2xpZW50IGVtYWlsIHByb2ZpbGUiLCJzaWQiOiI3YTVmZDAzNC05YWM1LTQzNTctOWY0Mi0xZGJlOGQwZmFhNzUiLCJmaXJzdE5hbWUiOiJ0ZW5hbnQtcHJvdGVjdGxpbmVAcHJvdGVjdGxpbmUuZnIiLCJsYXN0TmFtZSI6InRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoidGVuYW50LXByb3RlY3RsaW5lQHByb3RlY3RsaW5lLmZyIHRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJ0ZW5hbnRJZCI6IjEyNmE5ZDYwLWRiMTMtMTFlYS04NTI4LWYzOGFlNmFjM2VlNyIsInNjb3BlcyI6IlRFTkFOVF9BRE1JTiIsInByZWZlcnJlZF91c2VybmFtZSI6InRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsImdpdmVuX25hbWUiOiJ0ZW5hbnQtcHJvdGVjdGxpbmVAcHJvdGVjdGxpbmUuZnIiLCJmYW1pbHlfbmFtZSI6InRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsInVzZXJJZCI6IjE5YjYyMzUwLWRiMTMtMTFlYS05NTIyLWM5YTIzMjI2MDY2MyIsImVtYWlsIjoidGVuYW50LXByb3RlY3RsaW5lQHByb3RlY3RsaW5lLmZyIn0.SG89_RIfbYdGOz1_4tZgAgPmaZ0LX4KI9-o5cyd0MWVmzWlTFQJFjQdO9w_r7P6SJKElnaA4QSuM8pYPPvExiRaeDyE9iIZUkhzoEG45mLUC9iFJ3SO_m5As9B-TOZgB1YqT8DErTCCswNhzeAuEBkbzQW93n3kqzTWDOubVuaPC-wnpY2ZNDzINqLrA_LOMcAOVS5RGj1nl-HcnYH2-FNC-SY0-O1XniOeIy8Ju6keG7vySMAl2dkFoPM6xT42lPGVG-PrXIXERZKIhDOJMYx-8p7f2NtUUi_bUrpTvoclIEOqYvRVAYkZ-tNmEo94XLNg59E1XiiR7DTtWTLENBw",
"refreshToken" : "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJiYzNiNGNiNS1kZGUxLTQwMTEtOGI2Yi0wOWEzMmMxMmVjZWEifQ.eyJleHAiOjE3NTkzNDU4ODEsImlhdCI6MTc1OTMzMTQ4MSwianRpIjoiYjE3MzhhODYtMmFiNy00MWMyLWFlZjQtOTc3NmE5NGNlYjU2IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay0yMS5kZXYucHJvdGVjdGxpbmUuZnIvcmVhbG1zL1Byb3RlY3RsaW5lIiwiYXVkIjoiaHR0cHM6Ly9rZXljbG9hay0yMS5kZXYucHJvdGVjdGxpbmUuZnIvcmVhbG1zL1Byb3RlY3RsaW5lIiwic3ViIjoiOGI5NTQ2MjAtOTcxYi00OTcwLWFmNWMtOWQ2MjllOTc1ZmRjIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6InVzYWdlLWRhdGFlbnJpY2hlciIsInNlc3Npb25fc3RhdGUiOiI3YTVmZDAzNC05YWM1LTQzNTctOWY0Mi0xZGJlOGQwZmFhNzUiLCJzY29wZSI6Im9wZW5pZCBjYW11bmRhLXJlc3QtYXBpIHRiX2NsaWVudCBlbWFpbCBwcm9maWxlIiwic2lkIjoiN2E1ZmQwMzQtOWFjNS00MzU3LTlmNDItMWRiZThkMGZhYTc1In0.HTWXz20aT89D1WeCuMIG7ycJWKv7NLopk5dfQA5UH3A",
"contractId" : "OSDEVICE3TNR",
"locationDetail" : "Ma super location"
}

##### b. Traceability : 
Rien -> le cid ne fait pas partis des cid qui doivent déclencher la traçabilité


########################
### 2. alarm intrusion :

{
"dateTimeDevice" : "2025-10-14 00:07:55.000 +0200",
"dateTimeIOTGateway" : "2025-10-14 00:07:55.000 +0200",
"cid" : "app-alarm-matter",
"user" : "Celine",
"source" : "Safehome-001399AAAAADTNR_3000116",
"uuid" : "35a474ba-f99a-4d7d-81a7-505f4eb28c80"
}


##### a. sendTelemetry :

{
"cid" : "app-alarm-matter",
"dateTimeTB" : "",
"dateTimeGateway" : "2025-10-14 00:0:55.000 +0200",
"eventID" : "35a474ba-f99a-4d7d-81a7-505f4eb28c80",
"label" : "appearance",
"deviceId" : "Safehome-001399AAAAADTNR_3000116",
"location" : "pir",
"source" : "doshock",
"type" : "Alerte intrusion",
"gatewayId" : "Safehome-235711131719TNR",
"user" : "Celine",
"token" : "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJubE44VC13bDJCekRxNFZuZzY0U3lOUjdNYVFYUXBmR3dISS1jSjRCVFFnIn0.eyJleHAiOjE3NTkzNjc0ODEsImlhdCI6MTc1OTMzMTQ4MSwianRpIjoiYzMzZTY4ODktOTMzYy00MTUwLWI1OGYtYTEwN2IxOTA1YWVjIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay0yMS5kZXYucHJvdGVjdGxpbmUuZnIvcmVhbG1zL1Byb3RlY3RsaW5lIiwiYXVkIjpbImNhbXVuZGEtaWRlbnRpdHktc2VydmljZSIsInVzYWdlLXNpZ25hbGluZy1zZXJ2ZXIiLCJ1c2FnZS1nbGFkeXMiLCJhY2NvdW50Il0sInN1YiI6IjhiOTU0NjIwLTk3MWItNDk3MC1hZjVjLTlkNjI5ZTk3NWZkYyIsInR5cCI6IkJlYXJlciIsImF6cCI6InVzYWdlLWRhdGFlbnJpY2hlciIsInNlc3Npb25fc3RhdGUiOiI3YTVmZDAzNC05YWM1LTQzNTctOWY0Mi0xZGJlOGQwZmFhNzUiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJVQUQiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InVzYWdlLXNpZ25hbGluZy1zZXJ2ZXIiOnsicm9sZXMiOlsidW1hX3Byb3RlY3Rpb24iXX0sInVzYWdlLWdsYWR5cyI6eyJyb2xlcyI6WyJhZG1pbi1nbGFkeXMiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGNhbXVuZGEtcmVzdC1hcGkgdGJfY2xpZW50IGVtYWlsIHByb2ZpbGUiLCJzaWQiOiI3YTVmZDAzNC05YWM1LTQzNTctOWY0Mi0xZGJlOGQwZmFhNzUiLCJmaXJzdE5hbWUiOiJ0ZW5hbnQtcHJvdGVjdGxpbmVAcHJvdGVjdGxpbmUuZnIiLCJsYXN0TmFtZSI6InRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoidGVuYW50LXByb3RlY3RsaW5lQHByb3RlY3RsaW5lLmZyIHRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJ0ZW5hbnRJZCI6IjEyNmE5ZDYwLWRiMTMtMTFlYS04NTI4LWYzOGFlNmFjM2VlNyIsInNjb3BlcyI6IlRFTkFOVF9BRE1JTiIsInByZWZlcnJlZF91c2VybmFtZSI6InRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsImdpdmVuX25hbWUiOiJ0ZW5hbnQtcHJvdGVjdGxpbmVAcHJvdGVjdGxpbmUuZnIiLCJmYW1pbHlfbmFtZSI6InRlbmFudC1wcm90ZWN0bGluZUBwcm90ZWN0bGluZS5mciIsInVzZXJJZCI6IjE5YjYyMzUwLWRiMTMtMTFlYS05NTIyLWM5YTIzMjI2MDY2MyIsImVtYWlsIjoidGVuYW50LXByb3RlY3RsaW5lQHByb3RlY3RsaW5lLmZyIn0.SG89_RIfbYdGOz1_4tZgAgPmaZ0LX4KI9-o5cyd0MWVmzWlTFQJFjQdO9w_r7P6SJKElnaA4QSuM8pYPPvExiRaeDyE9iIZUkhzoEG45mLUC9iFJ3SO_m5As9B-TOZgB1YqT8DErTCCswNhzeAuEBkbzQW93n3kqzTWDOubVuaPC-wnpY2ZNDzINqLrA_LOMcAOVS5RGj1nl-HcnYH2-FNC-SY0-O1XniOeIy8Ju6keG7vySMAl2dkFoPM6xT42lPGVG-PrXIXERZKIhDOJMYx-8p7f2NtUUi_bUrpTvoclIEOqYvRVAYkZ-tNmEo94XLNg59E1XiiR7DTtWTLENBw",
"refreshToken" : "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJiYzNiNGNiNS1kZGUxLTQwMTEtOGI2Yi0wOWEzMmMxMmVjZWEifQ.eyJleHAiOjE3NTkzNDU4ODEsImlhdCI6MTc1OTMzMTQ4MSwianRpIjoiYjE3MzhhODYtMmFiNy00MWMyLWFlZjQtOTc3NmE5NGNlYjU2IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay0yMS5kZXYucHJvdGVjdGxpbmUuZnIvcmVhbG1zL1Byb3RlY3RsaW5lIiwiYXVkIjoiaHR0cHM6Ly9rZXljbG9hay0yMS5kZXYucHJvdGVjdGxpbmUuZnIvcmVhbG1zL1Byb3RlY3RsaW5lIiwic3ViIjoiOGI5NTQ2MjAtOTcxYi00OTcwLWFmNWMtOWQ2MjllOTc1ZmRjIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6InVzYWdlLWRhdGFlbnJpY2hlciIsInNlc3Npb25fc3RhdGUiOiI3YTVmZDAzNC05YWM1LTQzNTctOWY0Mi0xZGJlOGQwZmFhNzUiLCJzY29wZSI6Im9wZW5pZCBjYW11bmRhLXJlc3QtYXBpIHRiX2NsaWVudCBlbWFpbCBwcm9maWxlIiwic2lkIjoiN2E1ZmQwMzQtOWFjNS00MzU3LTlmNDItMWRiZThkMGZhYTc1In0.HTWXz20aT89D1WeCuMIG7ycJWKv7NLopk5dfQA5UH3A",
"contractId" : "OSDEVICE3TNR",
"locationDetail" : "pir V1"
}

##### b. Traceability :
{
"metadata": {
"messageId": "c51879d7-e69b-4000-a3a3-3aec44bef7cd",
"callerId": "dataEnricher",
"messageType": "ENRICHMENT"
},
"uuid": "35a474ba-f99a-4d7d-81a7-505f4eb28c80",
"enrichmentDate": "2025-10-01T15:14:03.840424200Z",
"source": "doshock",
"deviceId": "Safehome-001399AAAAADTNR_3000116",
"contractId": "OSDEVICE3TNR",
"contractStatus": "active"
}



*****************************************************************************************


## CONTRAT SUSPENDED :
### 1. activation :

{
"dateTimeDevice" : "2025-10-14 00:07:55.000 +0200" ,
"dateTimeIOTGateway" : "2025-10-14 00:07:55.000 +0200" ,
"cid" : "app-arm-rfid",
"user" : "Celine",
"source" : "Safehome-001399AAAAADTNR_R_5549463",
"uuid": "2be8abcf-e493-4af1-816b-4a5d6bd134d5k"
}


#### a. sendTelemetry :
Pas de télémétrie

##### b. Traceability :
Pas de traçabilité

########################
### 2. alarm intrusion :

{
"dateTimeDevice" : "2025-10-14 00:07:55.000 +0200" ,
"dateTimeIOTGateway" : "2025-10-14 00:07:55.000 +0200" ,
"cid" : "app-alarm-matter",
"user" : "Celine",
"source" : "Safehome-001399AAAAADTNR_3000116",
"uuid" : "35a474ba-f99a-4d7d-81a7-505f4eb28c80"
}


##### a. sendTelemetry :
Pas de télémétrie

##### b. Traceability :
{
"metadata": {
"messageId": "2cf2ba99-691b-496f-b593-e0e344fcf356",
"callerId": "dataEnricher",
"messageType": "ENRICHMENT"
},
"uuid": "35a474ba-f99a-4d7d-81a7-505f4eb28c80",
"enrichmentDate": "2025-10-01T15:15:41.098824900Z",
"source": "doshock",
"deviceId": "Safehome-001399AAAAADTNR_3000116",
"contractId": "OSDEVICE3TNR",
"expectedNotification": false,
"expectedMonitoringStation": false,
"contractStatus": "suspended"
}






