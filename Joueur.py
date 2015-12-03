from Bateau import Bateau


class Joueur:

    def __init__(self, nom):
        self.listeBateau = []
        self.nom = nom

    def addbateau(self, bateau):
        self.listeBateau.append(bateau)

    def __str__(self):
        string = ''
        string += self.nom
        string += '\n'
        for b in self.listeBateau:
            string += b.nom
        return string
