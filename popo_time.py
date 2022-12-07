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
        time.sleep(1)
        print("--------------- Bienvenu sur Popo Time ---------------")
        print("1 - Ajouter une tâche")
        print("2 - Modifier une tâche")
        print("3 - Supprimer une tâche")
        print("4 - Démarer le chrométre")
        print("5 - Voir l'historique")
        print("6 - Quitter le programme")
        self._throw_an_option()
        
    def _throw_an_option(self, option_number: str = None):
        """
        Cette méthode permet de sélectionner une option dans le menu.
        Le programmme demande de choisir une option si le paramétre 
        option_number n'a pas été passé en argument. Dans le cas 
        ou le paramètre option_number a été passé en argument une
        des méthodes qui se trouve dans la variable options est exécuté
        en fonction de la valeur de option number. 

        Args:
            option_number (str, optional): Ce paramétre represente
            une option du programme, par défault ça valeur est vide
        """        
        time.sleep(1)
        options = {
            "1": self.task_add, 
            "2": self.task_modify, 
            "3": self.task_delete, 
        }
        try:
            if option_number:
                options.get(option_number)()
            else:
                option = input("Veuillez choisir une option: ") 
                options.get(option)()
        except TypeError:
            print("L'option de vous avez choisir n'exite pas !")
        else:
            self.program_start()
        
    def task_add(self):
        task_name = input("Veuillez entrer le nom de la tâche à enregistrer: ")
        
        if not task_name:
            print("Entrer une valeur correcte !")
            self._throw_an_option("1")
        self.task_data_base.task_add(task_name)
        
    def display_list_of_task(self):
        "Cette méthode affiche la liste des tâches"
        
        time.sleep(1)
        tasks = utils.get_data_from_database(self.name_database, self.name_table)
        for task in tasks:
            print(f"ID: {task[0]}, nom de la tâche: {task[1]}")            
    
    def task_modify(self):
        tasks = utils.get_data_from_database(self.name_database, self.name_table)
        if tasks:
            # Affichage de la liste des tâches
            self.display_list_of_task()
        else:
            print("La liste des tâche est vide !")
            self.program_start()
        
        # Vérifions que l'ID existe
        task_id = input("Veuillez entrer l'ID de la tâche à modifier: ")
        try:
            task_exists = utils.item_exists_in_database(
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
            while not new_name_task:
                new_name_task = input("Veuillez entrer le nouveau nom de la tâche: ")
                
            self.task_data_base.task_modify(task_id, new_name_task)
            print("Tâche modifier avec success")
            ProgramMenu().program_start()
            
    def task_delete(self):
        tasks = utils.get_data_from_database(self.name_database, self.name_table)
        if tasks:
            # Affichage de la liste des tâches
            self.display_list_of_task()
        else:
            print("La liste des tâche est vide !")
            self.program_start()

        task_id = input("Veuillez entrer l'ID de la tâche à supprimer: ")
        try:
            task_exists = utils.item_exists_in_database(
                "popo_time",
                "task",
                task_id
            )
        except mysql.connector.errors.ProgrammingError:
            print("Aucune tâche est relier a cet identifiant !")
        else:
            if task_exists:
                self.task_data_base.task_delete(task_id)
            else:
                print("Aucune tâche est relier a cet identifiant !")
        
        
        
        