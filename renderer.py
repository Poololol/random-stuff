import pygame
import numpy
import math
screen = pygame.display.set_mode(size=(500,500))
clock = pygame.time.Clock()
screenSize = pygame.Surface.get_size(screen)
pygame.font.init()
angle = 3
rotateMatrix = numpy.array([[math.cos(math.radians(angle)), -math.sin(math.radians(angle))], [math.sin(math.radians(angle)), math.cos(math.radians(angle))]])
vertices = [(200, 200), (300, 200), (200, 300), (300, 300), (100, 250)]
lines = [(1, 2), (1, 3), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5), (4, 5)]
tempVertices = vertices
sliderX = 100
sliderY = 50
sliderLength = 100
sliderStart = 50
sliderEnd = sliderStart + sliderLength
sliderColor = (255,255,255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.draw.rect(screen, (0,0,0), (0,0,screenSize[0],screenSize[1]), width=0)
    i = 0
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
    slider = pygame.draw.circle(screen, sliderColor, (sliderX, sliderY), 10, width=0)
    mouseDown = pygame.mouse.get_pressed()[0]
    for vertex in vertices:
        rotateMatrix = numpy.array([[math.cos(math.radians(angle)), -math.sin(math.radians(angle))], [math.sin(math.radians(angle)), math.cos(math.radians(angle))]])
        vertex = numpy.array([vertex[0]-250, vertex[1]-250]) @ rotateMatrix
        pygame.draw.circle(screen, (222,222,222), (vertex[0]+250, vertex[1]+250), 5, width=0)
        tempVertices[i] = (vertex[0]+250, vertex[1]+250)
        i = i + 1
    for line in lines:
        pygame.draw.line(screen, (255,255,255), vertices[line[0]-1], vertices[line[1]-1], width=2)
    vertices = tempVertices
    if mousePos[0] <= slider.right and mousePos[0] >= slider.left and mousePos[1] >= slider.top and mousePos[1] <= slider.bottom and mouseDown == True:
        sliderX = mousePos[0]
    if sliderX < sliderStart:
        sliderX = sliderStart
    elif sliderX > sliderEnd:
        sliderX = sliderEnd
    sliderValue = (sliderX-sliderStart-50)/10
    value = myFont.render(str(sliderValue), True, (sliderColor))
    screen.blit(value, (sliderX-value.get_width()/2, sliderY-30))
    angle = sliderValue
    pygame.display.update()
    clock.tick(60)