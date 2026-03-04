# Health Establishments

Projet personnel visant à centraliser et visualiser des données de santé
(CMP, MDS, etc.) sous forme de tables et de cartes.

## 🎯 Objectifs
- Collecter des données via API ou scraping
- Stocker les données dans une base relationnelle
- Exposer les données via une API
- Visualiser les données (table, map)

## 🧱 Stack technique
- Backend : FastAPI (Python)
- Base de données : SQL Server (ou autre SGBD relationnel)
- Frontend : React 
- Cartographie : à définir

## 🚧 Statut
Projet en cours de développement.



Le `.get` permet d'eviter le problème de  `KeyError` on mets donc .get et pour mettre une valeur par defaut on met `.get("element","element_par_default")`

quand c'est une liste on met `.get("company",{})` pour que ça renvoie une liste vide si la liste et vide 

`user.get("name", "UNKNOWN")` → si "name" n’existe pas, renvoie "UNKNOWN"

`user.get("address", {})` → si "address" n’existe pas, renvoie un dictionnaire vide, ensuite on récupère "street"


# Supprimer + reset l’auto increment

`TRUNCATE TABLE mds RESTART IDENTITY;`

# Importer psycopg2 pour la connexion  sql 

`pip install psycopg2`
