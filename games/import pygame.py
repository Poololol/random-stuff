import pygame
import numpy
import random
screen = pygame.display.set_mode(size=(500,500))
screenSize = pygame.display.get_window_size()
numberOfSquares = 9
squareSize = int(min(screenSize)/numberOfSquares)
board = numpy.zeros([10,10])
clock = pygame.time.Clock()
lightGreen = (64, 255, 64)
darkGreen = (0, 200, 0)
red = (200, 0, 0)
playerPosition = (1, int(numberOfSquares/2))
#player = pygame.image.load('player.png').convert_alpha()
#player = pygame.transform.scale(player, (squareSize, squareSize))
playerRect = pygame.Rect((0,0), (squareSize, squareSize))
move = False
direction = 4
speed = .05
applePosition = (6, 4)
length = 1
lose = False
def ColorBoard(x, y, color1, color2):
    if (x+y)%2 == 0:
        pygame.draw.rect(screen, color1, [x*squareSize, y*squareSize, squareSize, squareSize], width=0)
    else:
        pygame.draw.rect(screen, color2, [x*squareSize, y*squareSize, squareSize, squareSize], width=0)
def MovePlayer(position, direction):
    if direction == 0:
        position = (position[0], position[1]-speed)
    elif direction == 1:
        position = (position[0]+speed, position[1])
    elif direction == 2:
        position = (position[0], position[1]+speed)
    elif direction == 3:
        position = (position[0]-speed, position[1])
    return position
def SpawnApple(position):
    return pygame.draw.circle(screen, red, (position[0]*squareSize+squareSize/2, position[1]*squareSize+squareSize/2), squareSize/3, width=0)
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if keys[pygame.K_w] == True:
            if direction != 2:
                direction = 0
                move = True
        elif keys[pygame.K_d] == True:
            if direction != 3:
                direction = 1
                move = True
        elif keys[pygame.K_s] == True:
            if direction != 0:
                direction = 2
                move = True
        elif keys[pygame.K_a] == True:
            if direction != 1:
                direction = 3
                move = True
    for x in range(numberOfSquares):
        for y in range(numberOfSquares):
            ColorBoard(x, y, lightGreen, darkGreen)
    if playerPosition[0] < 0:
        lose = True
    elif playerPosition[0] > numberOfSquares:
        lose = True
    elif playerPosition[1] < 0:
        lose = True
    elif playerPosition[1] > numberOfSquares:
        lose = True
    if move == True:
        playerPosition = MovePlayer(playerPosition, direction)
        playerRect.update(int(playerPosition[0])*squareSize, int(playerPosition[1])*squareSize, squareSize, squareSize)
    apple = SpawnApple(applePosition)
    if pygame.Rect.colliderect(playerRect, apple) == True:
        applePosition = (random.randrange(0, numberOfSquares), random.randrange(0, numberOfSquares))
        length = length + 1
    pygame.draw.rect(screen, (0,0,255), (int(playerPosition[0])*squareSize, int(playerPosition[1])*squareSize, squareSize, squareSize))
    if lose == True:
        pass
    pygame.display.update()
    clock.tick(60)
