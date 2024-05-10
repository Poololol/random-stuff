import pygame
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
screenSize = screen.get_size()
clock = pygame.time.Clock()
pygame.font.init()
myFont = pygame.font.SysFont('freesansbold', int(screenSize[0]/10))
values = pygame.font.get_fonts()
buttonColor = (66,66,66)
edge = 20
middle = 30
mouseDown = 0
textColor = (222,222,222)
open = False
dropDownWidth = 150
selectedValue = 0
scrollOffset = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        else:
            mouseDown = False
        if event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_UP:
                scrollOffset -= 1
            elif event.dict['key'] == pygame.K_DOWN:
                scrollOffset += 1
    screenSize = screen.get_size()
    background = pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
    button = pygame.draw.rect(screen, buttonColor, (10,10, dropDownWidth, 30), width=0)
    pygame.draw.line(screen, (255,255,255), (dropDownWidth-15, edge), (dropDownWidth-10, middle), width=2)
    pygame.draw.line(screen, (255,255,255), (dropDownWidth-5,edge), (dropDownWidth-10,middle), width=2)
    myFont = pygame.font.SysFont(values[selectedValue], int(500/15))
    smallerFont = pygame.font.SysFont(values[selectedValue], int(500/25))
    mousePos = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePos, (1,1))
    buttonText = myFont.render(values[selectedValue], True, textColor)
    screen.blit(buttonText, (10,10))
    if mouseDown > 1:
        mouseDown = 0
    if pygame.Rect.colliderect(mouseRect, button):
        buttonColor = (111,111,111)
        if mouseDown:
            edge = 30
            middle = 20
            if open == True:
                open = False
            else:
                open = True
        else:
            edge = 20
            middle = 30
    else:
        buttonColor = (50,50,50)
    if open:
        option1 = pygame.draw.rect(screen, (1,1,1), (10, 40, 110, 30), width=0)
        option1 = pygame.draw.rect(screen, (111,111,111) if pygame.Rect.colliderect(mouseRect, option1) else (64,64,64), (10, 40, dropDownWidth, 30), width=0)
        #smallerFont = pygame.font.SysFont(values[0+scrollOffset], int(500/25))
        option1Text = smallerFont.render(values[0+scrollOffset], True, textColor)
        screen.blit(option1Text, (10, 40))
        if pygame.Rect.colliderect(mouseRect, option1) and mouseDown:
            selectedValue = 0+scrollOffset
        option2 = pygame.draw.rect(screen, (1,1,1), (10, 70, 110, 30), width=0)
        option2 = pygame.draw.rect(screen, (111,111,111) if pygame.Rect.colliderect(mouseRect, option2) else (64,64,64), (10, 70, dropDownWidth, 30), width=0)
        #smallerFont = pygame.font.SysFont(values[1+scrollOffset], int(500/25))
        option2Text = smallerFont.render(values[1+scrollOffset], True, textColor)
        screen.blit(option2Text, (10, 70))
        if pygame.Rect.colliderect(mouseRect, option2) and mouseDown:
            selectedValue = 1+scrollOffset
        option3 = pygame.draw.rect(screen, (1,1,1), (10, 100, 110, 30), width=0)
        option3 = pygame.draw.rect(screen, (111,111,111) if pygame.Rect.colliderect(mouseRect, option3) else (64,64,64), (10, 100, dropDownWidth, 30), width=0)
        #smallerFont = pygame.font.SysFont(values[2+scrollOffset], int(500/25))
        option3Text = smallerFont.render(values[2+scrollOffset], True, textColor)
        screen.blit(option3Text, (10, 100))
        if pygame.Rect.colliderect(mouseRect, option3) and mouseDown:
            selectedValue = 2+scrollOffset
    pygame.display.update()
    clock.tick(60)