import fonction
import os
import data
import time

menu = """
---------- Bienvenue dans le menu ----------
1- Démarer le chronométre
2- Voir l'historique
3- Changer de profile
4- Quitter le programme
"""

path_file = os.path.realpath(__file__)
path_folder = os.path.dirname(path_file)
folder_data_programmme = os.path.join(path_folder, "data_programme")
file_profile_list = folder_data_programmme + "/" + "profile_list"
file_history = folder_data_programmme + "/" + "history"

if not os.path.isfile(file_history) and not os.path.isfile(file_profile_list):
    data.data_recording([], path_folder, "data_programme", "profile_list")
    data.data_recording([], path_folder, "data_programme", "history")

profile_exist = False

# Récupération des différentes données
profile_list_recovery = data.get_data(folder_data_programmme, "profile_list")
history = data.get_data(folder_data_programmme, "history")

print(history, profile_list_recovery)
    
profile = None
while True:  
    choice_profile = input("Veuillez entrer le nom de vôtre profile: ").lower()   
            
    for profile in profile_list_recovery:
        if profile["nom_profile"] == choice_profile:
            profile = profile
            profile_exist = True
                    
    while profile_exist == False:

        if not profile_exist:
            choice = input("Le profile n'existe pas ! Voulez vous crée un profile O/N ? ").upper()
            
            if choice == "O":
                name_profile = fonction.validation_profile()
                instance_profile = {"nom_profile": name_profile, "total_time": 0}
                profile_list_recovery.append(instance_profile)
                print(profile_list_recovery)
                profile_exist = True
                print("Vous venez de crée un nouveau profile")
                data.data_recording(profile_list_recovery, path_folder, "data_programme", "profile_list")
                time.sleep(1.5)
            else:
                break
    
    while profile_exist:
        print(menu)  
        choice_menu = int(input())
        
        if choice_menu == 1:
            stopwatch = fonction.stopwatch()
            profile["total_time"] += stopwatch
            data.data_recording(profile_list_recovery, path_folder, "data_programme", "profile_list")
        elif choice_menu == 2:
            pass                
        
        

