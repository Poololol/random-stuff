import pygame
import concurrent.futures
from math import cos, sin, radians
import math
import utils
import random
import time
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
screenSize = screen.get_size()
rayPos = [0,0,0]
numRaysPerPixel = 1
maxRaySteps = 100
maxAngleDifference = 0
intersecting = False
pixels = [[[0,0,0] for i in range(screenSize[0])] for i in range(screenSize[1])]
def AdvanceRay(pos: list[float], angle: list[float]):
    xc = sin(radians(angle[0]))
    yc = sin(radians(angle[1]))
    zc = 1
    #b = (xc**2)+(yc**2)+(zc**2)
    #targetLength = .01
    #scalar = ((1.01469*(x**0.488407))-0.0147947)/b
    #scalar = 1/b
    #scalar = 1
    #offset = [scalar*xc, scalar*yc, scalar*zc]
    pos[0] += xc
    pos[1] += yc
    pos[2] += zc
    return pos
class Sphere():
    def __init__(self, center, radius, color) -> None:
        self.centerX = center[0]
        self.centerY = center[1]
        self.centerZ = center[2]
        self.radius = radius
        self.color = color
    def intersection(self, pos):
        return (pos[0]-self.centerX)**2+(pos[1]-self.centerY)**2+(pos[2]-self.centerZ)**2 <= self.radius**2
objects = []
angles = []
threads = []
t1 = time.time()
print((200-250)**2+(200-250)**2+(100-300)**2 <= 250**2)
for angle in range(numRaysPerPixel):
    if maxAngleDifference != 0:
        angles.append(((random.random()-.5)*maxAngleDifference*2, (random.random()-.5)*maxAngleDifference*2))
    else:
        angles.append((0,0,0))
#rx,ry,rz = 0,0,0
#print(rx,ry,rz)
objects.append(Sphere([100, 400, 0], 150, utils.blue))
objects.append(Sphere([250, 250, 300], 250, utils.red))
i=0
maxpos=0
pri = False
def doray(input, i2,i3,i4):
    x=input
    y=i2
    maxRaySteps=i3
    numRaysPerPixel=i4
    r=0
    g=0
    b=0
    intersecting = False
    i=0
    for ray in range(numRaysPerPixel):
            pos = [x,y,0]
            while not intersecting and i<maxRaySteps:
                pos = AdvanceRay(pos, angles[ray])
                i+=1
                for object in objects:
                    if object.intersection(pos):
                        intersecting = True
                        r += object.color[0]/numRaysPerPixel
                        g += object.color[1]/numRaysPerPixel
                        b += object.color[2]/numRaysPerPixel
            intersecting = False
            pri = False
            i=0
    return r,g,b
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for x in range(screenSize[0]):
        for y in range(screenSize[1]):
            #pixels[x][y] = executor.map(doray, (x,y, maxRaySteps, numRaysPerPixel))
            pixels[x][y] = executor.submit(doray, x, y, maxRaySteps, numRaysPerPixel).result()
            #print(output.result())
t2 = time.time()
timeTaken = round(t2-t1, 2)
timeTakenMins = round(timeTaken/60, 2)
print(timeTaken, timeTakenMins)
while True:
    for x in range(screenSize[0]):
        for y in range(screenSize[1]):
            screen.set_at((x, y), pixels[x][y])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_F2:
                utils.TakeScreenshot(screen)
    pygame.display.update()
    clock.tick(6)