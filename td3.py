# Fonction permettant de demander à l'utilisateur de rentrer un temps en jours, heures, minutes et secondes

def demandeTemps():
    jours = int(input("Entrez le nombre de jours voulus : "))
    while jours == ValueError:
        jours = int(input("Entrez une valeur correcte : "))
    heures = int(input("Entrez le nombre d'heures voulues : "))
    while heures > 24 or heures == ValueError:
        heures = int(input("Entrez une valeur correcte : "))
    minutes = int(input("Entrez le nombre de minutes voulues : "))
    while minutes > 60 or minutes == ValueError:
        minutes = int(input("Entrez une valeur correcte : "))
    secondes = int(input("Entrez le nombre de secondes voulues : "))
    while secondes > 60 or secondes == ValueError:
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
        message += f"{jours} {pluriel(jours, 'jour')}, "
    if heures > 0:
        message += f"{heures} {pluriel(heures, 'heure')}, "
    if minutes > 0:
        message += f"{minutes} {pluriel(minutes, 'minute')}, "
    if secondes > 0:
        message += f"{secondes} {pluriel(secondes, 'seconde')}"
    print(message, end="\n")

# Fonction permettant d'additionner deux temps distincts en les convertissant en secondes, puis en affichant le total normalement

def sommeTemps(temps1, temps2):
    secondes_total = tempsEnSecondes(temps1) + tempsEnSecondes(temps2)
    temps_total = secondeEnTemps(secondes_total)
    return temps_total

# Fonction permettant de calculer le pourcentage d'un temps

def proportionTemps(temps, pourcentage):
    temps_seconde = tempsEnSecondes(temps)
    temps_pourcentage = secondeEnTemps(temps_seconde * pourcentage)
    resultat_final = afficheTemps(temps_pourcentage)
    return resultat_final

# Fonction prenant un temps en entrée et renvoyant une date en années, mois, jours, minutes, secondes (à partir du 1er janvier 1970) 

def tempsEnDate(temps_utilisateur):
    temps_départ = (1970*365, 0, 0, 0)
    temps_final = sommeTemps(temps_départ, temps_utilisateur)
    return temps_final

# Fonction permettant d'afficher une date au format

def afficheDate(temps_utilisateur):
    temps_date = tempsEnDate(temps_utilisateur)
    jours, heures, minutes, secondes = temps_date
    années, mois = 0, 0
    années = jours // 365
    jours_restants = jours % 365
    mois = jours_restants // 30  
    jours_restants = mois % 30
    message = "La date finale est la suivante : "
    mois_nom = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    if jours_restants > 0:
        message += f"{jours_restants} "
    else:
        message += "1er "
    message += f"{mois_nom[mois]} "
    message += f"{années}\n"
    print(message)

#  Fonction permettant d'afficher toutes les années bissextiles depuis 1970

def bissextile(jours):
    année = jours // 365 + 1970
    for i in range(1970, année):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(i)

# Demande à l'utilisateur de choisir une option

conversion_temps_secondes = input("Bonjour. Voulez-vous convertir un temps donné en secndes ? Oui [Y], non [N] ")
if conversion_temps_secondes.lower() == "y":
    temps_saisi = demandeTemps()
    temps_converti = tempsEnSecondes(temps_saisi)
    print(f"Cela correspond à {temps_converti} secondes.\n")

conversion_secondes_temps = input("Maintenant, voulez-vous convertir un nombre de secondes en temps ? Oui [Y], non [N] ")
if conversion_secondes_temps.lower() == "y":
    seconde_saisie = int(input("Entrez un temps en seconde : "))
    temps_resultat = secondeEnTemps(seconde_saisie)
    afficheTemps(temps_resultat)

somme_temps = input("Voulez-vous effectuer la somme de deux temps ? Oui [Y], non [N] ")
if somme_temps.lower() == "y":
    temps1 = demandeTemps()
    temps2 = demandeTemps()
    resultat = sommeTemps(temps1, temps2)
    print(afficheTemps(resultat))

prop_temps = input("Voulez-vous obtenir la proportion d'un temps ? Oui [Y], non [N] ")
if prop_temps.lower() == "y":
    temps = demandeTemps()
    pourcentage = float(input("Quel pourcentage du temps voulez-vous obtenir ? ")) / 100
    proportionTemps(temps, pourcentage)

temps_en_date = input("Voulez-vous obtenir un temps sous forme de date (depuis le 1er janvier 1970 ? Oui [Y], non [N] ")
if temps_en_date.lower() == "y":
    temps_utilisateur = demandeTemps()
    afficheDate(temps_utilisateur)

années_bissextiles = input("Voulez-vous afficher toutes les années bissextiles depuis 1970 jusqu'à une date ? Oui [Y], non [N] ")
if années_bissextiles.lower() == "y":
    jours = int(input("Entrez un nombre de jours : "))
    bissextile(jours)