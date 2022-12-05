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
        cls._create_tables()
        
    def setUp(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="pass",
            database="popo_time_test",
        )
        self.cursor = self.conn.cursor()
        
    @classmethod
    def tearDownClass(cls):
        conn = mysql.connector.connect(
            host="127.1.1.0",
            user="root",
            passwd="pass",
        )
        cursor = conn.cursor()
        cursor.execute("DROP DATABASE popo_time_test;")
    
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
