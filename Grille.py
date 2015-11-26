DEFAULT_SIZE = 10
DEFAULT_VALUE = (False, False)

class Grille:
    def __init__(self):
        self.value = []
        for _ in range(DEFAULT_SIZE):
            self.value.append([DEFAULT_VALUE for _ in range(DEFAULT_SIZE)])

    def __str__(self):
        string = ''
        for i in range(DEFAULT_SIZE):
            for j in range(DEFAULT_SIZE):
                string += str(self.value[i][j]) + ' '
            string += '\n'
        return string

    def getsize(self):
        return int(len(self.value))

    def get(self, ligne, col):
        return self.value[ligne][col]

    def set(self, val, ligne, col):
        self.value[ligne][col] = val
