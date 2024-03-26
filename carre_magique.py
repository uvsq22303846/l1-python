carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]

carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def AfficheCarre(carre):
    for i in range(4):
        print(carre[i])


def testLignesEgales(carre):
    somme = []
    for i in range(4):
        somme.append(sum(carre[i]))
    if somme[0] == somme[1] == somme[2] == somme[3]:
        return somme[0]
    else:
        return -1


def testColonnesEgales(carre):
    for j in range(4):
        somme = 0
        for i in range(4):
            somme += carre[i][j]
        if j == 0:
            somme_finale = somme
        else:
            if somme_finale != somme:
                return -1
    return somme_finale


def testDiagonalesEgales(carre):
    taille = len(carre)
    somme_diagonale_principale = sum(carre[i][i] for i in range(taille))
    somme_diagonale_inverse = sum(carre[i][taille - 1 - i] for i in range(taille))
    if somme_diagonale_principale != somme_diagonale_inverse:
        return -1
    return somme_diagonale_principale


def estCarreMagique(carre):
    if testLignesEgales(carre) == -1:
        False
    elif testColonnesEgales(carre) == -1:
        False
    elif testDiagonalesEgales(carre) == -1:
        return False
    else:
        return True


def estNormal(carre):
    taille = len(carre)
    valeurs_attendues = set(range(1, taille**2 + 1))
    valeurs_carre = [valeur for ligne in carre for valeur in ligne]
    return set(valeurs_carre) == valeurs_attendues


print(testColonnesEgales(carre_pas_mag))
