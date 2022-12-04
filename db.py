"""
Ce module permetra d'interagire avec la base de données,
par exemple le programme passera pas ce module pour crée des tables,
la base de données. Le programme passera aussi pas ce module pour éffectuer
les différente opération du CRUD.
"""

from datetime import datetime
import time

import mysql.connector


def _create_database():
    "Cette fonction permet de crée la base de donnés"
    
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="pass",
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS popo_time;")
    
        
def _create_tables():
    "Cette fonction permet les différentes tables de la base de donnée"
    
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
            name VARCHAR(150) NOT NULL UNIQUE,
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
    

class TaskDataBase:
    """
    Cette class permet d'éffectuer toute 
    les opétations CRUD de la table task
    """
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="pass",
            database="popo_time",
        )   
        self.cursor = self.conn.cursor()
        
    def task_add(self, task_name: str):
        """
       Cette méthode permet d'inserer 
       de nouvelle tâche à la table task

        Args:
            task_name (str): Ce paramétre represente 
            le nom de la tâche à ajouter
        """
        from popo_time import ProgramMenu
        
        if not task_name:
            print("Veuillez entrer un nom de tâche valide !")
            time.sleep(1)
            return ProgramMenu().task_add()
        
        date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        date_updated = date_created
        value = (task_name, date_created, date_updated)
        
        try: 
            self.cursor.execute(
                f"""
                INSERT INTO task (
                    name,
                    date_created,
                    date_updated
                )
                VALUES (%s, %s, %s);
                """,
                value
            )
        except mysql.connector.errors.IntegrityError:
            print("La tâche que vous essayez d'ajouter existe déjà !")
            time.sleep(1)
            self.conn.close()
            ProgramMenu().program_start()
        else:
            self.conn.commit()
            self.conn.close()
            print("Tâche ajouté")
        
        
if __name__ == "__main__":
    _create_database()
    _create_tables()

