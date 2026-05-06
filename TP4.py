import os

class Etudiant:
    def __init__(self, massar, nom, prenom, module, note):
        self.massar = massar
        self.nom = nom
        self.prenom = prenom
        self.module = module
        self.note = str(note)

def ajouter_etudiant(etudiant):
    with open("etudiantS2.txt", "a", encoding="utf-8") as fichier:
        ligne = f"{etudiant.massar},{etudiant.nom},{etudiant.prenom},{etudiant.module},{etudiant.note}\n"
        fichier.write(ligne)

def afficher_etudiants():
    if not os.path.exists("etudiantS2.txt"):
        print("Erreur : Le fichier n'existe pas.")
        return
    
    with open("etudiantS2.txt", "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            liste = ligne.strip().split(",")
            if len(liste) == 5:
                print(f"Massar: {liste[0]} | Nom: {liste[1]} | Prénom: {liste[2]} | Module: {liste[3]} | Note: {liste[4]}")

def chercher_etudiant(nom_recherche):
    if not os.path.exists("etudiantS2.txt"):
        return
    
    trouve = False
    with open("etudiantS2.txt", "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            liste = ligne.strip().split(",")
            if len(liste) == 5 and liste[1].lower() == nom_recherche.lower():
                print(f"Étudiant trouvé : {liste[0]}, {liste[1]}, {liste[2]}, {liste[3]}, {liste[4]}")
                trouve = True
                
    if not trouve:
        print("Étudiant non trouvé.")

def supprimer_etudiant(code_massar):
    if not os.path.exists("etudiantS2.txt"):
        return
    
    with open("etudiantS2.txt", "r", encoding="utf-8") as fichier:
        lignes = fichier.readlines()
        
    with open("etudiantS2.txt", "w", encoding="utf-8") as fichier:
        for ligne in lignes:
            liste = ligne.strip().split(",")
            if len(liste) == 5 and liste[0] != code_massar:
                fichier.write(ligne)

def modifier_etudiant(code_massar):
    if not os.path.exists("etudiantS2.txt"):
        return
        
    with open("etudiantS2.txt", "r", encoding="utf-8") as fichier:
        lignes = fichier.readlines()
        
    with open("etudiantS2.txt", "w", encoding="utf-8") as fichier:
        for ligne in lignes:
            liste = ligne.strip().split(",")
            if len(liste) == 5 and liste[0] == code_massar:
                liste[1] = liste[1].upper()
                liste[2] = liste[2].upper()
                nouvelle_ligne = ",".join(liste) + "\n"
                fichier.write(nouvelle_ligne)
            else:
                fichier.write(ligne)

if __name__ == "__main__":
    open("etudiantS2.txt", "w").close()

    base_donnees = [
        Etudiant("G10101010", "Alaoui", "Mohammed", "Python", 14),
        Etudiant("G20202020", "Benali", "Samira", "Python", 16),
        Etudiant("G30303030", "Ait Omar", "Youssef", "Python", 18),
        Etudiant("G40404040", "Naciri", "Amina", "Python", 15),
        Etudiant("G50505050", "Idrissi", "Omar", "Python", 12),
        Etudiant("G60606060", "Chafik", "Rachid", "Python", 17),
        Etudiant("G70707070", "Tazi", "Karim", "Python", 13),
        Etudiant("G80808080", "Mansouri", "Khadija", "Python", 19),
        Etudiant("G90909090", "Bennani", "Salma", "Python", 11),
        Etudiant("G00000000", "Zaid", "Ali", "Python", 14)
    ]
    
    for etudiant in base_donnees:
        ajouter_etudiant(etudiant)

    print("\n--- 1. Liste Complète des Étudiants ---")
    afficher_etudiants()

    print("\n--- 2. Recherche de l'étudiant 'Ait Omar' ---")
    chercher_etudiant("Ait Omar")

    print("\n--- 3. Modification G20202020 (Majuscules) ---")
    modifier_etudiant("G20202020")
    afficher_etudiants()

    print("\n--- 4. Suppression de G10101010 ---")
    supprimer_etudiant("G10101010")
    afficher_etudiants()