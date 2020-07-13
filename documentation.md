# **NinjaWhois - Documentation**

[https://ninjawhois.herokuapp.com/](https://ninjawhois.herokuapp.com/)

## Définition

L&#39;application permet de savoir un nom de ninja selon des mots de technologies qu&#39;on peut retrouver ici : [https://github.com/sindresorhus/awesome](https://github.com/sindresorhus/awesome). Les données ont été crawler avec Visual Web Ripper.

 Le projet est codé en python avec le framework django et hébergé avec Heroku. Bootstrap est utilisé pour le HTML.

## Fonctionnalités

- Ajout de mots &quot;buzzword&quot; dans la base de données par l&#39;administration
- Remplissage de la base de données avec les données de &quot;Awesome List&quot;
- Recherche ajax sur le Front-end pour savoir le nom de ninja
- Stockage des résultats dans la base de données
- Tableau des derniers résultats sur le Front-end
- Partager son résultat avec un permalink
- Demander le nom de ninja en json par GET
- Intégration de test pour l&#39;api &quot;ninjify&quot; et de la base de données
- Responsive selon l&#39;appareil
- Intégration de rest-framework pour buzzwords

## Algorithme

1. Recherche une correspondance pour chaque mot dans la base de données et conserve un mot selon la moyenne des lettres par mot
2. Sépare les mots en 3 listes égales si possible, sinon retourne les mots sélectionnés
3. Conserve 3 mots selon la moyenne et retourne le résultat.

Améliorations futures

- Importer des adjectifs dans les buzzwords
- Limiter le nombre de mots


## Installation

Fonctionne sur Heroku / Repl.it / Serveur Python

Configuration de la base de données autres que &quot;sqlite&quot; au besoin

Utiliser la commande pour peupler la base de données

## Administration

[https://ninjawhois.herokuapp.com/admin/](https://ninjawhois.herokuapp.com/admin/)

Utilisateur: test

Mot de passe: test

## Commande

- python manage.py feeddb
  - permet de peupler les tables de buzzwords

## Tests

- python manage.py test buzzwords.tests
  - Test les catégories avec le nombre de buzzwords à partir de la base de données

- python manage.py test ninjify.tests
  - Test l&#39;api ninjify/?x=string 20 fois avec un maximum de 5 mots par test