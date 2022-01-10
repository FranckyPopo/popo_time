import time
import os
import keyboard
import datetime
import data
    
def stopwatch():
    temp = 0
    print("le chrono a démarer")
    print("Pour quitter le chrono taper Q")
    
    while True:
        time.sleep(1)
        if keyboard.is_pressed("q"):
            print("Vous venez de quitter le chrono")
            return temp
            break
        else:
            # Création de temps
            temp += 1
            
            # Afichage du temps        
            heure = temp // 3600
            reste = temp % 3600
            minute = reste // 60
            seconde = reste % 60    
            print(f"{heure}:{minute}:{seconde}")
                  
def validation_profile():
    
    """
    Cette fonction va nous permétre vérifier le nom d'un profile

    Returns:
        [str]: On retourne le nom du profile
    """
    nom_du_profile = input("Veuillez entrer le nom de vôtre nouveau profile !")
    
    # On vérifie si le nom du profile contient au moin 4 caractére et qu'il ne contient pas de caratére spécial
    while True:
        if len(nom_du_profile) < 4:
            print("Le nom de vôtre profile est trop cour il dois contenir au moin 4 caractére ")
            nom_du_profile = input("Veuillez entrer le nom de vôtre nouveau profile !")
        elif not nom_du_profile.isalnum():
            print("Les caractéres spéciaux ne sont par toléré")
            nom_du_profile = input("Veuillez entrer le nom de vôtre nouveau profile sans caractére spéciale ")
        else:
            print("Vous venez de crée un nouveaux profile")
            return nom_du_profile
            break
        
def history(name_profile, time_stopwatch):
    """
    Cette fonction va permetre de d'enregistrer une nouvelle instance dans l'historique ou fait la mise du temps
    qui exite déjà

    Args:
        name_profile (str): Ce paramétre reprente le nom du profile, il va nous servir lors de la création de l'instance
        time_stopwatch (int): Ce paramétre reprente le temps du chronométre
    """

    folder_current = os.getcwd()
    folder_data_programmme = os.path.join(folder_current, "data_programme")
    history = data.get_data(folder_data_programmme, "history")

    history_exist = False
    date_current = datetime.date.today()
    instance_history = {
        "name_profile": name_profile,
        "date": str(date_current),
        "time": 0
    }   
         
    # On vérifie que le profile existe dans l'historique
    for profile_history in history:
        if profile_history["name_profile"] == name_profile and profile_history["date"] == str(date_current):
            history_exist = True
            break
    else:
        instance_history["time"] += time_stopwatch
        history.append(instance_history)
        data.data_recording(history, folder_current, "data_programme", "history")  
        
    if history_exist:
        profile_history["time"] += time_stopwatch 
        data.data_recording(history, folder_current, "data_programme", "history")  
        
