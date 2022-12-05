import time

import mysql.connector

from db import TaskDataBase
import utils


class ProgramMenu:
    "Cette class represent le menu d'acceuil du programme."
    
    def __init__(self):
        self.task_data_base = TaskDataBase()
        self.name_database = "popo_time"
        self.name_table = "task"
    
    def program_start(self):
        "Cette méthode represente le menu du programe"
        
        print("--------------- Bienvenu sur Popo Time ---------------")
        print("1 - Ajouter une tâche")
        print("2 - Modifier une tâche")
        print("3 - Supprimer une tâche")
        print("4 - Démarer le chrométre")
        print("5 - Voir l'historique")
        print("6 - Quitter le programme")
        self._throw_an_option()
        
    def _throw_an_option(self, option_number: str = None):
        time.sleep(1)
        options = {
            "1": self.task_add, 
            "2": self.task_modify, 
        }
        
        if option_number:
            options.get(option_number)()
        option = input("Veuillez choisir une option: ") 
        options.get(option)()
        
    def task_add(self):
        task_name = input("Veuillez entrer le nom de la tâche à enregistrer: ")
        self.task_data_base.task_add(task_name)
        
    def task_modify(self):
        # Affichage de la liste des tâches
        tasks = utils.get_data_from_database(self.name_database, self.name_table)
        for task in tasks:
            print(f"ID: {task[0]}, nom de la tâche: {task[1]}")
        
        # Vérifions que l'ID existe
        task_id = input("Veuillez entrer l'ID de la tâche à modifier: ")
        try:
            task_exists = utils.get_item_from_database(
                self.name_database,
                self.name_table,
                task_id,
            )
        except mysql.connector.errors.ProgrammingError:
            print("Aucune tâche est relier a cet identifiant")
            self._throw_an_option("2")
        else:
            if not task_exists:
                print("Aucune tâche est relier a cet identifiant")
                self._throw_an_option("2")
            
        
        new_name_task = input("Veuillez entrer le nouveau nom de la tâche: ")
        self.task_data_base.task_modify(task_id, new_name_task)
        