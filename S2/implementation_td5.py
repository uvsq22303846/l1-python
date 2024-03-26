import tkinter as tk

taille_fenetre = 100
min_match = 3


def match_size(mot, i, j):
    k = 0
    while i + k < len(mot) and mot[i + k] == mot[j + k]:
        k += 1
    return k


def max_match(mot, i):
    j = max(0, i - taille_fenetre)
    max_match = (0, 0)
    while j < i:
        taille_match = match_size(mot, i, j)
        if taille_match > max_match[1]:
            max_match = (i - j, taille_match)
        j += 1
    return max_match


def compresse():
    texte_a_compresser = entree.get()
    texte_compresse = []
    i = 0
    while i < len(texte_a_compresser):
        pass
    affichage_compression.config(text=str(texte_compresse))


def taille(liste_LZ):
    taille = 0
    for elem in liste_LZ:
        pass
    return taille


def changeFenetre():
    global taille_fenetre
    taille_fenetre = int(entree_fenetre.get())


def match2():
    global min_match
    min_match = 2


def match3():
    global min_match
    min_match = 3


racine = tk.Tk()
racine.title("Compression de texte")

entree = tk.Entry(racine, width=100, font=("helvetica", "20"))
entree.grid(row=1, column=0)


entree_fenetre = tk.Entry(racine, width=100, font=("helvetica", "20"))
entree_fenetre.grid(row=0, column=0)

bouton_fenetre = tk.Button(
    racine,
    text="Régler la fenêtre de recherche",
    command=changeFenetre,
    font=("helvetica", "30"),
)
bouton_fenetre.grid(row=0, column=1)

affichage_compression = tk.Message(racine, font=("helvetica", "20"), width=1000)
affichage_compression.grid(row=2, column=0, columnspan=2)


affichage_decompression = tk.Message(racine, font=("helvetica", "20"), width=1000)
affichage_decompression.grid(row=5, column=0, columnspan=2)


affichage_binaire = tk.Message(racine, font=("helvetica", "20"), width=1000)
affichage_binaire.grid(row=6, column=0, columnspan=2)


bouton_compresser = tk.Button(
    racine, text="Compresser", command=compresse, font=("helvetica", "30")
)
bouton_compresser.grid(row=1, column=1)


bouton_match2 = tk.Button(
    racine, text="Match minimal de taille 2", command=match2, font=("helvetica", "30")
)
bouton_match2.grid(row=4, column=0)


bouton_match3 = tk.Button(
    racine, text="Match minimal de taille 3", command=match3, font=("helvetica", "20")
)
bouton_match3.grid(row=4, column=1)

resultat = tk.Label(racine, font=("helvetica", "20"))
resultat.grid(row=3, column=0, columnspan=2)

racine.mainloop()
