import pygame
import utils
screen = pygame.display.set_mode((1100,550), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init
font = pygame.font.Font(None, 20)
screenSize = screen.get_size()
showFPS = False
screenshotKey = pygame.K_F2
FPSKey = pygame.K_f
gridSize = 50
ship = 1
ships = [(5, utils.gray), (4, utils.lightGray), (3, utils.darkGray), (3, utils.blue), (2, utils.lightBlue)]
shipPlacements = []
hits = []
misses = []
direction = 0
while True:
    screenSize = screen.get_size()
    mousePos = pygame.mouse.get_pos()
    mouseTile = (int(mousePos[0]/gridSize), int(mousePos[1]/gridSize))
    mouse = pygame.Rect(mousePos, (0,0))
    pygame.draw.rect(screen, utils.black, ((0,0),screenSize), width=0)
    for i in range(22):
        if i%11 != 0:
            text = font.render(str(i%11), True, utils.white)
            screen.blit(text, ((i+.5)*gridSize-text.get_width()/2, gridSize/2-text.get_height()/2))
        for j in range(11):
            if (i%11 == 0) and (j%11 != 0):
                letter = utils.alphabet[j%11-1]
                text = font.render(letter, True, utils.white)
                pos = (i+.5)*gridSize-text.get_width()/2, (j+.5)*gridSize-text.get_height()/2
                screen.blit(text, pos)
                #print(letter, pos, i, j)
            if mouseTile[0]>11 and mouseTile[1]>0:
                tile = (i,j)
                if ship:
                    if direction == 0 and mouseTile[0]<23-ships[ship-1][0]:
                        for o in range(ships[ship-1][0]):
                            if tile == (mouseTile[0]+o, mouseTile[1]):
                                pygame.draw.rect(screen, ships[ship-1][1], (i*gridSize, j*gridSize, gridSize, gridSize), width=0)
                    elif direction == 1 and mouseTile[1]<12-ships[ship-1][0]:
                        for o in range(ships[ship-1][0]):
                            if tile == (mouseTile[0], mouseTile[1]+o):
                                pygame.draw.rect(screen, ships[ship-1][1], (i*gridSize, j*gridSize, gridSize, gridSize), width=0)
                    elif direction == 2 and mouseTile[0]>10+ships[ship-1][0]:
                        for o in range(ships[ship-1][0]):
                            if tile == (mouseTile[0]-o, mouseTile[1]):
                                pygame.draw.rect(screen, ships[ship-1][1], (i*gridSize, j*gridSize, gridSize, gridSize), width=0)
                    elif direction == 3 and mouseTile[1]>ships[ship-1][0]-1:
                        for o in range(ships[ship-1][0]):
                            if tile == (mouseTile[0], mouseTile[1]-o):
                                pygame.draw.rect(screen, ships[ship-1][1], (i*gridSize, j*gridSize, gridSize, gridSize), width=0)
            if i%11 != 0 or j != 0:
                pygame.draw.rect(screen, utils.white, (i*gridSize, j*gridSize, gridSize, gridSize), width=1)
    if showFPS:
        text = font.render(str(round(clock.get_fps(),1)), True, utils.white)
        screen.blit(text, (0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == screenshotKey:
                utils.TakeScreenshot(screen)
            if event.__dict__['key'] == FPSKey:
                showFPS = not showFPS
            if event.__dict__['key'] == pygame.K_r:
                direction+=1
                direction%=4
        if event.type == pygame.MOUSEBUTTONDOWN:
            ship+=1
    pygame.display.update()
    clock.tick(60)
