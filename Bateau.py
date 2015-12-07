class Bateau:
    def __init__(self, orientation, longueur, coordonnee, nom):
        self.orientation = orientation
        self.longueur = longueur
        self.coordonnee = coordonnee
        self.nom = nom

    def setOrientation(self, paramorientation):
        self.orientation = paramorientation

    def getOrientation(self):
        return self.orientation

    def setLongueur(self, paramlongueur):
        self.longueur = paramlongueur

    def getLongueur(self):
        return self.longueur

    def setCoordonnee(self, paramcoordonnee):
        self.coordonnee = paramcoordonnee

    def getCoordonneex(self):
        return self.coordonnee[0]

    def getCoordonneey(self):
        return self.coordonnee[1]

    def setNom(self, paramnom):
        self.nom = paramnom

    def getNom(self):
        return self.nom