from Grille import Grille
import turtle
from Bateau import Bateau
from Jeu import Jeu


DEFAULT_MARGIN = 40
DEFAULT_SCREEN_WIDTH = 32 * DEFAULT_MARGIN
DEFAULT_SCREEN_HEIGHT = 12 * DEFAULT_MARGIN
SPEED = 0


class Vuegrille:
    def __init__(self):

        self.screen = turtle.Screen()
        self.screen.title("Bataille Navale")
        self.screen.listen()
        self.screen.onclick(self.getcoords, btn=1)
        self.setScreenSize(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.setGrille()
        self.setButtons()
        self.jeu = Jeu()
        self.start()
        turtle.done()

    def start(self):

        bateau1 = MyTurtles()
        bateau1.penup()
        bateau1.speed(SPEED)
        bateau1.setx(300)
        bateau1.sety(200)
        bateauun = ((0, 0),

                    ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                    (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                    ((DEFAULT_MARGIN * 2) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                    (((DEFAULT_MARGIN * 2) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                    ((DEFAULT_MARGIN * 2) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateauun', bateauun)
        bateau1.shape('bateauun')
        bateau1.penup()
        bateau1.fillcolor('white')
        bateau1.createBateau(2, bateau1.getcoords, "Torpilleur")
        bateau1.ondrag(bateau1.move)
        bateau1.onrelease(bateau1.changeOrientation, 3)

        bateau2 = MyTurtles()
        bateau2.penup()
        bateau2.speed(SPEED)
        bateau2.setx(250)
        bateau2.sety(200)
        bateaudeux = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateaudeux', bateaudeux)
        bateau2.shape('bateaudeux')
        bateau2.fillcolor('red')
        bateau2.penup()
        bateau2.createBateau(3, bateau2.getcoords, "Sous-Marin")
        bateau2.ondrag(bateau2.move)
        bateau2.onrelease(bateau2.changeOrientation, 3)

        bateau3 = MyTurtles()
        bateau3.penup()
        bateau3.speed(SPEED)
        bateau3.setx(350)
        bateau3.sety(200)
        bateautrois = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateautrois', bateautrois)
        bateau3.shape('bateautrois')
        bateau3.fillcolor('yellow')
        bateau3.penup()
        bateau3.createBateau(3, bateau3.getcoords, "Contre-Torpilleur")
        bateau3.ondrag(bateau3.move)
        bateau3.onrelease(bateau3.changeOrientation, 3)

        bateau4 = MyTurtles()
        bateau4.penup()
        bateau4.speed(SPEED)
        bateau4.setx(250)
        bateau4.sety(0)
        bateauquatre = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 4) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 4) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 4) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateauquatre', bateauquatre)
        bateau4.shape('bateauquatre')
        bateau4.fillcolor('black')
        bateau4.penup()
        bateau4.createBateau(3, bateau4.getcoords, "Croiseur")
        bateau4.ondrag(bateau4.move)
        bateau4.onrelease(bateau4.changeOrientation, 3)

        bateau5 = MyTurtles()
        bateau5.penup()
        bateau5.speed(SPEED)
        bateau5.setx(300)
        bateau5.sety(0)
        bateaucinq = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 5) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 5) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 5) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateaucinq', bateaucinq)
        bateau5.shape('bateaucinq')
        bateau5.fillcolor('gray')
        bateau5.penup()
        bateau5.createBateau(3, bateau3.getcoords, "Porte-Avion")
        bateau5.ondrag(bateau5.move)
        bateau5.onrelease(bateau5.changeOrientation, 3)



    def setButtons(self):
        # BOUTON PROTESTER
        boutonP = MyTurtles()
        boutonP.speed(SPEED)
        boutonP.pu()
        boutonP.setx(450)
        boutonP.sety(-160)
        boutonP.pd()
        boutonP.pencolor('goldenrod')
        boutonP.pensize(5)
        boutonP.fillcolor('gray')
        boutonP.begin_fill()

        for i in range(2):
            if (i == 1):
                boutonP.fd(75)
                boutonP.write('Protester', False, 'center', ('Arial', 14, 'bold'))
                boutonP.fd(75)
                boutonP.right(90)
            else:
                boutonP.fd(150)
                boutonP.right(90)
            boutonP.fd(30)
            boutonP.right(90)

        boutonP.end_fill()
        boutonP.hideturtle()

        # BOUTON ATTAQUER
        boutonA = MyTurtles()
        boutonA.speed(SPEED)
        boutonA.pu()
        boutonA.setx(450)
        boutonA.sety(-80)
        boutonA.pd()
        boutonA.pencolor('goldenrod')
        boutonA.pensize(5)
        boutonA.fillcolor('gray')
        boutonA.begin_fill()

        for i in range(2):
            if (i == 1):
                boutonA.fd(75)
                boutonA.write('Attaquer', False, 'center', ('Arial', 14, 'bold'))
                boutonA.fd(75)
                boutonA.right(90)
            else:
                boutonA.fd(150)
                boutonA.right(90)
            boutonA.fd(30)
            boutonA.right(90)

        boutonA.end_fill()
        boutonA.hideturtle()

        # BOUTON RÉPONSE
        boutonR = MyTurtles()
        boutonR.speed(SPEED)
        boutonR.pu()
        boutonR.setx(450)
        boutonR.sety(0)
        boutonR.pd()
        boutonR.pencolor('goldenrod')
        boutonR.pensize(5)
        boutonR.fillcolor('gray')
        boutonR.begin_fill()

        for i in range(2):
            if (i == 1):
                boutonR.fd(75)
                boutonR.write('Répondre', False, 'center', ('Arial', 14, 'bold'))
                boutonR.fd(75)
                boutonR.right(90)
            else:
                boutonR.fd(150)
                boutonR.right(90)
            boutonR.fd(30)
            boutonR.right(90)

        boutonR.end_fill()
        boutonR.hideturtle()

        # BOUTON COMMENCER
        boutonC = MyTurtles()
        boutonC.speed(SPEED)
        boutonC.pu()
        boutonC.setx(450)
        boutonC.sety(80)
        boutonC.pd()
        boutonC.pencolor('goldenrod')
        boutonC.pensize(5)
        boutonC.fillcolor('gray')
        boutonC.begin_fill()

        for i in range(2):
            if (i == 1):
                boutonC.fd(75)
                boutonC.write('Commencer', False, 'center', ('Arial', 14, 'bold'))
                boutonC.fd(75)
                boutonC.right(90)
            else:
                boutonC.fd(150)
                boutonC.right(90)
            boutonC.fd(30)
            boutonC.right(90)

        boutonC.end_fill()
        boutonC.onclick(boutonC.creerJeu)



    def setScreenSize(self, largeur, hauteur):
        self.screen.setup(largeur, hauteur)
        self.screen.bgpic("ressources/ocean.gif")

    def setGrille(self):
        animationgrille = turtle.Turtle()
        animationgrille.penup()
        animationgrille.speed(SPEED)
        animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)

        for i in range(2):
            animationgrille.pendown()
            animationgrille.fillcolor('orange')
            animationgrille.begin_fill()
            for i in range(4):
                animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
                animationgrille.right(90)
            animationgrille.end_fill()
            animationgrille.penup()
            animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + 12 * DEFAULT_MARGIN)

        animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)
        animationgrille.right(90)

        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
            animationgrille.setx(animationgrille.xcor() + DEFAULT_MARGIN)

        animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
        animationgrille.left(90)
        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(animationgrille.ycor() - DEFAULT_MARGIN)
            animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + DEFAULT_MARGIN)

        animationgrille.penup()
        animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + 12 * DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
        animationgrille.right(90)

        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
            animationgrille.setx(animationgrille.xcor() + DEFAULT_MARGIN)

        animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + 12 * DEFAULT_MARGIN)
        animationgrille.sety(DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)
        animationgrille.left(90)
        for i in range(Grille.DEFAULT_SIZE + 1):
            animationgrille.pendown()
            animationgrille.forward(DEFAULT_MARGIN * Grille.DEFAULT_SIZE)
            animationgrille.penup()
            animationgrille.sety(animationgrille.ycor() - DEFAULT_MARGIN)
            animationgrille.setx(-DEFAULT_SCREEN_WIDTH / 2 + 12 * DEFAULT_MARGIN)
        animationgrille.hideturtle()

    def getcoords(self, x, y):
        self.screen.onclick(None, btn=1)
        print(x, y)
        grillex = int((x + (DEFAULT_SCREEN_WIDTH / 2 - DEFAULT_MARGIN)) / DEFAULT_MARGIN)
        grilley = int((y - (DEFAULT_SCREEN_HEIGHT / 2 - DEFAULT_MARGIN)) / (-DEFAULT_MARGIN))

        if (x > -11 * DEFAULT_MARGIN):
            grillex -= 11

        print(grillex, grilley, self.getcorner(x, y))
        self.screen.onclick(self.getcoords, btn=1)
        return grillex, grilley

    def getcorner(self, x, y):
        if x >= 0:
            cornerx = ((int(x / DEFAULT_MARGIN)) * DEFAULT_MARGIN)
        else:
            cornerx = ((int(x / DEFAULT_MARGIN) - 1) * DEFAULT_MARGIN)
        if y >= 0:
            cornery = ((int(y / DEFAULT_MARGIN) + 1) * DEFAULT_MARGIN)
        else:
            cornery = ((int(y / DEFAULT_MARGIN)) * DEFAULT_MARGIN)
        return cornerx, cornery




class MyTurtles(turtle.Turtle, Vuegrille):

    def createBateau(self, longueur, coords, nom):
        self.bateau = Bateau(False, longueur, coords, nom)

    def move(self, x, y):
        corner = Vuegrille.getcorner(self, x, y)

        if self.bateau.getOrientation() == False:
            self.setx(corner[0] + DEFAULT_MARGIN / 8)
            self.sety(corner[1] - DEFAULT_MARGIN / 4)
        else:
            self.setx(corner[0] + DEFAULT_MARGIN / 4)
            self.sety(corner[1] + DEFAULT_MARGIN / 8)

    def changeOrientation(self, x, y):

        if (self.bateau.getOrientation() == False):
            self.left(90)
            corner = Vuegrille.getcorner(self, x, y)
            self.setx(corner[0] + DEFAULT_MARGIN / 4)
            self.sety(corner[1] - (DEFAULT_MARGIN - 5))
            self.bateau.setOrientation(True)
        else:
            self.right(90)
            corner = Vuegrille.getcorner(self, x, y)
            self.setx(corner[0] + (DEFAULT_MARGIN / 8))
            self.sety(corner[1] - (DEFAULT_MARGIN / 4))
            self.bateau.setOrientation(False)

Vuegrille()