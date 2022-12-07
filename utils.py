import mysql.connector
from dotenv import dotenv_values


ID_CONNEXION_DATABASE = dotenv_values()


def get_data_from_database(name_database: str, name_table: str) -> list[tuple]:
    "Cette fontion permet de récupèrer toute les entrés d'une table"
    
    conn = mysql.connector.connect(
        host=ID_CONNEXION_DATABASE.get("HOST_DATABASE"),
        user=ID_CONNEXION_DATABASE.get("USERNAME_DATABASE"),
        passwd=ID_CONNEXION_DATABASE.get("PASSWORD_DATABASE"),
        database=name_database
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {name_table};")
    return cursor.fetchall()


def get_item_from_database(name_database: str, name_table: str, id_item_search: str):
    conn = mysql.connector.connect(
        host=ID_CONNEXION_DATABASE["HOST_DATABASE"],
        user=ID_CONNEXION_DATABASE["USERNAME_DATABASE"],
        passwd=ID_CONNEXION_DATABASE["PASSWORD_DATABASE"],
        database=name_database
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {name_table};")
    return cursor.fetchone()
    

def item_exists_in_database(name_database: str, name_table: str, id_item_search: str) -> bool:
    "Cette méthode revoir True si l'entrer que nous cherchons existe"
    
    conn = mysql.connector.connect(
        host=ID_CONNEXION_DATABASE["HOST_DATABASE"],
        user=ID_CONNEXION_DATABASE["USERNAME_DATABASE"],
        passwd=ID_CONNEXION_DATABASE["PASSWORD_DATABASE"],
        database=name_database,
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT EXISTS( SELECT * FROM {name_table} WHERE id={id_item_search} );")
    result : tuple = cursor.fetchone()
    return True if result[0] else False