import time
import os
import keyboard
    
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