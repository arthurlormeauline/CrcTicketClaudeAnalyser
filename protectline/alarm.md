
Pour simuler un défaut de supervision : utiliser kafka-util :  
  [1381](https://protectline.atlassian.net/wiki/spaces/STU/pages/1536950283/Couverture+CID)-> défaut de supervision)
````
topic  - teamusages.dataEnrichementCrow.alarm.send  
header - false  
key    - Crow-0013A12596DA

{  
  "Crow-0013A12596DA_report": [  
    {  
      "_type": "report",  
      "_control_panel": "0013A12596DA",  
      "param1": 0,  
      "param2": 0,  
      "cid": 1381,  
      "panel_time": "2025-07-05T17:04:51.000Z",  
      "dateTimeTB": "2025-07-05T17:04:55.922Z",  
      "uuid": "cf64ca53-63c1-4be2-970d-25a7f9cc8389"  
    }  
  ]  
}
```


