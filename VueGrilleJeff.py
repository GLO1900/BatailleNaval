import Grille
import turtle

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
DEFAULT_MARGIN = (DEFAULT_SCREEN_WIDTH // 16)

class VueGrilleJeff:

    def __init__(self):

        fen = turtle.Screen()
        fen.title("Ma fenêtre de tortues!")
        fen.setup(width=800, height=600)
        alex = turtle.Turtle()

        alex.forward(50) # avancer de 50 pixels
        alex.left(90)    # tourner de 90° en sens anti-horaire
        alex.forward(30) # avancer de 30 pixels