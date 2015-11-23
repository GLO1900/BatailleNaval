import Grille
import turtle


DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
class Vuegrille:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Bataille Navale")
        self.setScreenSize(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


        turtle.done()

    def setScreenSize(self, largeur, hauteur):
        self.screen.setup(largeur, hauteur)

Vuegrille()
