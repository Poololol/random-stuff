import pygame
import utils
screen = pygame.display.set_mode((500,500), flags=pygame.RESIZABLE)
screenSize = screen.get_size()
clock = pygame.time.Clock()
while True:
    pygame.draw.rect(screen, utils.black, ((0,0), screenSize))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(60)