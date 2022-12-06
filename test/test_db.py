from unittest import TestCase
from datetime import datetime

import mysql.connector

from db import (
    _create_database,
    _create_tables,
)
import utils


class TestDataBase(TestCase):
    """
    Cette class s'occupe de tester la création de la 
    base de données et la création des différents table 
    """ 
    def test_create_data_base(self):
        "Ce test permet de vérifier la création de la base de données"
        self.assertIsNone(
            _create_database(),
            "La création de la base données ne c'est pas faite correctement"
        )
        
    def test_create_tables(self):
        "Ce test permet de vérifier la création des tables dans la base de données"
        self.assertIsNone(
            _create_tables(),
            "La création des tables ne c'est pas faite correctement"
        )
     
     
class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._create_data_base()
                
    def setUp(self):
        MockBD._create_tables()
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="pass",
            database="popo_time_test",
        )
        self.cursor = self.conn.cursor()
        
        test_in_progress = self.id()
        path_test = [
            "test_utils.TestUtils.test_get_data_from_database",
            "test_utils.TestUtils.test_get_item_from_database",
        ]
        if test_in_progress in path_test:
            self.adding_data_to_tables()
        
    def tearDown(self):
        self.cursor.execute(
            """
            DROP TABLE IF EXISTS task_test;
            DROP TABLE IF EXISTS timer_test;
            """
        )
        self.cursor.close() 
        
    @classmethod
    def tearDownClass(cls):
        conn = mysql.connector.connect(
            host="127.1.1.0",
            user="root",
            passwd="pass",
        )
        cursor = conn.cursor()
        cursor.execute("DROP DATABASE popo_time_test;")
    
    def adding_data_to_tables(self):
        """
        Cette méthode permet d'ajouter des données  
        dans les tables task_test et timer_tesy
        """
                
        # Ajout des donnés dans la  table task_test
        values = [
            (
                "Gagnez de l'argent", 
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),
            (
                "Rendre heureuse ma mére", 
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),
            (
                "Se former", 
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),
        ]
        
        self.cursor.executemany(
            """
            INSERT INTO task_test (
                name,
                date_created,
                date_updated
            )
            VALUES (%s, %s, %s)
            """,
            values
        )
        self.conn.commit()
        
    @classmethod
    def _create_data_base(cls):
        "Cette méthode crée une base de données fictive pour les test unitaire"
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="pass",
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS popo_time_test;")
    
    @classmethod
    def _create_tables(cls):
        "Cette méthode permet de crée des table fictive pour les test unitaire"
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="pass",
            database="popo_time_test"
        )
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS task_test (
                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                name VARCHAR(50) NOT NULL UNIQUE,
                date_created DATETIME NOT NULL,
                date_updated DATETIME NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS timer_test (
                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                minutes INT NOT NULL,
                task_id INT NOT NULL,
                FOREIGN KEY (task_id) REFERENCES task (id),
                date_created DATETIME NOT NULL
            );
            """
        )   
        conn.close()


class TestTableTask(MockBD):
    """
    Cette class s'occupe de tester toute les opération 
    CRUD qu'éffectura le programme sur la table task
    """
    
    def test_task_add(self):
        "Cette méthode de test permet de tester qu'une tâche est bien ajouté à la table task_test"
        
        # On vérifie que rien n'existe dans la table task_test
        tasks = utils.get_data_from_database("popo_time_test", "task_test")
        self.assertEqual(
            len(tasks),
            0,
            "Il existe des données dans la table task_test"
        )
        
        # Ajout des données dans la table task_test
        date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        date_updated = date_created
        values = [
            ("Jouer au foot", date_created, date_updated),
            ("Faire des projet", date_created, date_updated),
            ("Gagner de l'argent", date_created, date_updated),
        ]
        self.cursor.executemany(
            """
            INSERT INTO task_test (
                name,
                date_created,
                date_updated
            )
            VALUES (%s, %s, %s);
            """,
            values
        )
        self.conn.commit()
        
        tasks = utils.get_data_from_database("popo_time_test", "task_test")
        self.assertEqual(
            len(tasks),
            3,
            "Il existe plus de données qu'il en devais avoir dans la table tasks"
        )
        
    def test_task_modify(self):
        # Ajout d'une tâche dans la table task_test
        date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        date_updated = date_created
        value = ("Jouer au foot", date_created, date_updated)
    
        self.cursor.execute(
            """
            INSERT INTO task_test (
                name,
                date_created,
                date_updated
            )
            VALUES (%s, %s, %s);
            """,
            value
        )
        self.conn.commit()
        
        # Vérifions que la tâche a été crée
        task_id = 1
        task_exists = utils.item_exists_in_database(
            "popo_time_test",
            "task_test",
            task_id
        )
        self.assertTrue(task_exists, "La tâche recherché n'existe pas !")
        
        # Modification de la tâche
        date_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_new_name = "Gagner de l'argent"
        value = (task_new_name, date_updated, task_id)
        
        self.cursor.execute(
            f"""
            UPDATE task_test SET name = %s, date_updated = %s
            WHERE id = %s;
            """,
            value
        )
        self.conn.commit()

        # récupération de la tâche
        task = utils.get_item_from_database(
            "popo_time_test",
            "task_test",
            task_id
        )
        task_name = task[1]
        task_date_updated = task[3].strftime('%Y-%m-%d %H:%M:%S')
        
        # Vérifions que les modification on été appliqué
        self.assertEqual(
            task_name,
            task_new_name,
            "Les noms des deux tache sont différent"
        )
        self.assertEqual(
            date_updated,
            task_date_updated,
            "Les dates de mise ajout ne correspondent pas"
        )
        