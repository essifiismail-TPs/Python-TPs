class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

    def lire(self):
        print(f"<<< Je lis: {self.titre} de {self.auteur} >>>")

    def __str__(self):
        return f"<<< Livre: {self.titre} - {self.auteur} ({self.pages} pages) >>>"

    def __len__(self):
        return self.pages

    def __eq__(self, autre):
        if isinstance(autre, Livre):
            return self.titre == autre.titre and self.auteur == autre.auteur
        return False

l1 = Livre("1984", "Orwell", 328)
l2 = Livre("Le Petit Prince", "Saint-Exupéry", 96)

l1.lire()
l2.lire()

l3 = Livre("1984", "Orwell", 400)

print(l1)
print(len(l1))
print(l1 == l3)