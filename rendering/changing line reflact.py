import pygame
import utils
from math import cos,sin,radians,atan,degrees
import copy
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
numRaySteps = 100
pos = [250, 490]
hitPos = [250, 490]
angle = -90
unAngle = -90
prevAngle = -90
lineHeight1 = 50
lineHeight2 = 50
prevLineHeight = 50
def AdvanceRay(pos, angle):
    pos[0] += cos(radians(angle))*5
    pos[1] += sin(radians(angle))*5
    return pos
while True:
    screenSize = screen.get_size()
    mouseDown = pygame.mouse.get_pressed()[0]
    pygame.draw.rect(screen, utils.black, ((0,0),screenSize))
    pygame.draw.line(screen, utils.white, (0,lineHeight1), (screenSize[0], lineHeight2))
    slope = (lineHeight2-lineHeight1)/500
    if angle != prevAngle or lineHeight2 != prevLineHeight:
        print(angle, prevAngle, lineHeight2, prevLineHeight)
        pos = [250, 490]
        hitPos = [250, 490]
        angle = copy.deepcopy(unAngle)
        for step in range(numRaySteps):
            pos = AdvanceRay(pos, angle)
            if pos[1] <= slope*pos[0]+lineHeight1:
                print(slope, slope*pos[0]+lineHeight1, pos[0], pos[1])
                hitPos = copy.deepcopy(pos)
                prevAngle = copy.deepcopy(angle)
                an = copy.deepcopy(degrees(atan(slope)))
                ad = an - 90
                #al = an-ad
                angle = copy.deepcopy(ad)
                #print(angle)
        prevLineHeight = copy.copy(lineHeight2)
    pygame.draw.line(screen, utils.lightGray, (250, 490), hitPos, width=1)
    pygame.draw.line(screen, utils.lightGray, hitPos, pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        angle -= 1
        unAngle = copy.deepcopy(angle)
    elif keys[pygame.K_d]:
        angle += 1
        unAngle = copy.deepcopy(angle)
    if keys[pygame.K_w]:
        lineHeight2 -= 1
    elif keys[pygame.K_s]:
        lineHeight2 += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(60)