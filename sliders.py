import pygame
screen = pygame.display.set_mode(size=(500, 500))
clock = pygame.time.Clock()
pygame.font.init()
screenSize = screen.get_size()
sliders = []
class Slider():
    def __init__(self, start, end, lineColor, sliderColor, lineSize, sliderSize):
        pygame.draw.line(screen, lineColor, start, end, width=lineSize)
        self.slider = pygame.draw.circle(screen, sliderColor, start, sliderSize, width=0)
        self.start = start
        self.end = end
    def move(self, x):
        self.slider.move_ip((x,self.slider.top))
        if x < self.start[0]:
            x = self.start[0]
        elif x > self.end[0]:
            x = self.end[0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    myFont = pygame.font.Font(None, int(screenSize[1]/20))
    mousePos = pygame.mouse.get_pos()
    #pygame.draw.rect(screen, (0,0,0), (0,0,500,500), width=0)
    mouseDown = pygame.mouse.get_pressed()[0]
    if len(sliders) < 3:
        slider = Slider((50,25*(len(sliders)+1)), (150,25*(len(sliders)+1)), (111,111,111), (222,222,222), 3, 6)
        sliders.append(slider)
    pygame.display.update()
    clock.tick(60)