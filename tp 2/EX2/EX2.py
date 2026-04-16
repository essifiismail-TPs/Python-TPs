fichier_source = input("Nom du fichier source : ")
fichier_dest = input("Nom du fichier destination : ")

try:
    with open(fichier_source, "r", encoding="utf-8") as source:
        lignes = source.readlines()
        
    with open(fichier_dest, "w", encoding="utf-8") as destination:
        destination.writelines(lignes)
    print("Opération de copie terminée avec succès.")
except FileNotFoundError:
    print("Fichier source introuvable.")