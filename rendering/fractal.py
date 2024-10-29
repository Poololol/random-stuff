import pygame
import utils
import cmath
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
screenSize = screen.get_size()
clock = pygame.time.Clock()
insideColor = utils.Coordinate(0,0,0)
color = utils.Coordinate(.35/100, .5/100, 1/100)*5
c = complex(.48, .58)
def calc(x, y):
    x = utils.remap(0, screenSize[0], -2.5, 1.75, x)
    y = utils.remap(0, screenSize[1], -1.75, 1.75, screenSize[1]-y)
    z = complex(x,y)
    iteration = 0
    maxIters = 100
    if abs(x)<=0.001 and abs(y)<=0.001:
        return utils.Coordinate(1,1,1)
    while abs(z)<4 and iteration<maxIters:
        z = (z.conjugate()**2)+c
        iteration+=1
    if iteration==maxIters:
        return insideColor
    return color*iteration
colors = [[i for i in range(screenSize[1])] for i in range(screenSize[0])]
for x in range(screenSize[0]):
    for y in range(screenSize[1]):
        colors[x][y] = calc(x,y).toColor()
while True:
    pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
    for x in range(screenSize[0]):
        for y in range(screenSize[1]):
            screen.set_at((x,y), colors[x][y])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            colors = [[i for i in range(screenSize[1])] for i in range(screenSize[0])]
            for x in range(screenSize[0]):
                for y in range(screenSize[1]):
                    colors[x][y] = calc(x,y).toColor()
    pygame.display.update()
    clock.tick(60)