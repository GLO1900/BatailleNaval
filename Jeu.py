
from Grille import Grille
from Joueur import Joueur
from Bateau import Bateau

class Jeu:

    def __init__(self):

        self.joueur1 = Joueur('Joueur')
        self.turn = True
        self.joueur2 = Joueur('Adversaire')
        self.grille = Grille()

    def start(self, listebateaux1, listebateau2):

        print('test')

        for i in range(len(listebateaux1)):

            self.joueur1.addbateau(listebateaux1[i])

        for i in range(len(listebateau2)):

            self.joueur2.addbateau(listebateau2[i])

        for i in range(len(self.joueur1.listeBateau) - 1):
            if (self.joueur1.listeBateau[i].getOrientation() == False):

                for j in range(self.joueur1.listeBateau[i].getLongueur()):

                    self.grille.set(Grille.UNDAMAGED_BOAT, int(self.joueur1.listeBateau[i].getCoordonneex() + j),
                                    int(self.joueur1.listeBateau[i].getCoordonneey()))

            elif(self.joueur1.listeBateau[i].getOrientation() == True):

                 for k in range(self.joueur1.listeBateau[i].getLongueur()):
                    self.grille.set(Grille.UNDAMAGED_BOAT, int(self.joueur1.listeBateau[i].getCoordonneex()),
                                    int(self.joueur1.listeBateau[i].getCoordonneey()) + k)


        print('fin start')
        self.play()

    def play(self):
        pass
