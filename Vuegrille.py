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
        animationGrille.penup()
        animationGrille.speed(500)
        animationGrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)
        animationGrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
        animationGrille.right(90)

        for i in range(Grille.DEFAULT_SIZE + 1):
            animationGrille.pendown()
            animationGrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationGrille.penup()
            animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN)
            animationGrille.setx(animationGrille.xcor() + DEFAULT_MARGIN)

        animationGrille.setx(-DEFAULT_SCREEN_WIDTH/2 + margin)
        animationGrille.sety(DEFAULT_SCREEN_HEIGHT/2 - margin)
        animationGrille.left(90)
        for i in range(Grille.DEFAULT_SIZE + 1):
            animationGrille.pendown()
            animationGrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationGrille.penup()
            animationGrille.sety(animationGrille.ycor() - DEFAULT_MARGIN)
            animationGrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)

    def getcoords(self, x, y):
        self.screen.onclick(None, btn=1)
        print(x, y)
        grillex = int((x + (DEFAULT_SCREEN_WIDTH/2 - DEFAULT_MARGIN))/DEFAULT_MARGIN)
        grilley = int((y - (DEFAULT_SCREEN_HEIGHT/2 - DEFAULT_MARGIN))/(-DEFAULT_MARGIN))
        print(grillex, grilley)
        self.screen.onclick(self.getcoords, btn=1)
        return (grillex, grilley)
        animationGrille.hideturtle()


class MyTurtles(Turtle):
    def move(self, x, y):
        self.setx(x)
        self.sety(y)

    def changeOrientation(self, x, y):
        self.left(90)

bateau1 = MyTurtles()
bateau1.penup()
bateau1.speed(500)
bateau1.setx(200)
bateau1.sety(200)
bateauun = ((0, 0), (-5, 20), (0, 40), (60, 40), (65, 20), (60, 0))
turtle.addshape('bateauun', bateauun)
bateau1.shape('bateauun')
bateau1.fillcolor('white')
bateau1.penup()
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
bateau2.ondrag(bateau2.move)
bateau2.onrelease(bateau2.changeOrientation, 3)

Vuegrille()
