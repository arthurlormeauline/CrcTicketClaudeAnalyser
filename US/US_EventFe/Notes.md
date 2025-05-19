# Event Fe : notes

- derniers changement à intégrer dans event-fe depuis crm-customer-fe : TOF-6058
- exemples d'intégreation micro fe : crm angular -> TOF-5934

Bug : moins de résultat sans préciser de date qu'en ne prenant que le dernier mois

## Reconnecter à notre back

getDevicesByContractId : assez cher à faire, pas mal de logique (non testée) côté back crm  ; la solution la plus propre serait de déporter cette logique côté back Device

getDeviceTypeList : catalog donc pas chez nous ; mais si on met la logique de getDevicesByContractId chez Device, on aura un spi vers catalog, donc on pourrait imaginer un seul
appel "GetDeviceTypeAndDeviceByContractId" chez Device
