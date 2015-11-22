class Bateau():
    def __init__(self, orientation,longueur, coordonnee, nom):
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

    def getlongueur(self):
        return self.longueur

    def setCoordonnee(self, paramcoordonnee):
        self.coordonnee = paramcoordonnee

    def getCoordonnee(self):
        return self.coordonnee

    def setNom(self, paramnom):
        self.nom = paramnom

    def getNom(self):
        return self.nom