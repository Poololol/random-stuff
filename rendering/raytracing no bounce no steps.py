import pygame
import numpy
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
        self.center = center
        self.radius = radius
        self.color = color
    def intersection(self, pos):
        return (pos[0]-self.centerX)**2+(pos[1]-self.centerY)**2+(pos[2]-self.centerZ)**2 <= self.radius**2
class Ray():
    def __init__(self, dir: numpy.ndarray, origin: numpy.ndarray) -> None:
        self.dir = dir
        self.origin = origin
class HitInfo():
    def __init__(self, didHit, dst, hitPoint, normal, color) -> None:
        self.didHit = didHit
        self.dst = dst
        self.hitPoint = hitPoint
        self.normal = normal
        self.color = color
    def __str__(self) -> str:
        return f'{self.didHit}, {self.dst}, {self.hitPoint}'
def RaySphere(ray: Ray, sphere: Sphere):
    hitInfo=HitInfo(False, 0, 0, 0, (0,0,0))
    offsetRayOrigin = ray.origin - sphere.center
    color = sphere.color
    #a = numpy.dot(ray.dir,ray.dir)
    a = 1
    b = 2 * (offsetRayOrigin @ ray.dir)
    c = (offsetRayOrigin @ offsetRayOrigin) - sphere.radius**2
    discriminant = b*b - 4 * a * c
    if discriminant >= 0:
        dst = (-b - math.sqrt(discriminant)) / (2*a)
        if dst >= 0:
            hitInfo = HitInfo(True, dst, ray.origin+ray.dir*dst, 1, color)
    return hitInfo
def sorter(input):
    return input.center[2]
objects = []
angles = []
t1 = time.time()
print((200-250)**2+(200-250)**2+(100-300)**2 <= 250**2)
for angle in range(numRaysPerPixel):
    if maxAngleDifference != 0:
        angles.append(((random.random()-.5)*maxAngleDifference*2, (random.random()-.5)*maxAngleDifference*2))
    else:
        angles.append((0,0,1))
#rx,ry,rz = 0,0,0
#print(rx,ry,rz)
objects.append(Sphere(numpy.array([100, 400, 250]), 150, utils.blue))
objects.append(Sphere([250, 250, 300], 150, utils.red))
i=0
maxpos=0
pri = False
objects = sorted(objects, key=sorter, reverse=True)
for x in range(screenSize[0]):
    for y in range(screenSize[1]):
        for rayNum in range(numRaysPerPixel):
            ray = Ray(numpy.array(angles[rayNum]), numpy.array((x,y,0)))
            for object in objects:
                result = RaySphere(ray, object).color
                if result != (0,0,0):
                    #print(result)
                    pixels[x][y][0] = result[0]
                    pixels[x][y][1] = result[1]
                    pixels[x][y][2] = result[2]
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