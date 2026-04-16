def ajouter_tache(titre, description, statut):
    with open("taches.txt", "a", encoding="utf-8") as fichier:
        fichier.write(f"{titre}|{description}|{statut}\n")

def afficher_taches():
    try:
        with open("taches.txt", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                donnees = ligne.strip().split("|")
                if len(donnees) == 3:
                    print(f"Titre : {donnees[0]}\nDescription : {donnees[1]}\nStatut : {donnees[2]}\n")
    except FileNotFoundError:
        print("Aucune tâche trouvée.")

for _ in range(3):
    titre_saisi = input("Titre de la tâche : ")
    desc_saisie = input("Description : ")
    statut_saisi = input("Statut : ")
    ajouter_tache(titre_saisi, desc_saisie, statut_saisi)

print("\n--- Liste des tâches ---")
afficher_taches()