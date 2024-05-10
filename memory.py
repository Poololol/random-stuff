import pygame
import numpy
screen = pygame.display.set_mode(size=(500,500))
clock = pygame.time.Clock()
pygame.font.init()
screenSize = pygame.Surface.get_size(screen)
squareSize = min(screenSize)/5
myFont = pygame.font.Font(None, int(min(screenSize)/10))
board = numpy.zeros((4,4))
term = [1,2,3,4,5,6,7,8]
definition = [5,10,15,20.25,30,35,40]
tiles = numpy.array(term)
tileColor = (222,222,222)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    mousePos = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePos, (1,1))
    for x in range(4):
        for y in range(4):
            mouseDown = pygame.mouse.get_pressed()[0]
            tile = pygame.draw.rect(screen, tileColor, (x*(squareSize+25)+12.5, y*(squareSize+25)+12.5, squareSize, squareSize), width=0)
            if pygame.Rect.colliderect(mouseRect, tile):
                tileColor = (222,222,222)
                if mouseDown:
                    board[y,x] = 1
                else:
                    board[y,x] = 0
            else:
                tileColor = (151,151,151)
            pygame.draw.rect(screen, tileColor, (x*(squareSize+25)+12.5, y*(squareSize+25)+12.5, squareSize, squareSize), width=0)
            if board[y,x] == 1:
                text = myFont.render("1", True, (2,2,2))
                screen.blit(text, (200,200))
    print(board)
    pygame.display.update()
    clock.tick(60)