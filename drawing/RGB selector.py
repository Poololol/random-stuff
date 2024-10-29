import pygame
screen = pygame.display.set_mode(size=(500, 500))
clock = pygame.time.Clock()
pygame.font.init()
screenSize = screen.get_size()
sliderX = 100
sliderY = 50
sliderLength = 255
sliderStart = 50
sliderEnd = sliderStart + sliderLength
color = (222,222,222)
sliders = [0,1,2]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (sliderX-sliderStart,sliderX-sliderStart,sliderX-sliderStart), (0,0,500,500), width=0)
    for x in range(3):
        m = x + 1
        pygame.draw.line(screen, (111,111,111), (sliderStart, sliderY*m), (sliderEnd,sliderY*m), width=7)
        sliders[x] = pygame.draw.circle(screen, color, (sliderX, sliderY*m), 10, width=0)
    mouseDown = pygame.mouse.get_pressed()[0]
    for x in range(3):
        if mousePos[1] >= sliders[x].top and mousePos[1] <= sliders[x].bottom and mouseDown == True:
            sliderX = mousePos[0]
    if sliderX < sliderStart:
        sliderX = sliderStart
    elif sliderX > sliderEnd:
        sliderX = sliderEnd
    value = myFont.render(str(sliderX-sliderStart), True, (color))
    screen.blit(value, (sliderX-value.get_width()/2, sliderY-30))
    pygame.display.update()
    clock.tick(60)
