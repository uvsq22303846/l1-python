import re

user_password = str(input("Entrez votre mot de passe : "))

caps_letter = re.search("[A-Z]", user_password)
letter = re.search("[a-z]", user_password)
numbers = re.search("[0-9]", user_password)
special = re.search("[$#@]", user_password)
length = (6 <= len(user_password) <= 16)

if caps_letter == None or letter == None or numbers == None or length == False:
    print("Votre mot de passe n'est pas valide. Veuillez réessayer.")
else:
    print("Bravo, vous avez rentré un mot de passe valide !")