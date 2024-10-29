import utils
import pygame
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
while True:
    screenSize = screen.get_size()
    utils.dithering(pygame.Rect((0,0),screenSize), screen, (255,0,0), (0,0,255), 0, 'V')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(60)
