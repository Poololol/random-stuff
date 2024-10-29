import pygame
import math
import numpy
pygame.display.init()
screen = pygame.display.set_mode((750, 750), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
sliderStart = 25
sliderX = 50
sliderY = 50
sliderEnd = 125
color = (222,222,222)
previousLineThickness = .06
lineThickness = .06
screenSize = screen.get_size()
myFont = pygame.font.Font(None, int(screenSize[1]/20))
axesColor = (255,255,255)
myFont.render(str(sliderX-sliderStart), True, (color))
value = myFont.render(str(sliderX-sliderStart), True, (color))
#slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
lessThanShadingColor = (0, 0, 50, 100)
greaterThanShadingColor = (50, 50, 100, 100)
lineColor = (222, 222, 255)
def Draw_Line(lineThickness: float, shapeColor: pygame.Color):
    for x in range(int(screenSize[0]/-2), int(screenSize[0]/2)):
        for y in range(int(screenSize[1]/-2), int(screenSize[1]/2)):
            xCoord = x/100
            yCoord = y/-100
            equ = math.cos(xCoord)**2+math.cos(yCoord)**2
            if math.isclose(equ, 1, abs_tol=.02):
                pygame.draw.circle(screen, shapeColor, (x+(screenSize[0]/2),y+(screenSize[1]/2)), int(lineThickness*100), width=0)
                pygame.display.update()
def Draw(lineThickness: float, lessThanShading: bool, greaterThanShading: bool, lessThanShadingColor: pygame.Color, greaterThanShadingColor: pygame.Color, shapeColor: pygame.Color):
    screenSize = screen.get_size()
    image = pygame.Surface((1,1), flags=pygame.SRCALPHA)
    global fullImage
    fullImage = pygame.Surface(screenSize, pygame.SRCALPHA)
    yAxis = pygame.draw.line(screen, axesColor, (screenSize[0]/2, 0), (screenSize[0]/2, screenSize[1]), width=1)
    xAxis = pygame.draw.line(screen, axesColor, (0, screenSize[1]/2), (screenSize[0], screenSize[1]/2), width=1)
    pygame.display.update()
    if lessThanShading or greaterThanShading:
        for y in range(int(screenSize[1]/-2), int(screenSize[1]/2)):
            for x in range(int(screenSize[0]/-2), int(screenSize[0]/2)):
                xCoord = x/100
                yCoord = y/-100
                equ = math.cos(xCoord)**2+math.cos(yCoord)**2
                if lessThanShading:
                    if equ > 1:
                        pygame.draw.circle(image, lessThanShadingColor, (1,1), 1, width=0)
                        pygame.draw.circle(fullImage, lessThanShadingColor, (x+screenSize[0]/2,y+screenSize[1]/2), 1, width=0)
                if greaterThanShading:
                    if equ < 1:
                        pygame.draw.circle(image, greaterThanShadingColor, (1,1), 1, width=0)
                        pygame.draw.circle(fullImage, greaterThanShadingColor, (x+screenSize[0]/2,y+screenSize[1]/2), 1, width=0)
                screen.blit(image, (x+screenSize[0]/2,y+screenSize[1]/2))
                pygame.display.update(((x+screenSize[0]/2,y+screenSize[1]/2),(1,1)))
    Draw_Line(lineThickness, shapeColor)
    screen.blit(image, (0,0))
pygame.draw.rect(screen, (0,0,0), ((0,0),(screenSize)), width=0)
pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
screen.blit(value, (sliderX-value.get_width()/2, sliderY-40))
Draw(lineThickness, True, True, lessThanShadingColor, greaterThanShadingColor, lineColor)
pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
screen.blit(value, (sliderX-value.get_width()/2, sliderY-40))
while True:
    screenSize = screen.get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            pygame.draw.rect(screen, (0,0,0), ((0,0),(screenSize)), width=0)
            pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
            slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
            screen.blit(value, (sliderX-value.get_width()/2, sliderY-40))
            Draw(lineThickness, True, True, lessThanShadingColor, greaterThanShadingColor, lineColor)
            pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
            slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
            screen.blit(value, (sliderX-value.get_width()/2, sliderY-40))
        if event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_F11:
                pygame.display.toggle_fullscreen()
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
        pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
        yAxis = pygame.draw.line(screen, axesColor, (screenSize[0]/2, 0), (screenSize[0]/2, screenSize[1]), width=1)
        xAxis = pygame.draw.line(screen, axesColor, (0, screenSize[1]/2), (screenSize[0], screenSize[1]/2), width=1)
        screen.blit(fullImage, (0,0))
        pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
        slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
        screen.blit(value, (sliderX-value.get_width()/2, sliderY-40))
        Draw_Line(lineThickness, lineColor)
        pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
        slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
        screen.blit(value, (sliderX-value.get_width()/2, sliderY-40))
    previousLineThickness = lineThickness
    pygame.display.update()
    #clock.tick(60)