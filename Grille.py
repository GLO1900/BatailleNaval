class Grille:
    DEFAULT_SIZE = 10
    DEFAULT_VALUE = 0
    HIT_WATER = 1
    UNDAMAGED_BOAT = 2
    DAMAGED_BOAT = 3

    def __init__(self):
        self.value = []
        for _ in range(Grille.DEFAULT_SIZE):
            self.value.append([Grille.DEFAULT_VALUE for _ in range(Grille.DEFAULT_SIZE)])

    def __str__(self):
        string = ''
        for i in range(Grille.DEFAULT_SIZE):
            for j in range(Grille.DEFAULT_SIZE):
                string += str(self.value[i][j]) + ' '
            string += '\n'
        return string

    def getsize(self):
        return int(len(self.value))

    def get(self, ligne, col):
        return self.value[ligne][col]

    def set(self, val, ligne, col):
        self.value[ligne][col] = val
