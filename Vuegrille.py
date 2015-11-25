import Grille
import turtle

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600


class Vuegrille:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Bataille Navale")

        self.setScreenSize(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.setGrille()
        turtle.done()

    def setScreenSize(self, largeur, hauteur):
        self.screen.setup(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, None, None)
        self.screen.bgcolor('blue')

    def setGrille(self):
        margin = (DEFAULT_SCREEN_WIDTH // 20)
        print(margin)
        animationGrille = turtle.Turtle()
        animationGrille.penup()
        animationGrille.setx(-DEFAULT_SCREEN_WIDTH/2 + margin)
        animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - margin)
        animationGrille.right(90)

        for i in range(Grille.DEFAULT_SIZE + 1):
            animationGrille.pendown()
            animationGrille.forward(margin * Grille.DEFAULT_SIZE)
            animationGrille.penup()
            animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - margin)
            animationGrille.setx(animationGrille.xcor() + margin)

        animationGrille.setx(-DEFAULT_SCREEN_WIDTH/2 + margin)
        animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - margin)
        animationGrille.left(90)
        for i in range(Grille.DEFAULT_SIZE + 1):
            animationGrille.pendown()
            animationGrille.forward(margin * Grille.DEFAULT_SIZE)
            animationGrille.penup()
            animationGrille.sety(animationGrille.ycor() - margin)
            animationGrille.setx(-DEFAULT_SCREEN_WIDTH/2 + margin)


Vuegrille()
