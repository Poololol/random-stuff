import pygame
import utils
import numpy
import math
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
pygame.font.init()
clock = pygame.time.Clock()
gray = (32, 32, 32)
lightGray = (100, 100, 100)
x=50
x2=20
pixelSize = .01
tool = 'Pen'
pos = 1
sidebarSize = 100
screenSize = screen.get_size()
image = pygame.Surface((screenSize[0]-0, screenSize[1]), pygame.SRCALPHA)
pen = pygame.image.load('Pen Tool.png').convert_alpha()
eraser = pygame.image.load('Eraser Tool.png').convert_alpha()
line = pygame.image.load('Line Tool.png').convert_alpha()
rectangle = pygame.image.load('Rectangle Tool.png').convert_alpha()
circle = pygame.image.load('Circle Tool.png').convert_alpha()
padding = 5
numColumns = 2
numTools = 5
numRows = math.ceil(numTools/numColumns)
toolBoxSize = (sidebarSize-(padding*3))/numColumns
tools = numpy.array((pen, eraser, line, rectangle, circle, pen)).reshape((numRows, numColumns))
toolBoxes = []
toolNum = 0
clicked = False
image = pygame.Surface((2000,1500), flags=pygame.SRCALPHA)
fpsDisplay = False
while True:
    font = pygame.font.Font(None, int(screenSize[0]/20))
    mousePos = pygame.mouse.get_pos()
    mouseDown = pygame.mouse.get_pressed()[0]
    mouseRect = pygame.Rect((mousePos), (1,1))
    pixelSize = pixelSize*75
    pixelColor = (222,222,222)
    pygame.draw.rect(screen, (0,0,0), ((0,0), (screenSize)), width=0)
    if mouseDown and toolNum == 0 and mousePos[0] > sidebarSize and not clicked:
        pygame.draw.circle(image, pixelColor, mousePos, pixelSize, width=0)
    elif mouseDown and toolNum == 1 and mousePos[0] > sidebarSize and not clicked:
        pygame.draw.circle(image, (0,0,0,0), mousePos, pixelSize, width=0)
    if abs(mousePos[0]-sidebarSize) <= 5:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if clicked:
        prev = sidebarSize
        sidebarSize = mousePos[0]
        if sidebarSize <= 50:
            sidebarSize = 50
        x+=(sidebarSize-prev)*(pixelSize/75)
        toolBoxSize = (sidebarSize-(padding*3))/numColumns
    if fpsDisplay:
        text = font.render(str(round(clock.get_fps(), 2)), True, utils.blue)
        screen.blit(text, (sidebarSize+10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            #image = pygame.transform.scale(image, (screenSize[0], screenSize[1]))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if abs(mousePos[0]-sidebarSize) <= 2:
                clicked = True
            if toolNum == 2 and mousePos[0] > sidebarSize and event.dict['button'] == 1:
                if pos == 1:
                    pos1 = mousePos
                    pos = 2
                elif pos == 2:
                    pos2 = mousePos
                    pos = 1
                    pygame.draw.line(image, pixelColor, pos1, pos2, int(pixelSize*2))
            if toolNum == 3 and mousePos[0] > sidebarSize and event.dict['button'] == 1:
                if pos == 1:
                    pos1 = mousePos
                    pos = 2
                elif pos == 2:
                    pos2 = mousePos
                    pos = 1
                    wh = (pos2[0]-pos1[0], pos2[1]-pos1[1])
                    pygame.draw.rect(image, pixelColor, pygame.Rect(pos1, wh), int(pixelSize))
            if toolNum == 4 and mousePos[0] > sidebarSize and event.dict['button'] == 1:
                if pos == 1:
                    pos1 = mousePos
                    pos = 2
                elif pos == 2:
                    pos2 = mousePos
                    pos = 1
                    wh = (abs(pos2[0]-pos1[0]), abs(pos2[1]-pos1[1]))
                    pygame.draw.ellipse(image, pixelColor, pygame.Rect(pos1, wh), int(pixelSize))
            i=0
            for toolBox in toolBoxes:
                if pygame.Rect.colliderect(mouseRect, toolBox):
                    toolNum = i
                i+=1
        elif event.type == pygame.MOUSEBUTTONUP:
            if abs(mousePos[0]-sidebarSize) <= 2:
                clicked = False
        elif event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_f:
                fpsDisplay = not fpsDisplay
            elif event.dict['key'] == pygame.K_p:
                tool = 'Pen'
                toolNum = 0
            elif event.dict['key'] == pygame.K_e:
                tool = 'Eraser'
                toolNum = 1
            elif event.dict['key'] == pygame.K_l:
                tool = 'Line'
                toolNum = 2
    screen.blit(image, (0,0))
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, sidebarSize, screenSize[1]), width=0)
    it = numpy.nditer(tools, flags=['refs_ok', 'external_loop'])
    for ad in it:
        i=0
        j=0
        toolBoxes = []
        for toolBox in ad:
            if toolBox != 0:
                location = ((i*toolBoxSize)+((i+1)*padding), (j*toolBoxSize)+((j+1)*padding)+50)
                locationRect = pygame.Rect(location, (toolBoxSize, toolBoxSize))
                if pygame.Rect.colliderect(mouseRect, locationRect):
                    boxColor = lightGray
                else:
                    boxColor = gray
                toolBoxes.append(pygame.draw.rect(screen, boxColor, (location, (toolBoxSize, toolBoxSize)), width=0))
                screen.blit(pygame.transform.scale(toolBox, (toolBoxSize, toolBoxSize)), location)
            i+=1
            if i>=numColumns:
                i=0
                j+=1
    pixelSize, x = utils.Slider(15, sidebarSize-30, x, 35, screen, returnPercent=False)
    pixelSize = pixelSize/150
    pygame.display.update()
    clock.tick(600)
