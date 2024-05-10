import pygame
from playsound import playsound
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
translations = {' ': '  ', 'a':'.-','b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---'}
text = ''
morseText = ''
cursorColor = (255,255,255)
timer = 0
while True:
    screenSize = screen.get_size()
    myFont = pygame.font.SysFont('', 100)
    pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
    renderedText = myFont.render(text, True, (255,255,255))
    screen.blit(renderedText, (10,10))
    renderedMorseText = myFont.render(morseText, True, (255,255,255))
    screen.blit(renderedMorseText, (10,100))
    pygame.draw.rect(screen, cursorColor, (renderedText.get_width()+15, 10, 5, renderedText.get_height()-5))
    text = text.lower()
    morseText = ''
    for letter in text:
        if letter in translations.keys():
            morseText = str.join(morseText, ['', translations[letter]])
            morseText = str.join(morseText, ['', ' '])
        else:
            morseText = str.join(morseText, ['', letter])
            morseText = str.join(morseText, ['', ' '])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_BACKSPACE:
                if event.mod & pygame.KMOD_CTRL:
                    text = text.rstrip('qwertyuiopasdfghjklzxcvbnm')
                    text = text.rstrip(' ')
                else:
                    text = text[:-1]
            else:
                text = str.join(text, ['', event.dict['unicode']])
    if cursorColor == (255,255,255) and timer == 30:
        cursorColor = (0,0,0)
        timer = 0
    elif timer == 30:
        cursorColor = (255,255,255)
        timer = 0
    timer+=1
    pygame.display.update()
    clock.tick(60)