"""
Ce module permettra d'interagir avec la base de données;
par exemple le programme passera pas ce module pour créer des tables et
la base de données. Le programme passera aussi pas ce module pour effectuer
Les différentes opérations du CRUD.
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
    "Cette fonction permet de crée les différentes tables de la base de donnée"
    
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
        else:
            self.conn.commit()
            print("Tâche ajouté !")
        finally:
            self.conn.close()
            time.sleep(1)
            ProgramMenu().program_start()
        
    def task_modify(self, task_id: int, new_name_task: str):
        """
        Cette méthode permet de modifier 
        une entré dans la table task

        Args:
            task_id (int): Ce pramètre represente l'identifiant de la
            tâche modifier
            new_name_task (str): Ce pramètre represente le nom de la 
            nouvelle tâche
        """        
        from popo_time import ProgramMenu
        
        date_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        value = (new_name_task, date_updated, task_id)
        
        self.cursor.execute(
            f"""
            UPDATE task SET name = %s, date_updated = %s
            WHERE id = %s;
            """,
            value
        )
        self.conn.commit()
        self.conn.close()

            
        
        
if __name__ == "__main__":
    _create_database()
    _create_tables()

