import pygame
import math
#import sklearn.preprocessing
import numpy
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
sliderStart = 25
sliderX = 75
sliderY = 50
sliderEnd = 125
color = (222,222,222)
bgColor = (0,0,50)
previousLineThickness = 0
slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
def NormalizeData(data):
    return (data - numpy.min(data)) / (numpy.max(data) - numpy.min(data))
def Draw(lineThickness):
    screenSize = screen.get_size()
    for x in range(int(screenSize[0]/-2), int(screenSize[0]/2)):
        for y in range(int(screenSize[1]/-2), int(screenSize[1]/2)):
            xCoord = x/100
            yCoord = y/100
            if math.isclose(math.cos(xCoord)**2+math.cos(yCoord)**2, 1, abs_tol=lineThickness):
                pygame.draw.circle(screen, (255,255,255), (x+(screenSize[0]/2),y+(screenSize[1]/2)), 1, width=0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            pygame.draw.rect(screen, bgColor, ((0,0),(screenSize)), width=0)
            Draw(lineThickness)
            pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
            slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
            screen.blit(value, (sliderX-value.get_width()/2, sliderY-30))
    screenSize = screen.get_size()
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos() 
    mouseDown = pygame.mouse.get_pressed()[0]
    if mousePos[1] >= slider.top and mousePos[1] <= slider.bottom and mouseDown == True:
        sliderX = mousePos[0]
    if sliderX < sliderStart:
        sliderX = sliderStart
    elif sliderX > sliderEnd:
        sliderX = sliderEnd
    value = myFont.render(str(sliderX-sliderStart), True, (color))
    lineThickness = int((sliderX-sliderStart)+5)/500
    if lineThickness != previousLineThickness:
        pygame.draw.rect(screen, bgColor, ((0,0),(screenSize)), width=0)
        Draw(lineThickness)
        pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
        slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
        screen.blit(value, (sliderX-value.get_width()/2, sliderY-40))
    previousLineThickness = lineThickness
    pygame.display.update()
    clock.tick(60)