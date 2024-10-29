import pygame
import numpy
from math import cos, sin, sqrt, radians
import utils
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
screenSize = pygame.Surface.get_size(screen)
pygame.font.init()
angle = 0
vertexColor = (255, 255, 255)
lineColor = (255, 255, 255)
defaultFaceColor = (0, 0, 255)
vertices = [(100.0, 400.0, -150.0), (400.0, 400.0, -150.0), (100.0, 500.0, -150.0), (400.0, 500.0, -150.0), (100.0, 400.0, 150.0), (400.0, 400.0, 150.0), (100.0, 500.0, 150.0), (400.0, 500.0, 150.0)]
lines = [(1, 2), (1, 3), (1, 5), (2, 4), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 7), (6, 8), (7, 8)]
faces = [(1,2,3,(0,255,0)), (2,3,4,(0,255,0)), (5,6,7,(0,0,255)), (6,7,8,(0,0,255)), (1,2,5,(255,0,0)), (2,5,6,(255,0,0)), (3,4,7,(255,255,0)), (4,7,8,(255,255,0)), (1,3,5,(0,255,255)), (3,5,7,(0,255,255)), (2,4,6,(255,0,255)), (4,6,8,(255,0,255))]
Points = vertices.copy()
sliderX1 = 95
sliderY1 = 50
sliderLength = 100
sliderStart = 25
cameraPos = numpy.array([250, 250, 0], dtype=float)
cameraOffset = numpy.array([0, 0, 0], dtype=float)
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
    def Update(self, point1, point2, point3, distToCam, midpoint, color=defaultFaceColor):
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
spacing=0
paused = False
sensitivity = 1
prevScreenSize = screenSize
bx, by = 1,1
pygame.mouse.set_visible(False)
fpsCheckbox = utils.Setting.Checkbox((25, 75), 25, 'FPS Counter')
fpsCheckbox.checked = True
while True:
    screenSize = screen.get_size()
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screenSize[0], screenSize[1]), width=0)
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    rotate2dMatrix = numpy.array([[cos(radians(cameraAngle[1])), -sin(radians(cameraAngle[1]))],[sin(radians(cameraAngle[1])), cos(radians(cameraAngle[1]))]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_ESCAPE:
                paused = not paused
                pygame.mouse.set_visible(paused)
        if event.type == pygame.WINDOWRESIZED:
            cameraPos += numpy.array([(screenSize[0]-prevScreenSize[0])/2, (screenSize[1]-prevScreenSize[1])/2, 0])
            prevScreenSize = screenSize
            e = [screenSize[0]/2, screenSize[1]/2, 250]
            for vertex in vertices:
                vertex = ((screenSize[0]-prevScreenSize[0])/2+vertex[0], (screenSize[1]-prevScreenSize[1])/2+vertex[1], vertex[2])
        if event.type == pygame.MOUSEBUTTONDOWN:
            fpsCheckbox.Event(event)
    if keys[pygame.K_r] == True:
        cameraPos = numpy.array([screenSize[0]/2, screenSize[1]/2, 0], dtype=float)
        cameraAngle = numpy.array([0,0,0])
    # region Moving
    if not paused:
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
                cameraAngle[0] += sensitivity*2+.1
            elif mousePos[1] > 250:
                cameraAngle[0] -= sensitivity*2+.1
        if mousePos[0] > 0 and mousePos[0] < 500:
            if mousePos[0] > 250:
                cameraAngle[1] += sensitivity*2+.1
            elif mousePos[0] < 250:
                cameraAngle[1] -= sensitivity*2+.1
        if spacing==1:
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
    mouseDown = pygame.mouse.get_pressed()[0]
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
        #if (((Points[face[0]-1][0] <= screenSize[0] and Points[face[0]-1][0] >= 0) and (Points[face[0]-1][1] <= screenSize[1] and Points[face[0]-1][1] >= 0)) or ((Points[face[1]-1][0] <= screenSize[0] and Points[face[1]-1][0] >= 0) and (Points[face[1]-1][1] <= screenSize[1] and Points[face[1]-1][1] >= 0))) or ((Points[face[2]-1][0] <= screenSize[0] and Points[face[2]-1][0] >= 0) and (Points[face[2]-1][1] <= screenSize[1] and Points[face[2]-1][1] >= 0)):
        try:
            zList.append(Face.Update(Face(), Points[face[0]-1], Points[face[1]-1], Points[face[2]-1], distToCam, absPos, face[3]))
        except IndexError:
            zList.append(Face.Update(Face(), Points[face[0]-1], Points[face[1]-1], Points[face[2]-1], distToCam, absPos))
    for line in lines:
        absPos = utils.Midpoint(Vertices[line[0]-1].xyz, Vertices[line[1]-1].xyz) - cameraPos
        distToCam = sqrt((sqrt((absPos[0]**2)+(absPos[1]**2))**2)+(absPos[2]**2))
        #if ((Points[line[0]-1][0::1][0] <= screenSize[0] and Points[line[0]-1][0::1][0] >= 0) and (Points[line[0]-1][0::1][1] <= screenSize[1] and Points[line[0]-1][0::1][1] >= 0)) or ((Points[line[1]-1][0::1][0] <= screenSize[0] and Points[line[1]-1][0::1][0] >= 0) and (Points[line[1]-1][0::1][1] <= screenSize[1] and Points[line[1]-1][0::1][1] >= 0)):
        zList.append(Line.Update(Line(), Points[line[0]-1][0::1], Points[line[1]-1][0::1], distToCam, absPos))
    zList.sort(key=sorter, reverse=True)
    for thing in zList:
        if thing.__class__ == Vertex:
            pygame.draw.circle(screen, vertexColor, (thing.xy[0], thing.xy[1]), 2.5)
        elif thing.__class__ == Face:
            pygame.draw.polygon(screen, thing.color, (thing.point1, thing.point2, thing.point3), width=0)
        elif thing.__class__ == Line:
            pygame.draw.line(screen, lineColor, thing.point1, thing.point2, width=5)
    if fpsCheckbox.checked:
        text = myFont.render(str(round(clock.get_fps(), 1)), True, utils.white if not paused else utils.darkGray)
        screen.blit(text, (10,10))
    if paused:
        sensitivity, sliderX1 = utils.Slider(sliderStart, sliderLength, sliderX1, sliderY1, screen, name='Sensitivity')
        fpsCheckbox.Render(screen, utils.gray)
    spacing = not spacing
    pygame.display.update()
    clock.tick(60)