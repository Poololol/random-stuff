import pygame
import numpy
from math import cos, sin, sqrt, radians
import math
import utils
import pyperclip
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE|pygame.SRCALPHA)
clock = pygame.time.Clock()
screenSize = pygame.Surface.get_size(screen)
pygame.font.init()
angle = 0
vertexColor = (255, 255, 255)
lineColor = (255, 255, 255)
faceColor = (0, 0, 255, 1)
vertices = [(200, 200, 100), (300, 200, 100), (200, 300, 100), (300, 300, 100), (200, 200, 200), (300, 200, 200), (200, 300, 200), (300, 300, 200)]
lines = [(1, 2), (1, 3), (1, 5), (2, 4), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 7), (6, 8), (7, 8)]
faces = [(1,2,3,(0,255,0)), (2,3,4,(0,255,0)), (5,6,7,(0,0,255)), (6,7,8,(0,0,255)), (1,2,5,(255,0,0)), (2,5,6,(255,0,0)), (3,4,7,(255,255,0)), (4,7,8,(255,255,0)), (1,3,5,(0,255,255)), (3,5,7,(0,255,255)), (2,4,6,(255,0,255)), (4,6,8,(255,0,255))]
Points = vertices.copy()
sliderX1 = 75
sliderY1 = 50
sliderX2 = 75
sliderY2 = 100
sliderLength = 100
sliderStart = 25
sliderEnd = sliderStart + sliderLength
sliderColor = (255, 255, 255)
cameraPos = numpy.array([250, 250, 0], dtype=float)
e = [250, 250, 250]
d = numpy.array([0, 0, 0])
cameraAngle = [0, 0, 0]
axis = 0
class Vertex():
    def Update(self, x, y, z, distToCam, xy):
        self.x = x
        self.y = y
        self.z = z
        self.distToCam = distToCam
        self.xyz = numpy.array([x,y,z])
        self.xy = xy
        return self
class Face():
    def Update(self, point1, point2, point3, distToCam, midpoint, color=(0,0,255)):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.distToCam = distToCam
        self.midpoint = midpoint
        self.color = color
        return self
class Line():
    def Update(self, point1, point2, distToCam, midpoint):
        self.point1 = point1
        self.point2 = point2
        self.distToCam = distToCam
        self.midpoint = midpoint
        return self
def sorter(thing):
    return thing.distToCam
#vertices = startVertices
t=0
paused = False
pygame.mouse.set_visible(False)
while True:
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screenSize[0], screenSize[1]), width=0)
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    rotate2dMatrix = numpy.array([[cos(radians(cameraAngle[1])), -sin(radians(cameraAngle[1]))],[sin(radians(cameraAngle[1])), cos(radians(cameraAngle[1]))]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_UP:
                axis = axis + 1
            elif event.__dict__['key'] == pygame.K_DOWN:
                axis = axis - 1
            elif event.__dict__['key'] == pygame.K_ESCAPE:
                paused = not paused
                pygame.mouse.set_visible(paused)
    if keys[pygame.K_r] == True:
        sliderX1 = sliderStart + sliderLength/2
        sliderX2 = sliderStart + sliderLength/2
        angle = 0
        cameraPos = numpy.array([250, 250, 0], dtype=float)
        cameraAngle = numpy.array([0,0,0])
    # region Moving
    if keys[pygame.K_w]:
        offset = (rotate2dMatrix @ numpy.array([1,0]))
        cameraPos[0] += offset[1]
        cameraPos[2] += offset[0]
    elif keys[pygame.K_s] == True:
        offset = (rotate2dMatrix @ numpy.array([-1,0]))
        cameraPos[0] += offset[1]
        cameraPos[2] += offset[0]
    if keys[pygame.K_d] == True:
        offset = (rotate2dMatrix @ numpy.array([0,1]))
        cameraPos[0] += offset[1]
        cameraPos[2] += offset[0]
    elif keys[pygame.K_a] == True:
        offset = (rotate2dMatrix @ numpy.array([0,-1]))
        cameraPos[0] += offset[1]
        cameraPos[2] += offset[0]
    if keys[pygame.K_SPACE]:
        cameraPos[1] -= 1
    elif keys[pygame.K_LSHIFT]:
        cameraPos[1] += 1
    # endregion
    # region Looking
    if paused == False:
        if mousePos[1] > 0 and mousePos[1] < 500:
            if mousePos[1] < 250:
                cameraAngle[0] += 1
            elif mousePos[1] > 250:
                cameraAngle[0] -= 1
        if mousePos[0] > 0 and mousePos[0] < 500:
            if mousePos[0] > 250:
                cameraAngle[1] += 1
            elif mousePos[0] < 250:
                cameraAngle[1] -= 1
        if t==1:
            pygame.mouse.set_pos(250,250)
    if keys[pygame.K_i]:
        cameraAngle[0] += 1
    elif keys[pygame.K_k]:
        cameraAngle[0] -= 1
    if keys[pygame.K_j]:
        cameraAngle[1] -= 1
    elif keys[pygame.K_l]:
        cameraAngle[1] += 1
    # endregion
    if axis < 0:
        axis = 0
    elif axis > 2:
        axis = 2
    if axis == 0:
        axisL = 'Z'
    elif axis == 1:
        axisL = 'X'
    else:
        axisL = 'Y'
    sinAngle = sin(radians(angle))
    cosAngle = cos(radians(angle))
    axisText = myFont.render('Axis: {}'.format(axisL), True, sliderColor)
    screen.blit(axisText, (sliderEnd+10, sliderY1-axisText.get_height()/2))
    mouseDown = pygame.mouse.get_pressed()[0]
    rotateXMatrix = numpy.array([[1, 0, 0], [0, cosAngle, -sinAngle], [0, sinAngle, cosAngle]])
    rotateYMatrix = numpy.array([[cosAngle, 0, sinAngle],[0, 1, 0], [-sinAngle, 0, cosAngle]])
    rotateZMatrix = numpy.array([[cosAngle, -sinAngle, 0], [sinAngle, cosAngle, 0], [0, 0, 1]])
    cameraTransform1 = numpy.array([[1, 0, 0], [0, cos(radians(cameraAngle[0])), sin(radians(cameraAngle[0]))], [0, -sin(radians(cameraAngle[0])), cos(radians(cameraAngle[0]))]])
    cameraTransform2 = numpy.array([[cos(radians(cameraAngle[1])), 0, -sin(radians(cameraAngle[1]))], [0, 1, 0], [sin(radians(cameraAngle[1])), 0, cos(radians(cameraAngle[1]))]])
    cameraTransform3 = numpy.array([[cos(radians(cameraAngle[2])), sin(radians(cameraAngle[2])), 0], [-sin(cameraAngle[2]), cos(radians(cameraAngle[2])), 0], [0, 0, 1]])
    Vertices = []
    zList = []
    i = 0
    for vertex in vertices:
        currentVertex = Vertex.Update(Vertex(), vertex[0], vertex[1], vertex[2], 1, 1)
        absPos = currentVertex.xyz - cameraPos
        distToCam = sqrt((sqrt((absPos[0]**2)+(absPos[1]**2))**2)+(absPos[2]**2))
        d = ((cameraTransform1 @ cameraTransform2) @ cameraTransform3) @ (currentVertex.xyz - cameraPos)
        de = numpy.array([d[0]+(cameraPos[0]-250), d[1]+(cameraPos[1]-250), d[2]+(cameraPos[2])])
        if axis == 0:
            de = de @ rotateZMatrix
        elif axis == 1:
            de = de @ rotateXMatrix
        elif axis == 2:
            de = de @ rotateYMatrix
        d = numpy.array([de[0]-(cameraPos[0]-250), de[1]-(cameraPos[1]-250), de[2]-(cameraPos[2])])
        #vertices[i]=da
        if d[2] != 0:
            bx = ((e[2]/d[2])*d[0])+e[0]
            by = ((e[2]/d[2])*d[1])+e[1]
        point = (bx, by)
        currentVertex.Update(vertices[i][0], vertices[i][1], vertices[i][2], distToCam, point)
        zList.append(currentVertex)
        Vertices.append(currentVertex)
        Points[i] = point
        i += 1
    for face in faces:
        absPos = utils.TriangleMidpoint(Vertices[face[0]-1].xyz, Vertices[face[1]-1].xyz, Vertices[face[2]-1].xyz) - cameraPos
        distToCam = sqrt((sqrt((absPos[0]**2)+(absPos[1]**2))**2)+(absPos[2]**2))
        try:
            zList.append(Face.Update(Face(), Points[face[0]-1], Points[face[1]-1], Points[face[2]-1], distToCam, absPos, face[3]))
        except IndexError:
            zList.append(Face.Update(Face(), Points[face[0]-1], Points[face[1]-1], Points[face[2]-1], distToCam, absPos))
    for line in lines:
        absPos = utils.Midpoint(Vertices[line[0]-1].xyz, Vertices[line[1]-1].xyz) - cameraPos
        distToCam = sqrt((sqrt((absPos[0]**2)+(absPos[1]**2))**2)+(absPos[2]**2))
        if ((Points[line[0]-1][0::1][0] <= 500 and Points[line[0]-1][0::1][0] >= 0) and (Points[line[0]-1][0::1][1] <= 500 and Points[line[0]-1][0::1][1] >= 0)) or ((Points[line[1]-1][0::1][0] <= 500 and Points[line[1]-1][0::1][0] >= 0) and (Points[line[1]-1][0::1][1] <= 500 and Points[line[1]-1][0::1][1] >= 0)):
            zList.append(Line.Update(Line(), Points[line[0]-1][0::1], Points[line[1]-1][0::1], distToCam, absPos))
    zList.sort(key=sorter, reverse=True)
    for thing in zList:
        if thing.__class__.__name__ == 'Vertex':
            pygame.draw.circle(screen, vertexColor, (thing.xy[0], thing.xy[1]), 2.5)
            #screen.blit(myFont.render(str(round(thing.distToCam, 1)), True, vertexColor), (thing.xy[0], thing.xy[1]))
        elif thing.__class__.__name__ == 'Face':
            pygame.draw.polygon(screen, thing.color, (thing.point1, thing.point2, thing.point3), width=0)
            #screen.blit(myFont.render(str(round(thing.distToCam, 1)), True, vertexColor), utils.TriangleMidpoint(thing.xy1, thing.xy2, thing.xy3))
        elif thing.__class__.__name__ == 'Line':
            pygame.draw.line(screen, lineColor, thing.point1, thing.point2, width=5)
            #screen.blit(myFont.render(str(round(thing.distToCam, 1)), True, vertexColor), utils.Midpoint(thing.xy1, thing.xy2))
        #print(f'{thing.distToCam}, {thing.__class__.__name__}')
    pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY1), (sliderEnd,sliderY1), width=7)
    slider1 = pygame.draw.circle(screen, sliderColor, (sliderX1, sliderY1), 9, width=0)
    pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY2), (sliderEnd,sliderY2), width=7)
    slider2 = pygame.draw.circle(screen, sliderColor, (sliderX2, sliderY2), 9, width=0)
    if mousePos[1] >= slider1.top and mousePos[1] <= slider1.bottom and mouseDown == True:
        sliderX1 = mousePos[0]
    if sliderX1 < sliderStart:
        sliderX1 = sliderStart
    elif sliderX1 > sliderEnd:
        sliderX1 = sliderEnd
    if mousePos[1] >= slider2.top and mousePos[1] <= slider2.bottom and mouseDown == True:
        sliderX2 = mousePos[0]
    if sliderX2 < sliderStart:
        sliderX2 = sliderStart
    elif sliderX2 > sliderEnd:
        sliderX2 = sliderEnd
    sliderValue = (sliderX1-sliderStart-50)/50
    value = myFont.render(str(round(sliderValue*10, 2)), True, (sliderColor))
    screen.blit(value, (sliderX1-value.get_width()/2, sliderY1-30))
    slider2Value = (sliderX2-sliderStart-50)*2
    value2 = myFont.render(str(slider2Value), True, (sliderColor))
    screen.blit(value2, (sliderX2-value2.get_width()/2, sliderY2-30))
    e = [250, 250, 250 + slider2Value]
    angle = sliderValue+angle
    t=not t
    pygame.display.update()
    clock.tick(60)