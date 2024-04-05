import tkinter as tk
from tkinter import messagebox


def decalage(lettre_message, lettre_cle):
    return chr((ord(lettre_message) - 97 + (ord(lettre_cle) - 97)) % 26 + 97)


def chiffrer_texte(message, cle):
    resultat = ""
    for i in range(len(message)):
        resultat += decalage(message[i], cle[i % len(cle)])
    return resultat


def chiffrer():
    message = entree_texte.get()
    cle = entree_cle.get()
    if not message or not cle:
        messagebox.showerror(title="Erreur", message="Le message ou la clé ne peuvent pas être vides.")
        return
    resultat = chiffrer_texte(message, cle)
    afficher_resultat.delete(0, tk.END)
    afficher_resultat.insert(0, resultat)


def decalage_inv(lettre_message, lettre_cle):
    return chr((ord(lettre_message) - ord(lettre_cle)) % 26 + 97)


def dec_texte_inv(message, cle):
    resultat = ""
    for i in range(len(message)):
        resultat += decalage_inv(message[i], cle[i % len(cle)])
    return resultat


def dechiffrer():
    message = entree_texte.get()
    cle = entree_cle.get()
    if not message or not cle:
        messagebox.showerror(title="Erreur", message="Le message ou la clé ne peuvent pas être vides.")
        return
    resultat = dec_texte_inv(message, cle)
    afficher_resultat.delete(0, tk.END)
    afficher_resultat.insert(0, resultat)


root = tk.Tk()

entree_texte = tk.Entry(root, width=20)
entree_texte.grid(row=0,  column=0)

texte_label = tk.Label(root, text="Entrez le message ici.")
texte_label.grid(row=0, column=1)

entree_cle = tk.Entry(root, width=20)
entree_cle.grid(row=1, column=0)

cle_label = tk.Label(root, text="Entrez la clé ici")
cle_label.grid(row=1, column=1)

bouton_chiffrer = tk.Button(root, text="Chiffrer texte", command=chiffrer)
bouton_chiffrer.grid(row=2, column=0)

bouton_dechiffrer = tk.Button(root, text="Déchiffrer texte", command=dechiffrer)
bouton_dechiffrer.grid(row=2, column=1)

afficher_resultat = tk.Entry(root, width=20)
afficher_resultat.grid(row=3, column=0)

root.mainloop()
