def saisie_temps():
    jours = int(input("Entrez le nombre de jours voulus : "))
    heures = int(input("Entrez le nombre d'heures voulues : "))
    minutes = int(input("Entrez le nombre de minutes voulues : "))
    secondes = int(input("Entrez le nombre de secondes voulues : "))
    return jours, heures, minutes, secondes

def temps_en_secondes(temps):
    jours, heures, minutes, secondes = temps
    temps_en_secondes = jours * 24 * 3600 + heures * 3600 + minutes * 60 + secondes
    return temps_en_secondes

def seconde_en_temps(seconde):
    jours = seconde // (24 * 3600)
    seconde = seconde % (24 * 3600)
    heures = seconde // 3600
    seconde = seconde % 3600
    minutes = seconde // 60
    seconde = seconde % 60
    return jours, heures, minutes, seconde

def pluriel(n, mot):
    return mot + "s" if n != 1 else mot

def affiche_temps(temps):
    jours, heures, minutes, secondes = temps
    
    message = ""
    if jours > 0:
        message += f"{jours} {pluriel(jours, 'jour')} "
    if heures > 0:
        message += f"{heures} {pluriel(heures, 'heure')} "
    if minutes > 0:
        message += f"{minutes} {pluriel(minutes, 'minute')} "
    if secondes > 0:
        message += f"{secondes} {pluriel(secondes, 'seconde')} "
    
    print(message, end="")

if __name__ == "__main__":
    temps_saisi = saisie_temps()
    temps_converti = temps_en_secondes(temps_saisi)
    
    print(type(temps_saisi))
    print(f"Cela correspond à {temps_converti} secondes")
    
    seconde_saisie = int(input("Entrez un temps en secondes : "))
    temps_resultat = seconde_en_temps(seconde_saisie)
    
    affiche_temps(temps_resultat)