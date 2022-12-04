import mysql.connector
from unittest import TestCase

from db import (
    _create_database,
    _create_tables,
)


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
    
    @classmethod
    def _create_data_base(cls):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="pass",
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS popo_time_test;")
    
    @classmethod
    def _create_tables(cls):
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
        pass
        
        
        
