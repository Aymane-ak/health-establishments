import pandas as pd


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
  "nom maison des solidarités"     : "nom_maison_des_solidarités",
  "horaires accueil public"        : "horaires_accueil_public",
  "secteur maison des solidarités" : "secteur_maison_des_solidarités",
  "téléphone"                      : "telephone" 
})
# expand= True pour que ça me le sépare en deux 
nouvellesColonnes                  = df_cleaned["Geo Point"].str.split(",",expand= True)
df_cleaned["lat"]                  = nouvellesColonnes[0].astype(float)
#strip car après la virgule j'ai un espace 
df_cleaned["long"]                 = nouvellesColonnes[1].str.strip().astype(float)
df_cleaned.drop(["Geo Point"],axis = 1,inplace=True)  # inplace=True → modifie l’objet actuel
df_cleaned["code_postal"]          = df_cleaned["code_postal"].astype(str)

print("\nInfos dataframe cleaned :")
print(df_cleaned.info())



