import psycopg2 
import pandas as pd
import os
from dotenv import load_dotenv
import os

load_dotenv()

df = pd.read_csv("data/mds.csv", delimiter =";")
# Afficher les 5 premières lignes
print(df.head())
# Afficher les noms des colonnes
print("\nColonnes :")
print(df.columns)

# Infos générales
print("\nInfos :")
print(df.info())

df_cleaned = df.rename(columns= {    
  "nom maison des solidarités"     : "nom_maison_des_solidarites",
  "horaires accueil public"        : "horaires_accueil_public",
  "secteur maison des solidarités" : "secteur_maison_des_solidarites",
  "téléphone"                      : "telephone" 
})
# expand = True pour que ça me le sépare en deux 
nouvellesColonnes                  = df_cleaned["Geo Point"].str.split(",",expand= True)

# Création de la colonne lat 
df_cleaned["lat"]                  = nouvellesColonnes[0].astype(float)
# Création de la colonne lat 
# strip car après la virgule j'ai un espace 
df_cleaned["long"]                 = nouvellesColonnes[1].str.strip().astype(float)
df_cleaned.drop(["Geo Point"],axis = 1,inplace=True)  # inplace=True → modifie l’objet actuel
df_cleaned["code_postal"]          = df_cleaned["code_postal"].astype(str)

print("\nInfos dataframe cleaned :")
print(df_cleaned.info())


########  CONNEXION A LA BASE DE DONNEES  ######## 

conn = psycopg2.connect(
    dbname   = os.getenv("DB_NAME"),
    user     = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host     = os.getenv("DB_HOST"),
    port     = os.getenv("DB_PORT")
)
cur = conn.cursor()

cur.execute("SELECT * FROM mds")

records = cur.fetchall()

print( "Les resultats sont : " , records)

"""
try : 
  for index, row  in df_cleaned.iterrows() : 
    valeurs = (
        row['nom_commune'],
        row['nom_maison_des_solidarites'],
        row['adresse'],
        row['code_postal'],
        row['telephone'],
        row['secteur_maison_des_solidarites'],
        row['horaires_accueil_public'],
        row['type_site'],
        row['lat'], 
        row['long']
    )
    cur.execute(
      "INSERT INTO mds (nom_commune,nom_maison_des_solidarites,adresse,code_postal,telephone,secteur_maison_des_solidarites,horaires_accueil_public,"
      "type_site,lat,long) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
      valeurs ) 

    ##cur.executemany(
    # "INSERT INTO mds (nom_commune,nom_maison_des_solidarites,adresse,code_postal,telephone,secteur_maison_des_solidarites,horaires_accueil_public,"
    ##"type_site,lat,long) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", valeurs ) 
  conn.commit()
except Exception as e :  
  conn.rollback()
  print("Erreur : " , e)
finally : 
  cur.close()
  conn.close()
    
"""
