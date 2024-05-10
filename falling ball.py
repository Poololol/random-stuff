import pygame
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()
ballY = 10
ballVy = 0
gravity = .03
while True:
    screenSize = screen.get_size()
    pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
    pygame.draw.circle(screen, (255,255,255), (int(screenSize[0]/2), ballY), 5)
    ballVy += gravity
    ballY += ballVy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(60)