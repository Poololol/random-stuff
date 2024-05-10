import pygame
import pyperclip
pygame.display.init()
windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
pygame.font.init()
myFont = pygame.font.SysFont('Galacticfull.ttf', 100)
clock = pygame.time.Clock()
text = ''
cursorColor = (255,255,255)
timer = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_BACKSPACE:
                if event.mod & pygame.KMOD_CTRL:
                    text = text.rstrip('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
                    text = text.rstrip(''' .,/<>?;'":[]}{|+=_-)(*&^%$#@!`~''')
                else:
                    text = text[:-1]
            elif event.mod == pygame.KMOD_NONE or event.mod & pygame.KMOD_SHIFT:
                text = str.join(text, ['', event.dict['unicode']])
            if event.__dict__['key'] == pygame.K_c:
                if event.mod & pygame.KMOD_CTRL:
                    pyperclip.copy(text)
            if event.__dict__['key'] == pygame.K_v:
                if event.mod & pygame.KMOD_CTRL:
                    text = str.join(text, ['', pyperclip.paste()])
    myFont = pygame.font.SysFont('', 100)
    pygame.draw.rect(screen, (0,0,0), ((0,0),windowSize), width=0)
    renderedText = myFont.render(text, True, (255,255,255))
    screen.blit(renderedText, (10,10))
    pygame.draw.rect(screen, cursorColor, (renderedText.get_width()+15, 10, 5, renderedText.get_height()-5))
    if cursorColor == (255,255,255) and timer == 30:
        cursorColor = (0,0,0)
        timer = 0
    elif timer == 30:
        cursorColor = (255,255,255)
        timer = 0
    timer+=1
    pygame.display.update()
    clock.tick(60)