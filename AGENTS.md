## Conseils pour l'environnement de développement
- Vérifier l'environnement avant de proposer ou d'exécuter des commandes. Certains développeurs 
utilisent Codespaces (`bash`), d'autres utilisent Windows (`powershell`).

### Détails pour Codespaces
- Si l'utilisateur utilise Java, vérifier la version installée et, si ce n'est pas déjà fait,
installer `25.fx-zulu` avec : `sdk install java 25.fx-zulu`
- Si un utilisateur sur Codespaces développe un projet graphique mais le devcontainer n'est pas
configuré pour ça, lui proposer l'adaptation de configuration requise (par exemple, `desktop-lite`)

## Objectifs d'architecture
- Rester procédural avec modularisation en fonctions au besoin
- Pour les cours de 12ème seulement : l'organisation du code en classes est recommandé, soignant 
l'accès aux données
- Créer uniquement des tests unitaires et seulement dans le même fichier que le code à tester, sauf
si l'élève demande explicitement l'utilisation d'une bibliothèque de test spécifique
- Ne pas utiliser de structures plus complexes dans les tests que dans le code à tester.
- Ne pas utiliser de bibliothèques externes sauf si explicitement demandé par l'élève

## Permissions
- Dans tous les cas, avisez le requérant si la charge contextuelle s'approche de la limite. Si 
c'est le cas, lui recommander de commencer une nouvelle session avec le prompt `/start`
- Par défaut en modes edit et agent, utiliser le prompt `/todo`
- Attendre le prompt explicite `/go` avant de produire du code. Limiter le changement avant 
validation de l'élève à un maximum de 15 lignes ou une seule fonction ou méthode. Si plusieurs  
modifications de ce genre sont requis, énumérer les commentaires `TODO` créés à cette fin dans  
la discussion et demander une commande `/go` pour traiter chacun.
