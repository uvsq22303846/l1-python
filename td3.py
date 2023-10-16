# Fonction permettant de demander à l'utilisateur de rentrer un temps en jours, heures, minutes et secondes

def demandeTemps():
    jours = int(input("Entrez le nombre de jours voulus : "))
    heures = int(input("Entrez le nombre d'heures voulues : "))
    while heures > 24:
        heures = int(input("Entrez une valeur correcte : "))
    minutes = int(input("Entrez le nombre de minutes voulues : "))
    while minutes > 60:
        minutes = int(input("Entrez une valeur correcte : "))
    secondes = int(input("Entrez le nombre de secondes voulues : "))
    while secondes > 60:
        secondes = int(input("Entrez une valeur correcte : "))
    return jours, heures, minutes, secondes

# Fonction permettant de convertir en secondes le temps entré par l'utilisateur

def tempsEnSecondes(temps):
    jours, heures, minutes, secondes = temps
    temps_en_secondes = jours * 24 * 3600 + heures * 3600 + minutes * 60 + secondes
    return temps_en_secondes

# Fonction permettant de convertir en jour, heures minutes et seconde un temps donné en secondes par l'utilisateur

def secondeEnTemps(seconde):
    jours = seconde // (24 * 3600)
    seconde = seconde % (24 * 3600)
    heures = seconde // 3600
    seconde = seconde % 3600
    minutes = seconde // 60
    seconde = seconde % 60
    return jours, heures, minutes, seconde

# Fonction permettant de déterminer si un mot doit être mis au pluriel ou non

def pluriel(n, mot):
    return mot + "s" if n != 1 else mot

# Fonction permettant d'afficher un temps en jours, heures, minutes et secondes

def afficheTemps(temps):
    jours, heures, minutes, secondes = temps
    message = "Cela correspond à "
    if jours > 0:
        message += f"{jours} {pluriel(jours, 'jour')} "
    if heures > 0:
        message += f"{heures} {pluriel(heures, 'heure')} "
    if minutes > 0:
        message += f"{minutes} {pluriel(minutes, 'minute')} "
    if secondes > 0:
        message += f"{secondes} {pluriel(secondes, 'seconde')} "
    print(message, end="\n")

# Fonction permettant d'additionner deux temps distincts en les convertissant en secondes, puis en affichant le total normalement

def sommeTemps(temps1, temps2):
    secondes_total = tempsEnSecondes(temps1) + tempsEnSecondes(temps2)
    temps_total = secondeEnTemps(secondes_total)
    resultat = afficheTemps(temps_total)
    return temps_total

# Fonction permettant de calculer le pourcentage d'un temps

def proportionTemps(temps, pourcentage):
    print("Quel est le temps dont vous souhaitez connaître la proportion ?")
    temps = demandeTemps()
    temps_sec = tempsEnSecondes(temps)
    pourcentage = int(input("Quel est le pourcentage de ce temps que vous souhaitez connaître ? ")) / 100
    temps_pourcentage = secondeEnTemps(temps_sec * pourcentage)
    resultat_final = afficheTemps(temps_pourcentage)
    return resultat_final

# On utilise les premières fonctions afin de convertir en secondes un temps entré par l'utilisateur

conversion_temps_secondes = input("Bonjour. Voulez-vous convertir un temps donné en secondes ? Oui [Y], Non [N] ")
if conversion_temps_secondes == "Y".lower():
    temps_saisi = demandeTemps()
    temps_converti = tempsEnSecondes(temps_saisi)
    print(f"Cela correspond à {temps_converti} secondes.\n")

# On demande à l'utilisateur de rentrer un temps en secondes, puis on le converti en jours, heures, minutes et secondes

conversion_secondes_temps = input("Maintenant, voulez vous convertir un nombre de secondes en temps ? Oui [Y], Non [N] ")
if conversion_secondes_temps == "Y".lower():
    seconde_saisie = int(input("Entrez un temps en secondes : "))
    temps_resultat = secondeEnTemps(seconde_saisie)
    afficheTemps(temps_resultat)

# On demande à l'utilisateur de rentrer deux temps afin de réaliser leur somme

somme_temps = input("Enfin, voulez-vous effectuer la somme de deux temps ? Oui [Y], Non [N] ")
if somme_temps == "Y".lower():
    temps1 = demandeTemps()
    temps2 = demandeTemps()
    sommeTemps(temps1, temps2)

# On demande à l'utilisateur s'il veut calculer la proportion d'un temps

prop_temps = input("Enfin, voulez-vous obtenir la proportion d'un temps ? Oui [Y], Non [N] ")
if prop_temps == "Y".lower():
    temps = 0
    pourcentage = 0
    proportionTemps(temps, pourcentage)