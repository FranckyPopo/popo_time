from datetime import datetime

from test_db import MockBD
import utils


class TestUtils(MockBD):
    "Cette class va permetre de tester les fonctions du module utils"
    
    def test_get_data_from_database(self):
        "Cette méthode test la fonction get_data_from_database"
        
        tasks = utils.get_data_from_database(
            "popo_time_test",
            "task_test",
        )
        self.assertIsInstance(
            tasks,
            list,
            "Le type retourné n'est pas une liste"
        )
        
        for task in tasks:
            self.assertIsInstance(
                task,
                tuple,
                "Le type de donnée n'est pas un tuple",
            )
            self.assertEqual(len(task), 4)
            
    def test_get_item_from_database(self):
        "Cette méthode test la fonction get_item_from_database"
        
        task = utils.get_item_from_database(
            "popo_time_test",
            "task_test",
            "2",
        )
        
        # Vérifions les caractèristiques de l'entré retourné
        self.assertEqual(
            len(task),
            4,
            "L'entré est censé renvoyez un tuple avec 4 élèment à l'interieur"
        )
        self.assertIsInstance(
            task,
            tuple,
            "Le type de l'entré retourné n'est pas un tuple",
        )
        
        # Vérifions les types des données de l'entré retourné
        task_id = task[0]
        task_name = task[1]
        task_date_crated = task[2]
        task_date_updated = task[2]
        
        self.assertIsInstance(
            task_id,
            int,
            "Le type de l'identifiant de la tâche n'est pas un entier"
        )
        self.assertIsInstance(
            task_name,
            str,
            "Le type du nom de la tâche n'est pas une chaine de caractère"
        )
        self.assertIsInstance(
            task_date_crated,
            datetime,
            "Le type de la date de création n'est un datatime"
        )
        self.assertIsInstance(
            task_date_updated,
            datetime,
            "Le type de la date de mise ajout n'est un datatime"
        )
        
    def test_item_exists_in_database(self):
        "Cette méthode de test vérifie qu'une entré existe"
        
        task_1exists = utils.item_exists_in_database(
            "popo_time_test", 
            "task_test",
            "1"
        )
        task_5_exists = utils.item_exists_in_database(
            "popo_time_test", 
            "task_test",
            "5"
        )
        self.assertTrue(task_1exists)
        self.assertFalse(task_5_exists)
              
    
        
        