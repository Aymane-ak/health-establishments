import os
import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

def insertData(dataFrame, table):
    """
    Insère les données d'un DataFrame Pandas dans une table PostgreSQL.

    Arguments :
    - dataFrame : pd.DataFrame contenant les données à insérer
    - table : nom de la table PostgreSQL
    """
    # --- Connexion à la base ---
    conn = psycopg2.connect(
        dbname   = os.getenv("DB_NAME"),
        user     = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host     = os.getenv("DB_HOST"),
        port     = os.getenv("DB_PORT")
    )
    cur = conn.cursor()  # curseur pour exécuter les requêtes

    try:
        # --- Préparer la requête SQL dynamique ---
        colonnes = ", ".join(dataFrame.columns)                      # "nom_commune, nom_maison_des_solidarites, ..."
        placeholders = ", ".join(["%s"] * len(dataFrame.columns))    # "%s, %s, %s, ..."
        requete = f"INSERT INTO {table} ({colonnes}) VALUES ({placeholders})"

        # --- Option 1 : boucle ligne par ligne ---
        for index, row in dataFrame.iterrows():
            values = tuple(row)            # convertir la ligne en tuple
            cur.execute(requete, values)   # insertion sécurisée avec psycopg2

        # --- Option 2 : tout en lot (plus rapide) ---
        # values_list = [tuple(row) for _, row in dataFrame.iterrows()]
        # cur.executemany(requete, values_list)

        conn.commit()  # valider toutes les insertions
        print(f"{len(dataFrame)} lignes insérées avec succès dans la table '{table}'.")

    except Exception as e:
        conn.rollback()  # annuler en cas d'erreur
        print("Erreur lors de l'insertion :", e)

    finally:
        cur.close()   # fermer le curseur
        conn.close()  # fermer la connexion

