# Coder avec Claue : comment ?

## Forces de Claude

- Très bon dans l'analyse et la proposition de solution logique si dans un ou peu de fichiers
- Très bon dans l'application de pattern sur un grand nombre d'occurence (il peut éditer très vite les fichiers)
- Débug assez bien si on lui fournit un message d'erreur (stacktrace ou erreur de compilation etc)
- Excellente base de connaissance de Java des framework usuelle et des bonnes pratiques de code.
- Libère du temps pour travailler sur autre chose (mais attention à ne pas perdre le fil --> cf limitations)

## Limitations

- Peut mettre plusieurs itérations pour trouver la cause d'un problème (devient finalement plus lent qu'un humain doter d'un debugger dans certain cas)
- N'est pas exhaustif lorsque le nombre de fichier ou d'occurence à traiter est grand (oublis !)
- N'est pas exhaustif dans sa lecture de doc si elle est trop grande
- Peut faire plus que ce qu'on lui a demander (un plus dans certain cas, mais pas toujours)
- Difficile de suivre le raisonnement quand c'est pas toi qui le fait !
        - Comment rester engager intellectuellement quand on ne réfléchis pas directement dessus ?
- Les prompts peuvent être répétitifs à écrire et pas très fun (dès fois on veut juste coder nous même !)

## Tips and tricks

- Tous persister dans des fichiers : input et output :
        - prompt
        - réponse de claude (lui demander de répondre dans un ficheir spécifique)

- utiliser des templates de prompt pour éviter d'avoir à répéter certaines info de prompt en prompt (le module ou les classes où on travaille par exemple).

- Garder la main sur les commits : cela permet de gérer la granularité de travail de Claude

- Penser à intellij pour les tâches basiques ou l'exhaustivité est importantes (déplacement de fichier, renommage etc.)

- penser à toujours demander à Claude ce qu'il compte faire et lui demander explicitement de valider chacune de ses approches avant l'implémentation ; cela permet de vérifier en amont.
