import Bateau


class Joueur(Bateau):
    def __init__(self, nom):
        self.listeBateau = [self.Bateau(0, 5, (0, 0), "Porte-Avion"), self.Bateau(0, 4, (0, 0), "Croiseur"),
                            self.Bateau(0, 3, (0, 0), "Contre-Torpilleur"), self.Bateau(0, 3, (0, 0), "Sous-Marin"),
                            self.Bateau(0, 2, (0, 0), "Torpilleur")]
        self.nom = nom
