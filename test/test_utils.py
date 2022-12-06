from test_db import MockBD
import utils


class TestUtils(MockBD):
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