import pygame

class WazKlasa:
    def __init__(self):
        self.pozycje = [(400, 400)]
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
        noweWspolrzedne = self.check_border(zmiennaX,zmiennaY)
        self.pozycje.append(noweWspolrzedne)
        if len(self.pozycje) > self.dlugosc:
            del self.pozycje[0]

    def check_border(self, zmiennaX, zmiennaY):
        if zmiennaY < 0:
            zmiennaY = 760        
        if zmiennaY > 760:
            zmiennaY = 0
        if zmiennaX < 0:
            zmiennaX = 760
        if zmiennaX > 760:
            zmiennaX = 0
        return (zmiennaX, zmiennaY)

    def snakeDraw(self, oknoGry):
        for pos in self.pozycje[::-1]:
            ksztaltWaz = pygame.Rect((pos[0], pos[1]), (40, 40))
            pygame.draw.rect(oknoGry, (100, 100, 100), ksztaltWaz)
