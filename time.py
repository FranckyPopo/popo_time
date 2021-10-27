import fonction

# On récupere les profiles
profile_recuperer = fonction.recuperation_profile()

# On demande a l'utilisateur de choisir un pofile
# On affiche tout les profile qui son enregistré
profile = input("Veuillez entrer le nom de votre profile pour continuer: ")

if profile not in profile_recuperer.keys():
    reponse = input("Votre profile n'exixte pas voulez vous crée un profile O/N")
    
    # on enregistre le profile
    if reponse == "O":
        # on verfie si le profile de l'utilisateur est correct 
        validation_profile = fonction.validation_profile()
        
        # on enregistre le profile
        profile_recuperer[validation_profile] = None
        fonction.enregistrement_profile(profile_recuperer)