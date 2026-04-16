nom_fichier = input("Nom du fichier : ")
mot_cible = input("Mot à supprimer : ")

try:
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        lignes = fichier.readlines()
        
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        for ligne in lignes:
            if mot_cible not in ligne:
                fichier.write(ligne)
    print("Filtrage terminé avec succès.")
except FileNotFoundError:
    print("Fichier introuvable.")