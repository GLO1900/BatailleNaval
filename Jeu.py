
from Grille import Grille
from Joueur import Joueur
import Bateau


class Jeu:

    def __init__(self):

        self.joueur1 = Joueur('Joueur')
        self.joueur2 = Joueur('Adversaire')
        self.grille = Grille()

    def start(self, listebateaux):

        for i in range(listebateaux):

            self.joueur1.addbateau(listebateaux[i])

        for i in range(self.joueur1.listeBateau):
            self.grille.set(Grille.UNDAMAGED_BOAT, )