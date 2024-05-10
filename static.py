import pygame
import utils
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init
font = pygame.font.Font(None, 20)
screenSize = screen.get_size()
showFPS = False
screenShotKey = pygame.K_F2
FPSKey = pygame.K_f
frame = 0
while True:
    screenSize = screen.get_size()
    pygame.draw.rect(screen, utils.black, ((0,0),screenSize), width=0)
    for x in range(screenSize[0]):
        for y in range(screenSize[1]):
            a = x*y*(274532+frame)
            b = a / (38758+frame) * y
            c = b**5
            d = c%255
            screen.set_at((x, y), (d, d, d))
    if showFPS:
        text = font.render(str(round(clock.get_fps(),1)), True, utils.white)
        screen.blit(text, (0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == screenShotKey:
                utils.TakeScreenshot(screen)
            elif event.__dict__['key'] == FPSKey:
                showFPS = not showFPS
    frame += 1
    pygame.display.update()
    clock.tick(60)