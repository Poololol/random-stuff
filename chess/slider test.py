import utils
import pygame
screen = pygame.display.set_mode((500,500))
clock =pygame.time.Clock()
pygame.font.init()
x=50
while True:
    pygame.draw.rect(screen, (0,0,0), (0,0,500,500), width=0)
    percent, x=utils.Slider(start=15, length=115, x=x, y=50, screen=screen, lineColor=(111,111,111), knobColor=(222,222,222), displayText=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(50)