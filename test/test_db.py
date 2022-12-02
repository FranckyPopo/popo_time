import unittest

from db import (
    _create_database,
    _create_tables,
)


class DataBaseTest(unittest.TestCase):
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

