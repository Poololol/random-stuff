import pygame
screen = pygame.display.set_mode(size=(500, 500))
clock = pygame.time.Clock()
pygame.font.init()
screenSize = screen.get_size()
sliderX = 100
sliderY = 50
sliderLength = 100
sliderStart = 50
sliderEnd = sliderStart + sliderLength
color = (222,222,222)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0,0,0), (0,0,500,500), width=0)
    pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY), (sliderEnd,sliderY), width=7)
    slider = pygame.draw.circle(screen, color, (sliderX, sliderY), 10, width=0)
    mouseDown = pygame.mouse.get_pressed()[0]
    if mousePos[1] >= slider.top and mousePos[1] <= slider.bottom and mouseDown == True:
        sliderX = mousePos[0]
    if sliderX < sliderStart:
        sliderX = sliderStart
    elif sliderX > sliderEnd:
        sliderX = sliderEnd
    value = myFont.render(str(sliderX-sliderStart), True, (color))
    screen.blit(value, (sliderX-value.get_width()/2, sliderY-30))
    pygame.display.update()
    clock.tick(60)