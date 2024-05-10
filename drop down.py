import pygame
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
screenSize = screen.get_size()
clock = pygame.time.Clock()
pygame.font.init()
myFont = pygame.font.SysFont('arialbold', int(screenSize[0]/20))
buttonColor = (66,66,66)
edge = 20
middle = 30
mouseDown = False
textColor = (222,222,222)
opened = False
values = ['Earth','Dark','Light']
selectedValue = 0
while True:
    pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
    button = pygame.draw.rect(screen, buttonColor, (10,10, 110, 30), width=0)
    pygame.draw.line(screen, (255,255,255), (95, edge), (100, middle), width=2)
    pygame.draw.line(screen, (255,255,255), (105,edge), (100,middle), width=2)
    myFont = pygame.font.SysFont('arialbold', int(screenSize[0]/11))
    buttonText = myFont.render(values[selectedValue-1], True, textColor)
    screen.blit(buttonText, (10,10))
    mousePos = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePos, (1,1))
    if opened:
        option1 = pygame.draw.rect(screen, (1,1,1), (10, 40, 110, 30), width=0)
        option1 = pygame.draw.rect(screen, (111,111,111) if pygame.Rect.colliderect(mouseRect, option1) else (64,64,64), (10, 40, 110, 30), width=0)
        option1Text = myFont.render(values[0], True, textColor)
        screen.blit(option1Text, (10, 40))
        if pygame.Rect.colliderect(mouseRect, option1) and mouseDown:
            selectedValue = 1
            opened = False
        option2 = pygame.draw.rect(screen, (1,1,1), (10, 70, 110, 30), width=0)
        option2 = pygame.draw.rect(screen, (111,111,111) if pygame.Rect.colliderect(mouseRect, option2) else (64,64,64), (10, 70, 110, 30), width=0)
        option2Text = myFont.render(values[1], True, textColor)
        screen.blit(option2Text, (10, 70))
        if pygame.Rect.colliderect(mouseRect, option2) and mouseDown:
            selectedValue = 2
            opened = False
        option3 = pygame.draw.rect(screen, (1,1,1), (10, 100, 110, 30), width=0)
        option3 = pygame.draw.rect(screen, (111,111,111) if pygame.Rect.colliderect(mouseRect, option3) else (64,64,64), (10, 100, 110, 30), width=0)
        option3Text = myFont.render(values[2], True, textColor)
        screen.blit(option3Text, (10, 100))
        if pygame.Rect.colliderect(mouseRect, option3) and mouseDown:
            selectedValue = 3
            opened = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect.colliderect(mouseRect, button):
                buttonColor = (111,111,111)
                edge = 30
                middle = 20
                opened = not opened
            else:
                edge = 20
                middle = 30
                buttonColor = (50, 50, 50) 
    mouseDown = pygame.mouse.get_pressed()[0]
    pygame.display.update()
    clock.tick(60)