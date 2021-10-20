import time
            
def chrono():
    temps = 0
    intervale = 1
    
    while True:
        # Création de temps
        temps += 1
        time.sleep(intervale)
        
        # Afichage du temps        
        heure = temps // 3600
        reste = temps % 3600
        minute = reste // 60
        seconde = reste % 60
        
        print(f"{heure}:{minute}:{seconde}")
        
def creation_profile():
    """ Cette fonction aura pour mission d'ajouter un nouveau profile """
    
    # Création de la basse de doonés qui va contenir nos profile et temps
    donnees_profile = {}
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
            donnees_profile[nom_du_profile] = None
            print("Vous venez de crée votre profile")
            print(donnees_profile)
            break
        

creation_profile()