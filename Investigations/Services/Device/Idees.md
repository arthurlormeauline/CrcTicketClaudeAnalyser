# Idees de refacto pour service Device

## Ce qui ne va pas

- même model de Device pour les entrées sorties que pour le domaine (tout dans package bean avec les annotations pour le json et chose plus
problématique @AllArgsConstructo)
  - solution : créer un autre objet pour les rest IO

- design de package pas clair : un package model, mais du model un peu partout : où est le model ?

- noms inconsistent : on a l'impression que "Device" et "Gateway" sont interchangeable ou bien 2 concepts bien différents selon le context (voir aussi "Asset")

- pas de UT !!!!!!! refacto très difficile à faire

- DeviceServiceImpl tros gros, trop de responsabilité => séparer entre "Add" "Get" etc.

- DeviceServiceTest sont sensé être des UT mais font appel à Spring pour  @Autowired des objets qui pourraient être moqué ; résultat ça plante parce que le context applicatif 
n'arrive pas à se lancer
