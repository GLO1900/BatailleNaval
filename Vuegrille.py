import Grille
import turtle


DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
DEFAULT_MARGIN = (DEFAULT_SCREEN_WIDTH // 16)

class Vuegrille:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Bataille Navale")
        self.screen.listen()
        self.screen.onclick(self.getcoords, btn=1)
        self.setScreenSize(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.setGrille()
        turtle.done()

    def setScreenSize(self, largeur, hauteur):
        self.screen.setup(largeur, hauteur)
        self.screen.bgcolor('blue')

    def setGrille(self):
        print(DEFAULT_MARGIN)
        animationGrille = turtle.Turtle()
        animationGrille.speed(500)
        animationGrille.penup()
        animationGrille.setx(-DEFAULT_SCREEN_WIDTH/2 + DEFAULT_MARGIN)
        animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
        animationGrille.right(90)

        for i in range(Grille.DEFAULT_SIZE + 1):
            animationGrille.pendown()
            animationGrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationGrille.penup()
            animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
            animationGrille.setx(animationGrille.xcor() + DEFAULT_MARGIN)

        animationGrille.setx(-DEFAULT_SCREEN_WIDTH/2 + DEFAULT_MARGIN)
        animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
        animationGrille.left(90)
        for i in range(Grille.DEFAULT_SIZE + 1):
            animationGrille.pendown()
            animationGrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationGrille.penup()
            animationGrille.sety(animationGrille.ycor() - DEFAULT_MARGIN)
            animationGrille.setx(-DEFAULT_SCREEN_WIDTH/2 + DEFAULT_MARGIN)

    def getcoords(self, x, y):
        self.screen.onclick(None, btn=1)
        print(x, y)
        grillex = int((x + (DEFAULT_SCREEN_WIDTH/2 - DEFAULT_MARGIN))/DEFAULT_MARGIN)
        grilley = int((y - (DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN))/(-DEFAULT_MARGIN))
        print(grillex, grilley)
        self.screen.onclick(self.getcoords, btn=1)
        return (grillex, grilley)

    def getcorner(self, x, y):
        return (getcoords(x, y)[0])
Vuegrille()