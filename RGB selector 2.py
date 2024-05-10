import pygame
import pyperclip
import random
screen = pygame.display.set_mode(size=(500, 500), flags=(pygame.SRCALPHA | pygame.RESIZABLE))
clock = pygame.time.Clock()
pygame.font.init()
screenSize = screen.get_size()
sliderLength = 255
sliderStart = 20
sliderEnd = sliderStart + sliderLength
sliderSpacing = 42
slider1X = sliderStart
slider2X = slider1X
slider3X = slider1X
slider1Y = 40
slider2Y = slider1Y + sliderSpacing
slider3Y = slider2Y + sliderSpacing
colorR = 0
colorG = 0
colorB = 0
color = (222,222,222)
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if keys[pygame.K_r] == True:
            colorR = int(random.random()*255)
            colorG = int(random.random()*255)
            colorB = int(random.random()*255)
            slider1X = colorR + sliderStart
            slider2X = colorG + sliderStart
            slider3X = colorB + sliderStart
    myFont = pygame.font.Font(None, int(500/20))
    screenSize = screen.get_size()
    mousePos = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePos, (1,1))
    if colorR > 255:
        colorR = 255
    elif colorR < 0:
        colorR = 0
    if colorG > 255:
        colorG = 255
    elif colorG < 0:
        colorG = 0
    if colorB > 255:
        colorB = 255
    elif colorB < 0:
        colorB = 0
    #elif 
    tiles = pygame.Surface(screenSize, flags=pygame.SRCALPHA)
    pygame.draw.rect(screen, (colorR, colorG, colorB), ((0,0),screenSize), width=0)
    pygame.draw.rect(tiles, (64,64,64,175), (sliderStart-15, slider1Y-35, sliderLength+35, sliderSpacing*3+14), width=0)
    screen.blit(tiles, (0,0))
    pygame.draw.line(screen, (111,111,111), (sliderStart, slider1Y), (sliderEnd,slider1Y), width=7)
    slider1 = pygame.draw.circle(screen, (colorR, 0, 0), (slider1X, slider1Y), 10, width=0)
    pygame.draw.line(screen, (111,111,111), (sliderStart, slider2Y), (sliderEnd,slider2Y), width=7)
    slider2 = pygame.draw.circle(screen, (0, colorG, 0), (slider2X, slider2Y), 10, width=0)
    pygame.draw.line(screen, (111,111,111), (sliderStart, slider3Y), (sliderEnd,slider3Y), width=7)
    slider3 = pygame.draw.circle(screen, (0, 0, colorB), (slider3X, slider3Y), 10, width=0)
    mouseDown = pygame.mouse.get_pressed()[0]
    hexR = str(hex(colorR)).removeprefix('0x')
    hexG = str(hex(colorG)).removeprefix('0x')
    hexB = str(hex(colorB)).removeprefix('0x')
    Hex = myFont.render('#{}{}{}'.format(hexR if len(hexR) > 1 else str.join(hexR, ['0', '0'])[:-1], hexG if len(hexG) > 1 else str.join(hexG, ['0', '0'])[:-1], hexB if len(hexB) > 1 else str.join(hexB, ['0', '0'])[:-1]), True, color)
    rgb = myFont.render('{}, {}, {}'.format(colorR, colorG, colorB), True, color)
    boxWidth = max(rgb.get_width(), Hex.get_width())+20
    tiles = pygame.Surface(screenSize, flags=pygame.SRCALPHA)
    rgbBox = pygame.draw.rect(tiles, (64,64,64, 175), (sliderStart-15, slider1Y-35+sliderSpacing*3+14+5, boxWidth, rgb.get_height()+20), width=0)
    screen.blit(tiles, (0,0))
    screen.blit(rgb, (sliderStart-15+(boxWidth/2)-(rgb.get_width()/2), slider1Y-35+sliderSpacing*3+14+5+10))
    if pygame.Rect.colliderect(mouseRect, rgbBox) and mouseDown:
        pyperclip.copy('{}, {}, {}'.format(colorR, colorG, colorB))
    Hex = myFont.render('#{}{}{}'.format(hexR if len(hexR) > 1 else str.join(hexR, ['0', '0'])[:-1], hexG if len(hexG) > 1 else str.join(hexG, ['0', '0'])[:-1], hexB if len(hexB) > 1 else str.join(hexB, ['0', '0'])[:-1]), True, color)
    tiles = pygame.Surface(screenSize, flags=pygame.SRCALPHA)
    hexBox = pygame.draw.rect(tiles, (64,64,64,175), (sliderStart-15+boxWidth+5, slider1Y-35+sliderSpacing*3+14+5, boxWidth, Hex.get_height()+20), width=0)
    screen.blit(tiles, (0,0))
    screen.blit(Hex, (sliderStart-15+(boxWidth/2)-(Hex.get_width()/2)+boxWidth+5, slider1Y-35+sliderSpacing*3+14+5+10))
    if pygame.Rect.colliderect(mouseRect, hexBox) and mouseDown:
        pyperclip.copy('#{}{}{}'.format(str(hex(colorR)).removeprefix('0x'), str(hex(colorG)).removeprefix('0x'), str(hex(colorB)).removeprefix('0x')))
    if mousePos[1] >= slider1.top and mousePos[1] <= slider1.bottom and mouseDown == True:
        slider1X = mousePos[0]
        colorR = slider1X-sliderStart
    if slider1X <= sliderStart:
        slider1X = sliderStart
    elif slider1X >= sliderEnd:
        slider1X = sliderEnd
    if mousePos[1] >= slider2.top and mousePos[1] <= slider2.bottom and mouseDown == True:
        slider2X = mousePos[0]
        colorG = slider2X-sliderStart
    if slider2X < sliderStart:
        slider2X = sliderStart
    elif slider2X > sliderEnd:
        slider2X = sliderEnd
    if mousePos[1] >= slider3.top and mousePos[1] <= slider3.bottom and mouseDown == True:
        slider3X = mousePos[0]
        colorB = slider3X-sliderStart
    if slider3X < sliderStart:
        slider3X = sliderStart
    elif slider3X > sliderEnd:
        slider3X = sliderEnd
    value1 = myFont.render(str(slider1X-sliderStart), True, (color))
    screen.blit(value1, (slider1X-value1.get_width()/2, slider1Y-30))
    value2 = myFont.render(str(slider2X-sliderStart), True, (color))
    screen.blit(value2, (slider2X-value2.get_width()/2, slider2Y-30))
    value3 = myFont.render(str(slider3X-sliderStart), True, (color))
    screen.blit(value3, (slider3X-value3.get_width()/2, slider3Y-30))
    pygame.display.update()
    clock.tick(60)