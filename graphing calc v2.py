import pygame
import math
import numpy
import utils
pygame.display.init()
screen = pygame.display.set_mode((501, 501), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font(None, 20)
lineColor = [222,0,222]
axesColor = [255,255,255]
backgroundColor = [0,0,0]
screenSize = screen.get_size()
xMax = int(5)
xMin = int(-5)
yMax = int(5)
yMin = int(-5)
resolution = (xMax-xMin)/10000
zoom = 0
def Update(xMin: float, xMax: float, yMin: float, yMax: float, screenSize: tuple[int, int], axisColor: pygame.Color, lineColor: pygame.Color, zoom: int, antialiasing = False):
    yVals: list[tuple[float, float, pygame.Color]] = []
    locs = [[backgroundColor for _ in range(screenSize[0])] for _ in range(screenSize[1]+1)]
    if zoom < 0:
        xMin *= -zoom
        xMax *= -zoom
        yMin *= -zoom
        yMax *= -zoom
    elif zoom > 0:
        xMin /= zoom
        xMax /= zoom
        yMin /= zoom
        yMax /= zoom
    resolution = (xMax-xMin)/10000
    for y in range(screenSize[1]):
        locs[int(screenSize[0]/2)][y] = axisColor
    for x in range(screenSize[0]):
        locs[x][int(screenSize[1]/2)] = axisColor
    for x in numpy.arange(xMin, xMax, resolution):
        yVals.append((utils.remap(xMin, xMax, 0, screenSize[0]-1, x), utils.remap(yMin, yMax, 0, screenSize[1], math.sin(math.pi/2*math.cos(x-math.pi/2))), [0,255,0]))
        #yVals.append((utils.remap(xMin, xMax, 0, screenSize[0]-1, x), utils.remap(yMin, yMax, 0, screenSize[1], math.cos(x)), [255,0,0]))
        #yVals.append((utils.remap(xMin, xMax, 0, screenSize[0]-1, x), utils.remap(yMin, yMax, 0, screenSize[1], 0)))
    for pos in yVals:
        if abs(pos[1])>=screenSize[1]: continue
        if pos[1] <= 0: continue
        #print(pos[0],pos[1])
        if antialiasing:
            for i in range(-1,2):
                for j in range(-1,2):
                    for k in range(3):
                        locs[int(pos[0]+i)][int(screenSize[1]-(pos[1]+j))][k] = (pos[2][k]/(abs(i)+abs(j)+1))
        else:
            locs[int(pos[0])][int(screenSize[1]-pos[1])] = pos[2]
    for x in range(screenSize[0]):
        for y in range(screenSize[1]):
            screen.set_at((x,y), locs[x][y])
Update(xMin, xMax, yMin, yMax, screenSize, axesColor, lineColor, zoom)
while True:
    screenSize = screen.get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEWHEEL:
            zoom += event.dict['y']
            if zoom == 0:
                zoom += event.dict['y']
            Update(xMin, xMax, yMin, yMax, screenSize, axesColor, lineColor, zoom, True)
        if event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            Update(xMin, xMax, yMin, yMax, screenSize, axesColor, lineColor, zoom)
    pygame.display.update()
    #clock.tick(60)