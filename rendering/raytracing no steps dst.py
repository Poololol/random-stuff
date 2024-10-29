import pygame
import numpy
from math import cos, sin, radians
import math
import utils
import random
import time
import copy
import sys
sys.setrecursionlimit(5000)
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
screenSize = screen.get_size()
rayPos = [0,0,0]
numRaysPerPixel = 1
maxRaySteps = 100
maxAngleDifference = 0
intersecting = False
maxRayBounces = 1
backgroundColor = [0, 0, 0]
prevBackgroundColor = backgroundColor
pixels = [[copy.copy(backgroundColor) for i in range(screenSize[0])] for i in range(screenSize[1])]
class Sphere():
    def __init__(self, center, radius, color) -> None:
        self.center = center
        self.radius = radius
        self.color = color
class Ray():
    def __init__(self, origin: numpy.ndarray, numBounces: int, maxBounces: int, *, dir: numpy.ndarray = [], angles: list[int] = numpy.array([])) -> None:
        if dir.__class__ == list:
            self.dir = VectorFromAngles(angles)
        else:
            self.dir = dir
        if angles.__class__ == numpy.ndarray:
            pass
        else:
            self.angles = angles
        self.origin = origin
        self.bounces = numBounces
        self.maxBounces = maxBounces
class HitInfo():
    def __init__(self, didHit, dst, hitPoint, normal, color) -> None:
        self.didHit = didHit
        self.dst = dst
        self.hitPoint = hitPoint
        self.normal = normal
        self.color = color
    def __str__(self) -> str:
        return f'{self.didHit}, {self.dst}, {self.hitPoint}'
def VectorFromAngles(angles):
    return numpy.array([sin(radians(angles[0])), -cos(radians(angles[0]))*sin(radians(angles[1])), cos(radians(angles[0]))*cos(radians(angles[1]))])
def RaySphere(ray: Ray, sphere: Sphere, seed: float, hitInfo: HitInfo):
    offsetRayOrigin = ray.origin - sphere.center
    color = sphere.color
    #a = numpy.dot(ray.dir,ray.dir)
    a = 1
    #print(offsetRayOrigin, ray.dir, ray.origin, ray.angles)
    b = 2 * (offsetRayOrigin @ ray.dir)
    c = (offsetRayOrigin @ offsetRayOrigin) - sphere.radius**2
    discriminant = b*b - 4 * a * c
    if discriminant >= 0:
        dst = (-b - math.sqrt(discriminant)) / (2*a)
        if dst >= 0:
            hitPoint = copy.deepcopy(ray.origin+ray.dir*dst)
            x1, y1, z1 = hitPoint[0]*2, hitPoint[1]*2, hitPoint[2]*2
            scalar = math.sqrt(x1**2+y1**2+z1**2)
            if hitInfo.color == backgroundColor:
                hitInfo = HitInfo(True, dst, hitPoint, numpy.array([x1/scalar, y1/scalar, z1/scalar]), color)
            else:
                hitInfo = HitInfo(True, dst, hitPoint, numpy.array([x1/scalar, y1/scalar, z1/scalar]), ((color[0]+hitInfo.color[0])/2, (color[1]+hitInfo.color[1])/2, (color[2]+hitInfo.color[2])/2))
            if ray.bounces < ray.maxBounces:
                ray.dir = CalcBounceDir(ray, sphere, hitInfo, seed)
                ray.bounces += 1
                hitInfo = RaySphere(ray, sphere, seed, hitInfo)
    return hitInfo
def CalcBounceDir(ray: Ray, sphere: Sphere, hitInfo: HitInfo, seed: float):
    normal = hitInfo.normal
    vector = VectorFromAngles([seed, Random(seed, seed)])
    dot = numpy.dot(vector, normal)
    if dot < 0:
        sign = -1
    else:
        sign = 1
    vector = numpy.array([vector[0]*sign, vector[1]*sign, vector[2]*sign])
    return vector
def Random(x, y):
    randomNum = (x + 8323) * (y + 3487) * 8273159
    randomNum = randomNum**4
    randomNum = randomNum / 213897
    randomNum = randomNum % 360
    return randomNum
def sorter(input):
    return input.center[2]
objects = []
angles = []
t1 = time.time()
print((200-250)**2+(200-250)**2+(100-300)**2 <= 250**2)
for angle in range(numRaysPerPixel):
    if maxAngleDifference != 0:
        angles.append(((random.random()-.5)*maxAngleDifference*2, (random.random()-.5)*maxAngleDifference*2, 1))
    else:
        angles.append((0,0,0))
#rx,ry,rz = 0,0,0
#print(rx,ry,rz)
objects.append(Sphere(numpy.array([100, 400, 250]), 150, utils.blue))
objects.append(Sphere([250, 250, 300], 150, utils.red))
objects.append(Sphere([400, 75, 150], 125, utils.green))
i=0
maxpos=0
pri = False
objects = sorted(objects, key=sorter, reverse=0)
for x in range(screenSize[0]):
    for y in range(screenSize[1]):
        for rayNum in range(numRaysPerPixel):
            ray = Ray(numpy.array((x,y,0)), 0, maxRayBounces, angles=angles[rayNum])
            for object in objects:
                result = RaySphere(ray, object, Random(x, y), HitInfo(1,1,1,1,[0,0,0])).dst
                if result != 1:
                    pixels[x][y][0] = result
                    pixels[x][y][1] = result
                    pixels[x][y][2] = result
        if y == 350 and x==125:
            pass
t2 = time.time()
timeTaken = round(t2-t1, 2)
timeTakenMins = round(timeTaken/60, 2)
print(timeTaken, timeTakenMins)
pixelsR = []
pixelsG = []
pixelsB = []
for x in range(screenSize[0]):
    for y in range(screenSize[1]):
        pixelsR.append(pixels[x][y][0])
        pixelsG.append(pixels[x][y][1])
        pixelsB.append(pixels[x][y][2])
maxR = max(pixelsR)
maxG = max(pixelsG)
maxB = max(pixelsB)
while True:
    for x in range(screenSize[0]):
        for y in range(screenSize[1]):
            if pixels[x][y] == prevBackgroundColor:
                pixels[x][y] = backgroundColor
            screen.set_at((x, y), (utils.remap(0, maxR, 0, 255, pixels[x][y][0]), utils.remap(0, maxG, 0, 255, pixels[x][y][1]), utils.remap(0, maxB, 0, 255, pixels[x][y][2])))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_F2:
                utils.TakeScreenshot(screen)
            elif event.__dict__['key'] == pygame.K_b:
                prevBackgroundColor = backgroundColor
                backgroundColor = [255,255,255]
    pygame.display.update()
    clock.tick(60)