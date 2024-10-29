import pygame
import utils
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 15)
screenSize = screen.get_size()
backgroundColor = utils.darkGray
boardColor = utils.lightBlueishGray
padding = 8
chipRadius = 60/2
p1Color = utils.red
p2Color = utils.yellow
turn = 0
board = [[], [], [], [], [], [], []]
while True:
    screenSize = screen.get_size()
    padding = 8 * (min(screenSize)/500)
    chipRadius = (60/2)*(min(screenSize)/500)
    pygame.draw.rect(screen, backgroundColor, ((0,0), screenSize), width=0)
    pygame.draw.rect(screen, boardColor, pygame.Rect((padding, chipRadius*2+padding*2), (screenSize[0]-padding*2, screenSize[1]-chipRadius*2-padding*3)), border_radius=5)
    for x in range(7):
        for y in range(6):
            pygame.draw.circle(screen, backgroundColor, (x*(chipRadius*2+padding)+chipRadius+padding*2, (y+1)*(chipRadius*2+padding)+padding*2+chipRadius), chipRadius, width=0)
    i=0
    for column in board:
        j=0
        for chip in column:
            pygame.draw.circle(screen, p1Color if chip == 0 else p2Color, (i*(chipRadius*2+padding)+chipRadius+padding*2, (6-j)*(chipRadius*2+padding)+padding*2+chipRadius), chipRadius, width=0)
            j+=1
        i+=1
    mousePos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, p1Color if turn == 0 else p2Color, ((int((mousePos[0]-padding*1.5)/(chipRadius*2+padding)))*(chipRadius*2+padding)+chipRadius*2-padding*1.5-1, chipRadius+padding), chipRadius, width=0)
    columnNum = int((mousePos[0]-padding*1.5)/(chipRadius*2+padding))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board[columnNum].append(turn)
            turn = not turn
    pygame.display.update()
    clock.tick(60)
