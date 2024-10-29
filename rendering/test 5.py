import pygame
screen = pygame.display.set_mode((500,500), 0)
screenSize = screen.get_size()
def Random(x, y):
    randomNum = (x+8323) * (y+3487) * 8273159
    randomNum = randomNum**4
    randomNum = randomNum/213897
    randomNum = randomNum % 255
    return randomNum
while True:
    pygame.draw.rect(screen, (0,0,0), ((0,0), screenSize), width=0)
    for x in range(screenSize[0]):
        for y in range(screenSize[1]):
            screen.set_at((x,y), (int(Random(x,y)), int(Random(y,x)), int(Random(y+x,x*y))))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()