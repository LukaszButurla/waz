import random

class Jablko():
    def __init__(self):
        self.pozycja = [(1,1)]
        self.randomPosition()
        self.getPosition()

    def randomPosition(self):
        jablkoX=random.randint(0,19)*30
        jablkoY=random.randint(0,19)*30

        

    def getPosition(self):
        return self.pozycja[-1]

    def setPosition(self, x, y):
        self.pozycja = (x, y)