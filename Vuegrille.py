from Grille import Grille
import turtle
from Bateau import Bateau

DEFAULT_SCREEN_WIDTH = 1200
DEFAULT_SCREEN_HEIGHT = 620
DEFAULT_MARGIN = (DEFAULT_SCREEN_WIDTH // 25)


class Vuegrille:

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Bataille Navale")
        self.screen.listen()
        self.screen.onclick(self.getcoords, btn=1)
        self.setscreensize(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.setgrille()
        turtle.done()

    def setscreensize(self, largeur, hauteur):
        self.screen.setup(largeur, hauteur)
        self.screen.bgcolor("blue")

    def setgrille(self):
        animationgrille = turtle.Turtle()
        animationgrille.penup()
        animationgrille.speed(100)
        animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
        animationgrille.right(90)

        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
            animationgrille.setx(animationgrille.xcor() + DEFAULT_MARGIN)

        animationgrille.setx(-DEFAULT_SCREEN_WIDTH/2 + DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
        animationgrille.left(90)
        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(animationgrille.ycor() - DEFAULT_MARGIN)
            animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)

        animationgrille.penup()
        animationgrille.setx(DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
        animationgrille.right(90)

        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
            animationgrille.setx(animationgrille.xcor() + DEFAULT_MARGIN)

        animationgrille.setx(DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
        animationgrille.left(90)
        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(animationgrille.ycor() - DEFAULT_MARGIN)
            animationgrille.setx(DEFAULT_MARGIN)
        animationgrille.hideturtle()
        b1 = turtle.Turtle()
        b1.penup()
        b1.setx(0)
        b1.sety(0)
        b2x1 = ((0, 0), (2*DEFAULT_MARGIN, 0), (2*DEFAULT_MARGIN, DEFAULT_MARGIN), (0, DEFAULT_MARGIN))
        turtle.addshape('b2x1', b2x1)
        b1.shape('b2x1')
        b1.color('black')
        b1.ondrag(b1.goto)

    def getcoords(self, x, y):
        self.screen.onclick(None, btn=1)
        print(x, y)
        grillex = int((x + (DEFAULT_SCREEN_WIDTH/2 - DEFAULT_MARGIN))/DEFAULT_MARGIN)
        grilley = int((y - (DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN))/(-DEFAULT_MARGIN))
        print(grillex, grilley, self.getcorner(x, y))
        self.screen.onclick(self.getcoords, btn=1)
        return grillex, grilley

    def getcorner(self, x, y):
        if x >= 0:
            cornerx = ((int(x/DEFAULT_MARGIN))*DEFAULT_MARGIN)
        else:
            cornerx = ((int(x/DEFAULT_MARGIN)+1)*DEFAULT_MARGIN)
        if y and x <= 0:
            cornery = ((int(y/DEFAULT_MARGIN)+1)*DEFAULT_MARGIN)
        else:
            cornery = ((int(y/DEFAULT_MARGIN))*DEFAULT_MARGIN)
        return cornerx, cornery


class MyTurtles(turtle.Turtle, Vuegrille):

    def createBateau(self, longueur, coords, nom):
        self.bateau = Bateau(False, longueur, coords, nom)

    def move(self, x, y):
        corner = Vuegrille.getcorner(self, x, y)

        if(self.bateau.getOrientation() == False):
            self.setx(corner[0] + DEFAULT_MARGIN / 8)
            self.sety(corner[1] - DEFAULT_MARGIN / 2)
        else:
            self.setx(corner[0] + DEFAULT_MARGIN / 2)
            self.sety(corner[1] + DEFAULT_MARGIN / 8)

    def changeOrientation(self, x, y):

        if (self.bateau.getOrientation() == False):
            self.left(90)
            corner = Vuegrille.getcorner(self, x, y)
            self.setx(corner[0] + 20)
            self.sety(corner[1] - 45)
            self.bateau.setOrientation(True)
        else:
            self.right(90)
            corner = Vuegrille.getcorner(self, x, y)
            self.setx(corner[0] + 5)
            self.sety(corner[1] - 20)
            self.bateau.setOrientation(False)

bateau1 = MyTurtles()
bateau1.penup()
bateau1.speed(500)
bateau1.setx(0)
bateau1.sety(0)
bateauun = ((0, 0), (-5, 20), (0, 40), (60, 40), (65, 20), (60, 0))
turtle.addshape('bateauun', bateauun)
bateau1.shape('bateauun')
bateau1.penup()
bateau1.fillcolor('white')
bateau1.createBateau(2, bateau1.getcoords, "Torpilleur")
bateau1.ondrag(bateau1.move)
bateau1.onrelease(bateau1.changeOrientation, 3)

bateau2 = MyTurtles()
bateau2.penup()
bateau2.speed(500)
bateau2.setx(250)
bateau2.sety(200)
bateaudeux = ((0, 0), (-5, 20), (0, 40), (100, 40), (105, 20), (100, 0))
turtle.addshape('bateaudeux', bateaudeux)
bateau2.shape('bateaudeux')
bateau2.fillcolor('red')
bateau2.penup()
bateau2.createBateau(3, bateau2.getcoords, "Blazeit")
bateau2.ondrag(bateau2.move)
bateau2.onrelease(bateau2.changeorientation, 3)

Vuegrille()
