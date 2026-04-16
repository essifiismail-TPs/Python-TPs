def ajouter_contact(nom, numero):
    with open("contacts.txt", "a", encoding="utf-8") as fichier:
        fichier.write(f"{nom},{numero}\n")

def rechercher_contact(nom):
    try:
        with open("contacts.txt", "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                donnees = ligne.strip().split(",")
                if len(donnees) == 2 and donnees[0] == nom:
                    return donnees[1]
        return "Contact introuvable"
    except FileNotFoundError:
        return "Contact introuvable"

for _ in range(3):
    nom_saisi = input("Entrez le nom du contact : ")
    numero_saisi = input("Entrez le numéro de téléphone : ")
    ajouter_contact(nom_saisi, numero_saisi)

resultat_recherche = rechercher_contact("Ait Ali")
print(f"Résultat de la recherche pour 'Ait Ali' : {resultat_recherche}")