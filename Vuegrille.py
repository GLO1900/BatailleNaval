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

        self.jeu = Jeu()
        self.listeBateauJoueur1 = []
        self.screen = turtle.Screen()
        self.screen.title("Bataille Navale")
        self.screen.listen()
        self.screen.onclick(self.getcoords, btn=1)
        self.setScreenSize(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.setGrille()
        self.setButtons()
        self.start()
        self.boutonC.onclick(self.creerJeu)
        self.screen.listen()
        self.screen.mainloop()

    def start(self):

        self.bateau1 = MyTurtles()
        self.bateau1.penup()
        self.bateau1.speed(SPEED)
        self.bateau1.setx(300)
        self.bateau1.sety(200)
        bateauun = ((0, 0),

                    ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                    (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                    ((DEFAULT_MARGIN * 2) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                    (((DEFAULT_MARGIN * 2) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                    ((DEFAULT_MARGIN * 2) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateauun', bateauun)
        self.bateau1.shape('bateauun')
        self.bateau1.penup()
        self.bateau1.fillcolor('white')
        self.bateau1.createBateau(2, self.bateau1.getcoords(self.bateau1.xcor(), self.bateau1.ycor()), "Torpilleur")
        self.listeBateauJoueur1.append(self.bateau1.bateau)
        self.bateau1.ondrag(self.bateau1.move)
        self.bateau1.onrelease(self.bateau1.changeOrientation, 3)

        self.bateau2 = MyTurtles()
        self.bateau2.penup()
        self.bateau2.speed(SPEED)
        self.bateau2.setx(250)
        self.bateau2.sety(200)
        bateaudeux = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateaudeux', bateaudeux)
        self.bateau2.shape('bateaudeux')
        self.bateau2.fillcolor('red')
        self.bateau2.penup()
        self.bateau2.createBateau(3, self.bateau2.getcoords(self.bateau2.xcor(), self.bateau2.ycor()), "Sous-Marin")
        self.listeBateauJoueur1.append(self.bateau2.bateau)
        self.bateau2.ondrag(self.bateau2.move)
        self.bateau2.onrelease(self.bateau2.changeOrientation, 3)

        self.bateau3 = MyTurtles()
        self.bateau3.penup()
        self.bateau3.speed(SPEED)
        self.bateau3.setx(350)
        self.bateau3.sety(200)
        bateautrois = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 3) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateautrois', bateautrois)
        self.bateau3.shape('bateautrois')
        self.bateau3.fillcolor('yellow')
        self.bateau3.penup()
        self.bateau3.createBateau(3, self.bateau3.getcoords(self.bateau3.xcor(), self.bateau3.ycor()), "Contre-Torpilleur")
        self.listeBateauJoueur1.append(self.bateau3.bateau)
        self.bateau3.ondrag(self.bateau3.move)
        self.bateau3.onrelease(self.bateau3.changeOrientation, 3)

        self.bateau4 = MyTurtles()
        self.bateau4.penup()
        self.bateau4.speed(SPEED)
        self.bateau4.setx(250)
        self.bateau4.sety(0)
        bateauquatre = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 4) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 4) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 4) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateauquatre', bateauquatre)
        self.bateau4.shape('bateauquatre')
        self.bateau4.fillcolor('black')
        self.bateau4.penup()
        self.bateau4.createBateau(4, self.bateau4.getcoords(self.bateau4.xcor(), self.bateau4.ycor()), "Croiseur")
        self.listeBateauJoueur1.append(self.bateau4.bateau)
        self.bateau4.ondrag(self.bateau4.move)
        self.bateau4.onrelease(self.bateau4.changeOrientation, 3)

        self.bateau5 = MyTurtles()
        self.bateau5.penup()
        self.bateau5.speed(SPEED)
        self.bateau5.setx(300)
        self.bateau5.sety(0)
        bateaucinq = ((0, 0),

                      ((0 - 5), (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      (0, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      ((DEFAULT_MARGIN * 5) - DEFAULT_MARGIN / 2, DEFAULT_MARGIN - DEFAULT_MARGIN / 4),

                      (((DEFAULT_MARGIN * 5) - DEFAULT_MARGIN / 2) + 5, (DEFAULT_MARGIN - DEFAULT_MARGIN / 4) / 2),

                      ((DEFAULT_MARGIN * 5) - DEFAULT_MARGIN / 2, 0))
        turtle.addshape('bateaucinq', bateaucinq)
        self.bateau5.shape('bateaucinq')
        self.bateau5.fillcolor('gray')
        self.bateau5.penup()
        self.bateau5.createBateau(5, self.bateau5.getcoords(self.bateau5.xcor(), self.bateau5.ycor()), "Porte-Avion")
        self.listeBateauJoueur1.append(self.bateau5.bateau)
        self.bateau5.ondrag(self.bateau5.move)
        self.bateau5.onrelease(self.bateau5.changeOrientation, 3)



    def setButtons(self):
        # BOUTON PROTESTER
        self.boutonP = MyTurtles()
        self.boutonP.speed(SPEED)
        self.boutonP.pu()
        self.boutonP.setx(450)
        self.boutonP.sety(-160)
        self.boutonP.pd()
        self.boutonP.pencolor('goldenrod')
        self.boutonP.pensize(5)
        self.boutonP.fillcolor('gray')
        self.boutonP.begin_fill()

        for i in range(2):
            if (i == 1):
                self.boutonP.fd(75)
                self.boutonP.write('Protester', False, 'center', ('Arial', 14, 'bold'))
                self.boutonP.fd(75)
                self.boutonP.right(90)
            else:
                self.boutonP.fd(150)
                self.boutonP.right(90)
            self.boutonP.fd(30)
            self.boutonP.right(90)

        self.boutonP.end_fill()
        self.boutonP.hideturtle()

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
        self.boutonC = MyTurtles()
        self.boutonC.speed(SPEED)
        self.boutonC.pu()
        self.boutonC.setx(450)
        self.boutonC.sety(80)
        self.boutonC.pd()
        self.boutonC.pencolor('goldenrod')
        self.boutonC.pensize(5)
        self.boutonC.fillcolor('gray')
        self.boutonC.begin_fill()

        for i in range(2):
            if (i == 1):
                self.boutonC.fd(75)
                self.boutonC.write('Commencer', False, 'center', ('Arial', 14, 'bold'))
                self.boutonC.fd(75)
                self.boutonC.right(90)
            else:
                self.boutonC.fd(150)
                self.boutonC.right(90)
            self.boutonC.fd(30)
            self.boutonC.right(90)

        self.boutonC.end_fill()
        self.boutonC.shape('square')



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

    def creerJeu(self, x, y):
        self.jeu.start(self.listeBateauJoueur1, self.listeBateauJoueur1)




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

        self.bateau.setCoordonnee(self.getcoords(x, y))

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

v = Vuegrille()