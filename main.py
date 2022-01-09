import fonction
import os
import data
import time

path_file = os.path.realpath(__file__)
path_folder = os.path.dirname(path_file)
folder_data_programmme = os.path.join(path_folder, "data_programme")

if not os.path.exists(folder_data_programmme) or os.path.getsize(r"D:\Programmation\projet_personnel\popo_time\data_programme\profile_list.json") == 0:
    data.data_recording([], path_folder, "data_programme", "profile_list")

choice_profile = input("Veuillez entrer le nom de vôtre profile: ").lower()
while True:
    profile_exist = False
        
    while profile_exist == False:
        # Récupération de la liste des profiles
        profile_list_recovery = data.get_data(folder_data_programmme, "profile_list")
        
        for profile in profile_list_recovery:
            if profile["nom_profile"] == choice_profile:
                profile_exist = True

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
        elif profile_exist:
            menu = """
            ---------- Bienvenue dans le menu ----------
            1- Démarer le chronométre
            2- Voir l'historique
            3- Changer de profile
            4- Quitter le programme
            """
            print(menu)
            
            choice_menu = int(input())
            
            if choice_menu == 1:
                stopwatch = fonction.stopwatch()
                profile["total_time"] += stopwatch
                data.data_recording(profile_list_recovery, path_folder, "data_programme", "profile_list")
            elif choice_menu == 2:
                pass
            print(profile_list_recovery)
                
            
             

