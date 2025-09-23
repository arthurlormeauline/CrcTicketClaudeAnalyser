Après avoir recopié en vrac les specs depuis confluences plus quelques conseils d'implémentation :

```
dans todo.md j'ai mis quelques todo, il y aussi une description de la nouvelle api. C'est un peu mélangé. Je voudrais que tu mettes ce document en page dans un bon markdown. Ne change pas le contenu mais re organise dans des
sections clair : description de ce qu'il faut faire, description des doutes sur l'existant ou sur la marche à suivre, ce qu'il faut résoudre ; description sur les nouvelles implémentations à prévoir
```

Puis :

```
dans todo.md tu trouveras un récapitulatif de la nouvelle us à développer dans Dataenricher. Dans un nouveau fichier "UsFullAnalyze.md" :jJe voudrais dans un premier temps que tu analyse le projet, et que tu créé une liste
de tous les composants (classes, méthodes, enum, exception) à créer ou à réutiliser. Je veux que tu mettes à chaque fois si il y a des choses des informations complémentaires à fournir pour la bonne implémentation. Pour
chacun de ces composants je veux que tu mettes une stratégie de test unitaire et/ou d'intégration : limite toi à un test, dit s'il faut le créer from scratch ou l'ajouter à une suite de test existant, essaye d'être le plus
proche possible du test unitaire (on mock dès que possible). A la fin je veux que aussi que tu ajoutes la description d'un test d'intégration ou unitaire qui test globalement toute la nouvelle us
  
```

puis : 

```
ok, on va reprendre. Supprime le fichier que tu viens de créer et recommence => reprend mon prompts précédent et ajoute : on garde le test d'integration global, mais pour le reste on en reste aux tests unitaire. Je voudrais 
  aussi que dans ton découpage tu ai une approche plus top down : commence par la route, puis le processor, service, puis appel service externe. Intègre les modèles associés et constantes dans chaque section, l'idée c'est que 
  chaque section puisse tester par un test unitaire
```

puis: 

```
Plusieurs questions/remarques : je ne vois pas de couche parser implémenter dans les autres routes déjà éxistantes, si c'est optionel on va s'en passer pour garder l'homogénéité avec le reste du projet. Tu dis que la route
est responsable des ack/nack mais la couche processor gère aussi les nack pour 503/502, est ce une erreur ? si oui vaut il mieux gérer ça au niveau de la route ou du processor ? C'est quoi ReportMessagePayload ? La couche
service ne rend pas compte pour l'instant du fait qu'il y a deux appels distincs, le pattern c'est "appel+enrichment" et ça deux fois un pour asset l'autre pour device, avec les règles métier associés à chaque fois. Pour la
couche externe des connecteurs je ne vois rien dans ton document qui rende compte que pour device il n'y a rien à faire puisque déjà fait, mais qu'il par contre développer asset. Enlève les références à Lombok c'est trop
spécifiques. De manière général essaye de bien séparé ce qui est déjà implémenter et qu'on va utiliser de ce qu'il faut créer
```
