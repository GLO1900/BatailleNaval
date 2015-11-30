from Bateau import Bateau
from Grille import Grille
from Joueur import Joueur
from VueGrilleJeff import VueGrilleJeff
from Vuegrille import Vuegrille
from Vuegrille import MyTurtles
import turtle

class Jeu():
    def __init__(self):
        self.listJoueur = []
        #self.mainMenu = VueGrilleJeff()
        #self.vue = Vuegrille()

    def addJoueur(self, nouveauJoueur):
        self.listJoueur += nouveauJoueur

    def getJoueurs(self):
        return self.listJoueur

    def getVue(self):
        return self.vue

if __name__ == "__main__":
    jeu = Jeu()