import pygame
from datetime import datetime
screen = pygame.display.set_mode((200, 33))
screenSize = screen.get_size()
clock = pygame.time.Clock()
pygame.font.init()
myFont = pygame.font.Font(None, 40)
full = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_f:
                if full == 0:
                    pygame.display.set_mode((120, 33), pygame.NOFRAME)
                    full = 1
                else:
                    pygame.display.set_mode((200, 33))
                    full = 0
    screenSize = screen.get_size()
    pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
    now = datetime.now()
    currentTime = now.strftime("%I:%M:%S")
    time = myFont.render(currentTime, True, (255,255,255))
    screen.blit(time, (screenSize[0]/2-(time.get_width()/2), screenSize[1]/2-(time.get_height()/2)))
    pygame.display.update()
    clock.tick(60)