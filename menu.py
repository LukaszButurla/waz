import pygame_menu
import pygame
import wazz

def wlacz_gre():
    wazz.waz()

def zmienJablka(tekst, ilosc):
    wazz.iloscJablek = ilosc

def main():
    pygame.init()
    oknoGry=pygame.display.set_mode((600,600),0,32)
    pygame.display.set_caption("Gra Wąż")
    menu = pygame_menu.Menu("Gra wąż 3TIE", 600, 600, theme=pygame_menu.themes.THEME_ORANGE)
    menu.add.button("Start", wlacz_gre, background_color = (0,0,0))
    menu.add.selector("Ilość jabłek", [("jedno", 1), ("dwa", 2), ("pięć", 5), ("dziesięć", 10), ("dwadzieścia", 20)], onchange=zmienJablka)   

    menu.mainloop(oknoGry)

main()