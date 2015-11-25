from Bateau import Bateau


class Joueur():
    def __init__(self, nom):
        self.listeBateau = [Bateau(0, 2, (0, 0), 'Torpilleur'), Bateau(0, 3, (0, 0), 'Contre-Torpilleur')]
        self.nom = nom

    def __str__(self):
        string = ''
        string += self.nom
        string += '\n'
        for b in self.listeBateau:
            string += b.nom
        return string
