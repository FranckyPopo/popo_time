"""
Ce module permetra d'interagire avec la base de données,
par exemple le programme passera pas ce module pour crée des tables,
la base de données. Le programme passera aussi pas ce module pour éffectuer
les différente opération du CRUD.
"""

import mysql.connector


def _created_database():
    "Cette fonction permetra de crée un base de donnés"
    
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="pass",
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS popo_time;")
        
        
def _create_tables():
    "Cette fonction permetra de crée les différentes tables de la base de donnée"
    
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="pass",
        database="popo_time"
    )
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS task (
            id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            name VARCHAR(150) NOT NULL,
            date_created DATETIME NOT NULL,
            date_updated DATETIME NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS timer (
            id INT AUTO_INCREMENT PRIMARY KEY,
            minutes INT NOT NULL,
            task_id INT NOT NULL,
            FOREIGN KEY (task_id) REFERENCES task (id),
            date_created DATETIME NOT NULL
        );
        """
    )


if __name__ == "__main__":
    _created_database()
    _create_tables()
    
    
    
    
    
    