import pygame
import utils
import random
import math
import numpy
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
screenSize = screen.get_size()
randomNum = random.random()
randomNum2 = random.random()
frame = 0
def Fun(rayorigin: numpy.ndarray, rayangle: list[int], spherecenter: numpy.ndarray, sphereradius: int):
    hitPoint = [10, 0]
    raydir = numpy.array([math.cos(math.radians(rayangle[0])), math.sin(math.radians(rayangle[0]))])
    offsetRayOrigin = rayorigin - spherecenter
    a = 1
    b = 2 * (offsetRayOrigin @ raydir)
    c = (offsetRayOrigin @ offsetRayOrigin) - sphereradius**2
    discriminant = b*b - 4 * a * c
    if discriminant >= 0:
        dst = (-b - math.sqrt(discriminant)) / (2*a)
        if dst != 28957894275:
            hitPoint = rayorigin+raydir*dst
            normal = numpy.array([0,1])
    #print(hitPoint)
    if hitPoint[0] == 10 and hitPoint[1] == 0:
        if abs(rayangle[0]) >10:
            print(rayangle)
    return hitPoint
def CalculateBounceDir(ray, random):
    angle = random*180-90
    return [-angle]
while True:
    screenSize = screen.get_size()
    pygame.draw.rect(screen, utils.black, ((0,0),screenSize), width=0)
    pygame.draw.circle(screen, utils.white, (screenSize[0]/2, screenSize[1]*50), screenSize[1]*49.2, width=1)
    pygame.draw.circle(screen, utils.white, (screenSize[0]/2, screenSize[1]*-49.1), screenSize[1]*49.2, width=1)
    hitPoint = Fun(numpy.array((50,50)), [45], numpy.array((screenSize[0]/2, screenSize[1]*50)), screenSize[1]*49.2)
    pygame.draw.line(screen, utils.white, (50,50), hitPoint, width=1)
    hitPoint2 = Fun(hitPoint, CalculateBounceDir([], randomNum), numpy.array((screenSize[0]/2, screenSize[1]*-49.1)), screenSize[1]*49.2)
    '''if randomNum2 >= .5:
        hitPoint2[0] += hitPoint[0]-hitPoint2[0]'''
    pygame.draw.line(screen, utils.red, hitPoint, hitPoint2, width=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_r:
                pass
    #if frame % 3 == 0:
                randomNum = random.random()
                #randomNum2 = random.random()
    frame += 1
    pygame.display.update()
    clock.tick(60)