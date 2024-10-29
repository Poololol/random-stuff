import pygame
import utils
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
optionNum = 3
x = 100
y = 200
targetx = 300
targety =  200
percent = 0
print(utils.lerp(0,0,.5))
while True:
    screenSize = screen.get_size()
    #print(screenSize)
    pygame.draw.rect(screen, (0,0,0), ((0, 0), screenSize), width=0)
    pygame.draw.rect(screen, (55,55,55), (utils.lerp2d((x,y),(targetx, targety), percent/100),(25,25)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_RETURN:
                menu = False
    percent+=1
    pygame.display.update()
    pygame.time.Clock().tick(30)