import pygame
from utils import *
import numpy as np
import math
from contextlib import suppress
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
board = np.zeros((4,8))
p1Color = green
p2Color = red
pieceSize = 15
clickedRing = 4
turn = 1
won = (False, 0)
debug = False
def CheckWin(turn: int, move: tuple[int, int]):
    win = [((), False)]
    for i in CheckAdjacent(turn, move):
        if i[1]:
            p = 0
            dx, dy = i[0][0]-move[0], i[0][1]-move[1]
            for j in range(1,4):
                try:
                    if board[move[0]+(j*dx)][(move[1]+(j*dy))%8] == turn:
                        p += 1
                except:
                    pass
                if p == 3:
                    return True
def CheckAdjacent(turn: int, move: tuple[int, int]):
    c1,c2,c3,c4,c5,c6,c7,c8=False,False,False,False,False,False,False,False
    with suppress(IndexError): c1 = board[move[0]+0][(move[1]+1)%8] == turn
    with suppress(IndexError): c2 = board[move[0]+0][(move[1]-1)%8] == turn
    with suppress(IndexError): c3 = board[move[0]+1][(move[1]+0)%8] == turn
    with suppress(IndexError): c4 = board[move[0]-1][(move[1]+0)%8] == turn
    with suppress(IndexError): c5 = board[move[0]+1][(move[1]+1)%8] == turn
    with suppress(IndexError): c6 = board[move[0]+1][(move[1]-1)%8] == turn
    with suppress(IndexError): c7 = board[move[0]-1][(move[1]+1)%8] == turn
    with suppress(IndexError): c8 = board[move[0]-1][(move[1]-1)%8] == turn

    return [((move[0]  , move[1]+1), c1), 
            ((move[0]  , move[1]-1), c2), 
            ((move[0]+1, move[1]+0), c3),
            ((move[0]-1, move[1]+0), c4), 
            ((move[0]+1, move[1]+1), c5), 
            ((move[0]+1, move[1]-1), c6), 
            ((move[0]-1, move[1]+1), c7), 
            ((move[0]-1, move[1]-1), c8)]
while True:
    screenSize = screen.get_size()
    pygame.draw.rect(screen, black, ((0,0), screenSize), width=0)
    pygame.draw.circle(screen, white, (screenSize[0]/2, screenSize[1]/2), min(screenSize)/2.2, width=2)
    pygame.draw.circle(screen, white, (screenSize[0]/2, screenSize[1]/2), min(screenSize)/2.2-50, width=2)
    pygame.draw.circle(screen, white, (screenSize[0]/2, screenSize[1]/2), min(screenSize)/2.2-100, width=2)
    pygame.draw.circle(screen, white, (screenSize[0]/2, screenSize[1]/2), min(screenSize)/2.2-150, width=2)
    pygame.draw.line(screen, white, (screenSize[0]/2, screenSize[1]/2-min(screenSize)/2.2), (screenSize[0]/2, screenSize[1]/2+min(screenSize)/2.2), width=2)
    pygame.draw.line(screen, white, (screenSize[0]/2-min(screenSize)/2.2, screenSize[1]/2), (screenSize[0]/2+min(screenSize)/2.2, screenSize[1]/2), width=2)
    pygame.draw.line(screen, white, (screenSize[0]/2-math.cos(math.pi/4)*min(screenSize)/2.2, screenSize[1]/2-math.cos(math.pi/4)*min(screenSize)/2.2), (screenSize[0]/2-math.cos(3*math.pi/4)*min(screenSize)/2.2, screenSize[1]/2-math.cos(3*math.pi/4)*min(screenSize)/2.2), width=2)
    pygame.draw.line(screen, white, (screenSize[0]/2+math.cos(math.pi/4)*min(screenSize)/2.2, screenSize[1]/2-math.cos(math.pi/4)*min(screenSize)/2.2), (screenSize[0]/2+math.cos(5*math.pi/4)*min(screenSize)/2.2, screenSize[1]/2-math.cos(5*math.pi/4)*min(screenSize)/2.2), width=2)
    for ringNum, ring in enumerate(board):
        for segmentNum, piece in enumerate(ring):
            x = screenSize[0]/2+((ringNum+1)*50)*math.cos((segmentNum+.5)*(math.pi*2)/8)
            y = screenSize[1]/2-((ringNum+1)*50)*math.sin((segmentNum+.5)*(math.pi*2)/8)
            if piece == 1:
                pygame.draw.line(screen, p1Color, (x-pieceSize, y-pieceSize), (x+pieceSize, y+pieceSize), width=2)
                pygame.draw.line(screen, p1Color, (x-pieceSize, y+pieceSize), (x+pieceSize, y-pieceSize), width=2)
            elif piece == 2:
                pygame.draw.circle(screen, p2Color, (x, y), pieceSize+5, width=2)
    if debug:
        screen.blit(font.render(str(round(clock.get_fps(),2)), True, white), (5, 5))
    if won[0]:
        screen.blit(font.render(f'Player {won[1]} Won!', True, p1Color if won[1] == 1 else p2Color), (100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            key = event.__dict__['key']
            if key == pygame.K_F3:
                debug = not debug
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.__dict__['pos'][0]-screenSize[0]/2
            y = -event.__dict__['pos'][1]+screenSize[1]/2
            c = math.sqrt((x**2)+(y**2))
            if c<min(screenSize)/2.2:
                clickedRing = math.floor((c/50)-(6/11))
            a=math.atan(x/y)
            if a > math.atan(1):
                clickedSeg = 0
            elif 0 < a < math.atan(1):
                clickedSeg = 1
            elif -math.atan(1) < a:
                clickedSeg = 2
            elif a < -math.atan(1):
                clickedSeg = 3
            if y < 0:
                clickedSeg += 4
            if c<min(screenSize)/2.2:
                board[clickedRing][clickedSeg] = turn+1
                if CheckWin(turn+1, (clickedRing, clickedSeg)):
                    won = (True, turn+1)
                turn = not turn
    pygame.display.update()
    clock.tick(60)
