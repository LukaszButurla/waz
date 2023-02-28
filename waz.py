import pygame


def waz():
    pygame.init()
    oknoGry = pygame.display.set_mode((800, 800),0,32)
    pygame.display.set_caption("Snake")
    run = True
    while run:
        oknoGry.fill((0,0,0))
        pygame.time.delay(200)
        for zdarzenia in pygame.event.get():
            if zdarzenia.type==pygame.QUIT:
                run = False

        ksztaltWaz = pygame.Rect((400, 400), (40, 40))
        pygame.draw.rect(oknoGry, (100, 100, 100), ksztaltWaz)

        pygame.display.update()

waz()