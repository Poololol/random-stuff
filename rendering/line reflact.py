import pygame
import utils
from math import cos,sin,radians
import copy
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
numRaySteps = 1000
pos = [10, 10]
hitPos = [10,10]
angle = -45
prevAngle = 1
lineHeight = 50
def AdvanceRay(pos, angle):
    pos[0] += cos(radians(angle))
    pos[1] += sin(radians(angle))
    return pos
while True:
    screenSize = screen.get_size()
    mouseDown = pygame.mouse.get_pressed()[0]
    pygame.draw.rect(screen, utils.black, ((0,0),screenSize))
    pygame.draw.line(screen, utils.white, (0,screenSize[1]-lineHeight), (screenSize[0], screenSize[1]-lineHeight))
    if angle != prevAngle or lineHeight != prevLineHeight:
        pos = [10,10]
        hitPos = [10,10]
        if angle < 0:
            angle = -angle
        for step in range(numRaySteps):
            pos = AdvanceRay(pos, angle)
            if pos[1] >= screenSize[1]-lineHeight:
                hitPos = copy.deepcopy(pos)
                angle = -copy.copy(angle)
                prevAngle = copy.deepcopy(angle)
                prevLineHeight = copy.copy(lineHeight)
    pygame.draw.line(screen, utils.lightGray, (10,10), hitPos, width=1)
    pygame.draw.line(screen, utils.lightGray, hitPos, pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        angle -= 1
    elif keys[pygame.K_d]:
        angle += 1
    if keys[pygame.K_w]:
        lineHeight += 1
    elif keys[pygame.K_s]:
        lineHeight -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(60)