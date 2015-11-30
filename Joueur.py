from Bateau import Bateau
from Grille import Grille

class Joueur():
    def __init__(self, nom):
        self.listeBateau = [Bateau(0, 2, (0, 0), 'Torpilleur'), Bateau(0, 3, (0, 0), 'Contre-Torpilleur'),
                            Bateau(0, 3, (0, 0), 'Sous-Marin'), Bateau(0, 5, (0, 0), 'Porte-Avions'),
                            Bateau(0, 4, (0, 0), 'Croiseur')]
        self.nom = nom
        self.grille = Grille()

    def __str__(self):
        string = ''
        string += self.nom
        string += '\n'
        for b in self.listeBateau:
            string += b.nom
        return string
