valeur_recherchee = input("Entrez la valeur à rechercher : ")
occurrences = 0

try:
    with open("fichier.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        mots = contenu.split()
        occurrences = mots.count(valeur_recherchee)
    print(f"Occurrences : {occurrences}")
except FileNotFoundError:
    print("Fichier introuvable.")