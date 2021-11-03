import time
import pickle
import os
import keyboard

"""
NB: chercher a savoir pourquoi il a un probléme avec ma fonction menu ligne 64
"""
            
def chrono():
    temp = 0
    print("le chrono a démarer")
    print("Pour quitter le chrono taper Q")
    
    while True:
        if keyboard.is_pressed("q"):
            print("Vous venez de quitter le chrono")
            return temp
            break
        else:
            # Création de temps
            temp += 1
            time.sleep(1)
            
            # Afichage du temps        
            heure = temp // 3600
            reste = temp % 3600
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

def menu(profile_a_enregisttre):
    """
    UTILITER:
    Cette fonction aura pour but de gerer le menu
    
    UTILISATION:
    1- le premier paramére qui se nome profile_a_enregisttre prendra le profile a enregistrer
    """
    print("---------- Bienvenue dans le menu ----------")
    print("1- Démarer le chronométre")
    print("2- Voir l'historique")
    print("3- Changer de profile")
    reponse = int(input())
  
    if reponse == 1:
            temps_a_enregistrer = chrono()
            
            # On récupere les profiles
            liste_profiles = recuperation_profile()
            
            # Aprés avoir quitté le chrono on enregistre le temp passé par l'utilisateur
            liste_profiles[profile_a_enregisttre] += temps_a_enregistrer
            
            # on enregistre la variable profile recuperer
            enregistrement_profile(liste_profiles)
            
            # on raméne l'tilisateur au menu
            menu(profile_a_enregisttre)
            
    if reponse == 2:
        print("vous etre dans l'option 2")
