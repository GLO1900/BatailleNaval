class Bateau():
    def __init__(self, orientation,longueur, coordonnee):
        self.orientation = orientation
        self.longueur = longueur
        self.coordonnee = coordonnee

    def setOrientation(self, paramorientation):
        self.orientation = paramorientation

    def getOrientation(self):
        return self.orientation

    def setLongueur(self, paramlongueur):
        self.longueur = paramlongueur

    def getlongueur(self):
        return self.longueur

    def setCoordonnee(self, paramcoordonnee):
        self.coordonnee = paramcoordonnee

    def getCoordonnee(self):
        return self.coordonnee
    def test(self):
        return None