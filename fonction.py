import time
import pickle
import os
            
def chrono():
    temps = 0
    
    while True:
        # Création de temps
        temps += 1
        time.sleep(1)
        
        # Afichage du temps        
        heure = temps // 3600
        reste = temps % 3600
        minute = reste // 60
        seconde = reste % 60
        
        print(f"{heure}:{minute}:{seconde}")
        
def validation_profile():
    # Cette fonction aura pour mission d'ajouter un nouveau profile
    # Création de la basse de doonés qui va contenir nos profile et temps
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
        
def enregistrement_profile(profile):
    with open("profile", "wb") as fichier:
        sauvegarde = pickle.Pickler(fichier)
        sauvegarde.dump(profile)
        
def recuperation_profile():
    if os.path.exists("profile"):
        with open("profile", "rb") as fichier:
            recuperation = pickle.Unpickler(fichier)
            profile_recupere = recuperation.load()
            return profile_recupere
    else:
        profile_recupere = {}
    return profile_recupere