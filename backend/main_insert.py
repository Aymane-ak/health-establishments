from scripts.clean_csv import df_cleaned
from scripts.insert_data import insertData

# Lancer l'insertion dans la table 'mds'
insertData(df_cleaned, "mds")