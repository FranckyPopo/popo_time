import fonction
import os
import data
import time
from pprint import pprint

menu = """
---------- Bienvenue dans le menu ----------
1- Démarer le chronométre
2- Voir l'historique
3- Changer de profile
4- Quitter le programme
"""
display_history = """
Date: {}
Temps: {}
----------------------
"""

path_file = os.path.realpath(__file__)
path_folder = os.path.dirname(path_file)
folder_data_programmme = os.path.join(path_folder, "data_programme")
file_profile_list = folder_data_programmme + "/" + "profile_list.json"
file_history = folder_data_programmme + "/" + "history.json"

if not os.path.isfile(file_history) and not os.path.isfile(file_profile_list):
    data.data_recording([], path_folder, "data_programme", "profile_list")
    data.data_recording([], path_folder, "data_programme", "history")

profile_exist = False
profile_list_recovery = data.get_data(folder_data_programmme, "profile_list")

# On vérifie que le profile existe dans la liste des profiles
choice_profile = input("Veuillez entrer le nom de vôtre profile: ").lower()
for item in profile_list_recovery:
    if item["name_profile"] == choice_profile:
        profile_exist = True
        break
        
while True:

    while not profile_exist:
        choice = input("Le profile n'existe pas ! Voulez vous crée un profile O/N ? ").upper()

        if choice == "O":
            name_profile = fonction.validation_profile()
            #choice_profile = name_profile
            instance_profile = {"name_profile": name_profile, "total_time": 0}
            profile_list_recovery.append(instance_profile)
            profile_exist = True
            print("Vous venez de crée un nouveau profile")
            data.data_recording(profile_list_recovery, path_folder, "data_programme", "profile_list")
            time.sleep(1.5)
        else:
            break
    
    while profile_exist:
        print(menu)  
        choice_menu = int(input())
        history = data.get_data(folder_data_programmme, "history") 
        
        if choice_menu == 1:
            stopwatch = fonction.stopwatch()
            item["total_time"] += stopwatch
            fonction.history(item["name_profile"], stopwatch)
            data.data_recording(profile_list_recovery, path_folder, "data_programme", "profile_list")    
        elif choice_menu == 2:
            history_profile = [item for item in history if item["name_profile"] == choice_profile]
            
            for item in history_profile:
                hour = item["time"] // 3600
                rest_hour = item["time"] % 3600
                minute = rest_hour // 60
                seconde = rest_hour % 60 
                time_total = f"{hour}: {minute}: {seconde}"
                print(display_history.format(item["date"], time_total))
                time.sleep(0.5)
                