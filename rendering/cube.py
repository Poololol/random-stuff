import pygame
import numpy
import math
screen = pygame.display.set_mode(size=(500,500))
clock = pygame.time.Clock()
screenSize = pygame.Surface.get_size(screen)
pygame.font.init()
angle = 0
rotateMatrix = numpy.array([[math.cos(math.radians(angle)), -math.sin(math.radians(angle))], [math.sin(math.radians(angle)), math.cos(math.radians(angle))]])
vertices = [(200, 200, 100), (300, 200, 100), (200, 300, 100), (300, 300, 100), (200, 200, 200), (300, 200, 200), (200, 300, 200), (300, 300, 250)]
lines = [(1, 2), (1, 3), (1, 5), (2, 4), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 7), (6, 8), (7, 8)]
linePoints = vertices
sliderX1 = 75
sliderY1 = 50
sliderX2 = 75
sliderY2 = 100
sliderLength = 100
sliderStart = 25
sliderEnd = sliderStart + sliderLength
sliderColor = (255,255,255)
cameraPos = numpy.array([250, 250, 0])
e = [250, 250, 250]
d = numpy.array([0,0,0])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.draw.rect(screen, (0,0,0), (0,0,screenSize[0],screenSize[1]), width=0)
    i = 0
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY1), (sliderEnd,sliderY1), width=7)
    slider1 = pygame.draw.circle(screen, sliderColor, (sliderX1, sliderY1), 9, width=0)
    pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY2), (sliderEnd,sliderY2), width=7)
    slider2 = pygame.draw.circle(screen, sliderColor, (sliderX2, sliderY2), 9, width=0)
    mouseDown = pygame.mouse.get_pressed()[0]
    cos = math.cos(math.radians(angle))
    sin = math.sin(math.radians(angle))
    vertices = [(200, 200, 100), (300, 200, 100), (200, 300, 100), (300, 300, 100), (200, 200, 200), (300, 200, 200), (200, 300, 200), (300, 300, 200)]
    rotateXMatrix = numpy.array([[1, 0, 0], [0, cos, -sin], [0, sin, cos]])
    rotateYMatrix = numpy.array([[cos, 0, sin],[0, 1, 0], [-sin, 0, cos]])
    rotateZMatrix = numpy.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    axis = 0
    for vertex in vertices:
        #print(vertices)
        vertex = numpy.array(vertex)
        d = numpy.subtract(vertex, cameraPos)
        if axis == 0:
            d = d @ rotateZMatrix
            axis = 1
        if axis == 1:
            de = numpy.array([d[0], d[1], d[2]-150]) @ rotateXMatrix
            d = numpy.array([de[0], de[1], de[2]+150])
            axis = 2
        if axis == 2:
            de = numpy.array([d[0], d[1], d[2]-150]) @ rotateYMatrix
            d = numpy.array([de[0], de[1], de[2]+150])
            axis = 0
        bx = ((e[2]/d[2])*d[0])+e[0]
        by = ((e[2]/d[2])*d[1])+e[1]
        point = (bx, by)
        pygame.draw.circle(screen, (222,222,222), point, 5, width=0)
        linePoints[i] = point
        i = i + 1
    for line in lines:
        pygame.draw.line(screen, (255,255,255), (linePoints[line[0]-1][0], linePoints[line[0]-1][1]), (linePoints[line[1]-1][0], linePoints[line[1]-1][1]), width=2)
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
    angle = sliderValue + angle
    pygame.display.update()
    clock.tick(60)