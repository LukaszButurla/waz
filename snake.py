class WazKlasa:
    def __init__(self):
        self.pozycje = [(300, 300)]
        self.dlugosc = 1
        self.kierunek = [1, 0]
        self.punkty = 0

    def setDirection(self, direction):
        self.kierunek = direction

    def getHeadPosition(self):
        return self.pozycje[-1]

    def snakeMove(self):
        ostatniaPozycja = self.getHeadPosition()

        zmiennaX = ostatniaPozycja[0]+self.kierunek[0]*40
        zmiennaY = ostatniaPozycja[1]+self.kierunek[1]*40

