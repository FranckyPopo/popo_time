from db import TaskDataBase


class ProgramMenu:
    "Cette class represent le menu d'acceuil du programme."
    
    def __init__(self):
        self.task_data_base = TaskDataBase()
    
    def program_start(self):
        "Cette méthode represente le menu du programe"
        
        print("--------------- Bienvenu sur Popo Time ---------------")
        print("1- Ajouter une tâche")
        print("2- Modifier une tâche")
        print("3- Supprimer une tâche")
        print("4- Démarer le chrométre")
        print("5- Voir l'historique")
        print("6- Quitter le programme")
        option = input("Veuillez choisir une option: ") 
        options = {
            "1": self.task_add(), 
            "1": None, 
            "1": None, 
            "1": None, 
            "1": None, 
            "1": None, 
        }
        
    def task_add(self):
        task_name = input("Veuillez entrer le nom de la tâche à enregistrer: ")
        self.task_data_base.task_add(task_name)
        
        