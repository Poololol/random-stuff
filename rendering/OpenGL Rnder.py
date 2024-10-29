import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import PIL.Image as im
import copy
import numpy
import math
#verticies = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))
colors = ((0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0))
surfaces = ((0,1,2,3), (3,2,7,6), (6,7,5,4), (4,5,1,0), (1,5,7,2), (4,0,3,6))
def Cube(corner, size):
    vertices = ((corner[0]+size, corner[1], corner[2]), (corner[0]+size, corner[1]+size, corner[2]), (corner[0], corner[1]+size, corner[2]), (corner[0], corner[1], corner[2]), (corner[0]+size, corner[1], corner[2]+size), (corner[0]+size, corner[1]+size, corner[2]+size), (corner[0], corner[1], corner[2]+size), (corner[0], corner[1]+size, corner[2]+size))
    glBegin(GL_LINES)
    glColor((1,1,1))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
        x+=1
    glEnd()
def rotateY(angle, cameraAngles):
    alpha = math.radians(cameraAngles[0]+90)
    beta = math.radians(cameraAngles[1]*0)
    x = math.sin(-beta) * math.cos(alpha)
    y = math.sin(alpha)
    z = math.cos(beta) * math.cos(alpha)
    #glTranslatef(x/10,y/10,z/10)
    glRotatef(-angle,x,y,z)
def rotateX(angle, cameraAngles):
    alpha = math.radians(cameraAngles[0]*0)
    beta = math.radians(cameraAngles[1]+90)
    x = math.sin(-beta) * math.cos(alpha)
    y = math.sin(alpha)
    z = math.cos(beta) * math.cos(alpha)
    #glTranslatef(x/10,y/10,z/10)
    glRotatef(-angle,x,y,z)
pygame.init()
clock = pygame.time.Clock()
display = (800,600)
screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)
screenSize = screen.get_size()
font = pygame.font.Font(None, 10)
glLineWidth(2)
gluPerspective(80, (screenSize[0]/screenSize[1]), 0.1, 100.0)
glTranslatef(0.0,0.0, -6)
cameraAngle = numpy.array([0.0, 0.0, 0.0])
prevCameraAngle = [0,0,0]
move = 0
off = 0
ofz = 0
showFPS = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == WINDOWRESIZED:
            screenSize = screen.get_size()
            gluPerspective(80, (screenSize[0]/screenSize[1]), 0.2, 100.0)
            #glTranslatef(0.0,0.0, -5)
        if event.type == KEYDOWN:
            if event.__dict__['key'] == K_f:
                showFPS = not showFPS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] == True:
        alpha = math.radians(cameraAngle[0])
        beta = math.radians(cameraAngle[1])
        x = math.sin(-beta) * math.cos(alpha)
        y = 0
        z = math.cos(beta) * math.cos(alpha)
        glTranslatef(x/10, y/10, z/10)
    elif keys[pygame.K_s] == True:
        alpha = math.radians(-cameraAngle[0])
        beta = math.radians(cameraAngle[1]+180)
        x = math.sin(-beta) * math.cos(alpha)
        y = 0
        z = math.cos(beta) * math.cos(alpha)
        glTranslatef(x/10, y/10, z/10)
    if keys[pygame.K_d] == True:
        alpha = math.radians(cameraAngle[0]*0)
        beta = math.radians(cameraAngle[1]+90)
        x = math.sin(-beta) * math.cos(alpha)
        y = math.sin(alpha)
        z = math.cos(beta) * math.cos(alpha)
        dire = [x/10,y/10,z/10]
        glTranslatef(dire[0], dire[1], dire[2])
    elif keys[pygame.K_a] == True:
        alpha = math.radians(cameraAngle[0]*0)
        beta = math.radians(cameraAngle[1]-90)
        x = math.sin(-beta) * math.cos(alpha)
        y = math.sin(alpha)
        z = math.cos(beta) * math.cos(alpha)
        dire = [x/10,y/10,z/10]
        glTranslatef(dire[0], dire[1], dire[2])
    if keys[pygame.K_LSHIFT] == True:
        glTranslatef(0,.1,0)
    elif keys[pygame.K_SPACE] == True:
        glTranslatef(0, -.1, 0)
    if keys[pygame.K_i] == True:
        cameraAngle[0] = cameraAngle[0] - 1.
        #rotateX(-1, cameraAngle)
    elif keys[pygame.K_k] == True:
        cameraAngle[0] = cameraAngle[0] + 1.
        #rotateX(1, cameraAngle)
    if keys[pygame.K_j] == True:
        cameraAngle[1] = cameraAngle[1] - 1.
        #rotateY(-1, cameraAngle)
    elif keys[pygame.K_l] == True:
        cameraAngle[1] = cameraAngle[1] + 1.
        #rotateY(1, cameraAngle)
    deltaXAngle = cameraAngle[0]-prevCameraAngle[0]
    deltaYAngle = cameraAngle[1]-prevCameraAngle[1]
    deltaZAngle = cameraAngle[2]-prevCameraAngle[2]
    if not (deltaXAngle == 0 and deltaYAngle == 0 and deltaZAngle == 0):
        #glRotatef(1, x,y,z)
        #glRotatef(2, deltaXAngle*math.cos(math.radians(cameraAngle[1]*2)), deltaYAngle, deltaXAngle*math.sin(math.radians(cameraAngle[1]*2)))
        glRotatef(1, deltaXAngle, deltaYAngle, deltaZAngle)
        glTranslatef(0,0,0)
        #print(cameraAngle)
    #glRotatef(1, 0,0,0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube((-10, -25, -10), 20)
    Cube((-1+off,-1,-1+ofz), 2)
    prevCameraAngle = copy.deepcopy(cameraAngle)
    move+=.1
    #off=(math.sin(move/math.pi))*3
    #ofz=(math.cos(move/math.pi))*3
    if showFPS == 0:
        pygame.display.set_caption(str(round(clock.get_fps(), 2))+' FPS')
    showFPS+=1
    showFPS%=60
    pygame.display.flip()
    clock.tick(60)