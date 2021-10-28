import fonction

# On récupere les profiles
profile_recuperer = fonction.recuperation_profile()
print(profile_recuperer)

# On demande a l'utilisateur de choisir un pofile
print("Veuillez choisir un profile")

# On affiche tout les profile qui son enregistré
for cle in profile_recuperer.keys():
    print(cle)
    
choix_profile = input("Veuillez entrer le nom de votre profile pour continuer: ")

# On enregistre l'utilisateur si le profile n'existe pas
if choix_profile not in profile_recuperer.keys():
    reponse = input("Votre profile n'exixte pas voulez vous crée un profile O/N: ")
    
    # on enregistre le profile
    if reponse.upper() == "O":
        # on verfie si le profile de l'utilisateur est correct 
        validation_profile = fonction.validation_profile()
        
        # on enregistre le profile
        profile_recuperer[validation_profile] = None
        fonction.enregistrement_profile(profile_recuperer)
        
# On affiche le menu a l'utilisateur si le profile choisir ou crée est dans la liste des profile
if choix_profile or validation_profile in profile_recuperer.keys():
    # Menu creation du menu
    # On affiche des option au menu
    print("---------- Bienvenue dans le menu du chrono ----------") 
    print("1- Démarer le chrone")
    print("2- Voir l'historique")
    print("3- Choisir un autres profile")
