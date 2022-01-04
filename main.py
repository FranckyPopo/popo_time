import fonction

# On récupere les profiles
liste_profiles = fonction.recuperation_profile()
print(f'les temp quand on récupere des le demarage du programe: {liste_profiles}')

# On demande a l'utilisateur de choisir un pofile
print("Veuillez choisir un profile")

# On affiche tout les profile qui son enregistré q<w<<
for cle in liste_profiles.keys():
    print(cle)
    
choix_profile = input("Veuillez entrer le nom de votre profile pour continuer: ")

# On enregistre l'utilisateur si le profile n'existe pas
if choix_profile not in liste_profiles.keys():
    reponse = input("Votre profile n'exixte pas voulez vous crée un profile O/N: ")
    
    # on enregistre le profile
    if reponse.upper() == "O":
        # on verfie si le profile de l'utilisateur est correct 
        validation_profile = fonction.validation_profile()
        
        # on enregistre le profile
        liste_profiles[validation_profile] = 0
        fonction.enregistrement_profile(liste_profiles)
        
# On affiche le menu a l'utilisateur si le profile choisir ou crée est dans la liste des profile
if choix_profile or validation_profile in liste_profiles.keys():

    # On affiche le menu a l'utilisateur s'il passe le controle
    fonction.menu(choix_profile)       