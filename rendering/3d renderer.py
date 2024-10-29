import pygame
import numpy
import math
import utils
screen = pygame.display.set_mode(size=(500,500), flags=pygame.SRCALPHA)
clock = pygame.time.Clock()
screenSize = pygame.Surface.get_size(screen)
pygame.font.init()
angle = 0
vertices = [(200, 200, 100), (300, 200, 100), (200, 300, 100), (300, 300, 100), (200, 200, 200), (300, 200, 200), (200, 300, 200), (300, 300, 250)]
lines = [(1, 2), (1, 3), (1, 5), (2, 4), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 7), (6, 8), (7, 8)]
faces = [(1,2,4,3,(255,100,64)), (5,6,8,7,(64,255,100))]
Points = vertices
sliderX1 = 75
sliderY1 = 50
sliderX2 = 75
sliderY2 = 100
sliderLength = 100
sliderStart = 25
sliderEnd = sliderStart + sliderLength
sliderColor = (255, 255, 255)
faceColor = (0, 64, 200, 5)
cameraPos = numpy.array([250, 250, 0])
e = [250, 250, 250]
d = numpy.array([0, 0, 0])
axis = 0
while True:   
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screenSize[0], screenSize[1]), width=0)
    i = 0
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r] == True:
        sliderX1 = sliderStart + sliderLength/2
        sliderX2 = sliderStart + sliderLength/2
        angle = 0
        cameraPos = numpy.array([250, 250, 0])
    if keys[pygame.K_w] == True:
        cameraPos[1] = cameraPos[1] - 1
    elif keys[pygame.K_s] == True:
        cameraPos[1] = cameraPos[1] + 1
    if keys[pygame.K_d] == True:
        cameraPos[0] = cameraPos[0] + 1
    elif keys[pygame.K_a] == True:
        cameraPos[0] = cameraPos[0] - 1
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
    axisText = myFont.render('Axis: {}'.format(axisL), True, sliderColor)
    screen.blit(axisText, (sliderEnd+10, sliderY1-axisText.get_height()/2))
    mouseDown = pygame.mouse.get_pressed()[0]
    cos = math.cos(math.radians(angle))
    sin = math.sin(math.radians(angle))
    vertices = [(200, 200, 100), (300, 200, 100), (200, 300, 100), (300, 300, 100), (200, 200, 200), (300, 200, 200), (200, 300, 200), (300, 300, 200)]
    rotateXMatrix = numpy.array([[1, 0, 0], [0, cos, -sin], [0, sin, cos]])
    rotateYMatrix = numpy.array([[cos, 0, sin],[0, 1, 0], [-sin, 0, cos]])
    rotateZMatrix = numpy.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    for vertex in vertices:
        vertex = numpy.array(vertex)
        d = numpy.subtract(vertex, cameraPos)
        if axis == 0:
            de = numpy.array([d[0]+(cameraPos[0]-250), d[1]+(cameraPos[1]-250), d[2]-150]) @ rotateZMatrix
            d = numpy.array([de[0]-(cameraPos[0]-250), de[1]-(cameraPos[1]-250), de[2]+150])
        elif axis == 1:
            de = numpy.array([d[0]+(cameraPos[0]-250), d[1]+(cameraPos[1]-250), d[2]-150]) @ rotateXMatrix
            d = numpy.array([de[0]-(cameraPos[0]-250), de[1]-(cameraPos[1]-250), de[2]+150])
        elif axis == 2:
            de = numpy.array([d[0]+(cameraPos[0]-250), d[1]+(cameraPos[1]-250), d[2]-150]) @ rotateYMatrix
            d = numpy.array([de[0]-(cameraPos[0]-250), de[1]-(cameraPos[1]-250), de[2]+150])
        bx = ((e[2]/d[2])*d[0])+e[0]
        by = ((e[2]/d[2])*d[1])+e[1]
        point = (bx, by)
        pygame.draw.circle(screen, (255,255,255), point, 0, width=0)
        Points[i] = point
        i = i + 1
    for face in faces:
        pygame.draw.polygon(screen, face[4], (Points[face[0]-1], Points[face[1]-1], Points[face[2]-1], Points[face[3]-1]), width=0)
    for line in lines:
        pygame.draw.line(screen, (255,255,255), (Points[line[0]-1][0::1]), (Points[line[1]-1][0::1]), width=3)
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
    sliderValue = (sliderX1-sliderStart-50)/10
    value = myFont.render(str(sliderValue), True, (sliderColor))
    screen.blit(value, (sliderX1-value.get_width()/2, sliderY1-30))
    slider2Value = (sliderX2-sliderStart-50)*2
    value2 = myFont.render(str(slider2Value), True, (sliderColor))
    screen.blit(value2, (sliderX2-value2.get_width()/2, sliderY2-30))
    e = [250, 250, 250 + slider2Value]
    angle = -sliderValue + angle
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if keys[pygame.K_UP] == True:
            axis = axis + 1
        elif keys[pygame.K_DOWN] == True:
            axis = axis - 1
        elif keys[pygame.K_F2] == True:
            utils.TakeScreenshot(screen)
    clock.tick(60)
