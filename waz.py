import pygame
import random
from snake import Waz

def waz():
    pygame.init()
    oknoGry = pygame.display.set_mode((800, 800),0,32)
    pygame.display.set_caption("Snake")
    run = True
    zmiennaX = 400
    zmiennaY = 400
    pozycjaWaz = [(zmiennaX, zmiennaY)]
    dlugoscWaz = 1
    jablkoX = random.randint(0, 19) * 40
    jablkoY = random.randint(0, 19) * 40
    score = 0    
    kierunek = [1, 0]
    
    while run:
        oknoGry.fill((0,0,0))
        pygame.time.delay(200)


        for zdarzenia in pygame.event.get():
            if zdarzenia.type==pygame.QUIT:
                run = False
            elif zdarzenia.type==pygame.KEYDOWN:

                match(zdarzenia.key):
                    case pygame.K_DOWN:
                            kierunek = [0, 1]
                    case pygame.K_LEFT:
                            kierunek = [-1, 0]
                    case pygame.K_RIGHT:
                            kierunek = [1, 0]
                    case pygame.K_UP:
                            kierunek = [0, -1]

        zmiennaX = zmiennaX+kierunek[0]*40
        zmiennaY = zmiennaY+kierunek[1]*40

        if zmiennaY < 0:
            zmiennaY = 760        
        if zmiennaY > 760:
            zmiennaY = 0
        if zmiennaX < 0:
            zmiennaX = 760
        if zmiennaX > 760:
            zmiennaX = 0

        pozycjaWaz.append((zmiennaX, zmiennaY))

        if len(pozycjaWaz)>dlugoscWaz:
            del pozycjaWaz[0]

            


        if zmiennaX==jablkoX and zmiennaY==jablkoY:
            jablkoX = random.randint(0, 19) * 40
            jablkoY = random.randint(0, 19) * 40
            score += 1
            dlugoscWaz +=1

        ksztaltJablko = pygame.draw.circle(oknoGry, (255, 0, 0), (jablkoX + 20, jablkoY + 20), 20)
        czcionka = pygame.font.SysFont("Arial", 25)
        tekst = czcionka.render("Zdobyte puknty: {}".format(score), 1, (150, 200, 75))
        oknoGry.blit(tekst, (10, 10))

        for pos in pozycjaWaz[::-1]:
            ksztaltWaz = pygame.Rect((pos[0], pos[1]), (40, 40))
            pygame.draw.rect(oknoGry, (100, 100, 100), ksztaltWaz)

        pygame.display.update()

waz()