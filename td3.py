jours = int(input("Entrez le nombre de jours voulus : "))
heures = int(input("Entrez le nombre d'heures voulues : "))
minutes = int(input("Entrez le nombre de minutes voulues : "))
secondes = int(input("Entrez le nombre de secondes voulues : "))
temps = (jours, heures, minutes, secondes)

def tempsEnSecondes(temps):
    jours = temps[0] * 24 * 3600
    heures = temps[1] * 3600
    minutes = temps[2] * 60
    secondes = temps[3]
    temps_en_secondes = jours + heures + minutes + secondes
    return temps_en_secondes

print(type(temps))
print(f"Cela correspond à {tempsEnSecondes(temps)} secondes")

seconde = int(input("Entrez un temps en secondes :"))

def secondeEnTemps(seconde):
    jours = seconde // (24*3600)
    seconde = seconde % (24*3600)
    heures = seconde // 3600
    seconde = seconde % 3600
    minutes = seconde // 60
    seconde = seconde % 60
    return jours, heures, minutes, seconde

temps = secondeEnTemps(seconde)
print(f"Cela correspond à {temps[0]} jours, {temps[1]} heures, {temps[2]} minutes et {temps[3]} secondes.")