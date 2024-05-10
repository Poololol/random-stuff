import pygame
import utils
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
symbols = [pygame.image.load("pixil-frame-0.png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(1).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(2).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(3).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(4).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(5).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(6).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(7).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(8).png").convert_alpha(), 
           pygame.image.load("pixil-frame-0(9).png").convert_alpha(), ]
includeSame = False
hideMirror = True
while True:
    screenSize = screen.get_size()
    cellWidth = screenSize[0]/(len(symbols)+1)
    cellHeight = screenSize[1]/(len(symbols)+1)
    pygame.draw.rect(screen, (62, 93, 91), ((0,0),screenSize), width=0)
    #pygame.draw.polygon(screen, (62/4, 93/4, 91/4), ((cellWidth, cellHeight), (screenSize[0], cellHeight), (screenSize[0], screenSize[1])), width=0)
    for x in range(1,len(symbols)+1):
        pygame.draw.line(screen, utils.black, (0,cellHeight*x), (screenSize[0], cellHeight*x), width=1)
        pygame.draw.line(screen, utils.black, (cellWidth*x,0), (cellWidth*x, screenSize[1]), width=1)
    column = 1.5
    for symbol in symbols:
        symbol = pygame.transform.scale(symbol, (min(cellWidth,cellHeight)-10, min(cellWidth,cellHeight)-10))
        row = 0.5
        for x in range(len(symbols)+1):
            screen.blit(symbol, (row*cellWidth-symbol.get_width()/2, cellHeight*column-symbol.get_height()/2))
            row += 1
        row = 0.5
        for x in range(len(symbols)+1):
            if column > row and row > 1 and includeSame and hideMirror:
                pygame.draw.rect(screen, utils.darkGray, (column*cellWidth-cellWidth/2, cellHeight*row-cellHeight/2, cellWidth+1, cellHeight+1), width=0)
            elif column >= row and row > 1 and includeSame == False and hideMirror:
                pygame.draw.rect(screen, utils.darkGray, (column*cellWidth-cellWidth/2, cellHeight*row-cellHeight/2, cellWidth+1, cellHeight+1), width=0)    
            else:
                screen.blit(symbol, (column*cellWidth-symbol.get_width()/2, cellHeight*row-symbol.get_height()/2))
            row += 1
        #screen.blit(symbol, (cellWidth/2-symbol.get_width()/2, i*cellHeight-symbol.get_height()/2))
        column += 1
    for x in range(1,len(symbols)+1):
        pygame.draw.line(screen, utils.black, (0,cellHeight*x), (screenSize[0], cellHeight*x), width=1)
        pygame.draw.line(screen, utils.black, (cellWidth*x,0), (cellWidth*x, screenSize[1]), width=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            print(event.__dict__['key'])
            if event.__dict__['key'] == pygame.K_F2:
                utils.TakeScreenshot(screen)
    pygame.display.update()
    clock.tick(60)