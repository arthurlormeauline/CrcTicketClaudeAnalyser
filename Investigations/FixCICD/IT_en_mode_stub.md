# IT en mode stub

Qu'est ce qu'on a besoin de stubber : 

- appels base de donnée --> h2 ou postgres dans docker via testcontainer (à investiguer)
- consul --> en dur dans le projet (1 interface ConfigurationService, 2 implementation : prod et stub, une appelle consul l'autre des fichiers de conf directement dans le repo)
- appels http --> wiremock