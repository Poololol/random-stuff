import numpy
import pygame
import math
def ChangeColor(object, color):
    temp = object
    pixelColor = temp.get_at((50, 50))
    for x in range(100):
        for y in range(100):
            if temp.get_at((x, y)) == pygame.color.Color(pixelColor):
                temp.set_at((x, y), color)
    return temp
class GeneratePiece:
    def __init__(self, piece, position):
        self.image = pygame.transform.scale(piece, [squareSize, squareSize])
        self.pos = position
def GenerateBoard(x, y):
    if (x + y) % 2 == 0:
        pygame.draw.rect(screen, (64, 64, 64), (x*squareSize, y*squareSize, squareSize, squareSize), width=0)
    else:
        pygame.draw.rect(screen, (210, 180, 140), (x*squareSize, y*squareSize, squareSize, squareSize), width=0)
def HighlightSquare(color, position):
    highlight.fill((0,0,0,0))
    highlight.fill(color)
    screen.blit(highlight, position)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=(640+(80*3), 640), flags=pygame.RESIZABLE | pygame.SRCALPHA)
screenSize = pygame.display.get_window_size()
squareSize = min(screenSize)/8
white = (255, 255, 255)
transparentWhite = (255, 255, 255, 127)
transparentRed = (255, 0, 0, 127)
blackRook = pygame.image.load('Rook.png').convert_alpha()
blackPawn = pygame.image.load('Pawn.png').convert_alpha()
blackKnight = pygame.image.load('knight.png').convert_alpha()
blackBishop = pygame.image.load('bishop.png').convert_alpha()
blackKing = pygame.image.load('king.png').convert_alpha()
blackQueen = pygame.image.load('queen.png').convert_alpha()
whiteRook = ChangeColor(blackRook, white)
whitePawn = ChangeColor(blackPawn, white)
whiteKnight = ChangeColor(blackKnight, white)
whiteBishop = ChangeColor(blackBishop, white)
whiteKing = ChangeColor(blackKing, white)
whiteQueen = ChangeColor(blackQueen, white)
blackRook = pygame.image.load('Rook.png').convert_alpha()
blackPawn = pygame.image.load('Pawn.png').convert_alpha()
blackKnight = pygame.image.load('knight.png').convert_alpha()
blackBishop = pygame.image.load('bishop.png').convert_alpha()
blackKing = pygame.image.load('king.png').convert_alpha()
blackQueen = pygame.image.load('queen.png').convert_alpha()
blank = pygame.image.load('blank.png').convert_alpha()
highlight = pygame.Surface((squareSize, squareSize), flags=pygame.SRCALPHA)
highlightColor = transparentWhite
mouseX = int(pygame.mouse.get_pos()[0])
mouseY = int(pygame.mouse.get_pos()[1])
mousePos = (int(mouseX/squareSize)*squareSize, int(mouseY/squareSize)*squareSize)
board = numpy.array([[whiteRook, whiteKnight, whiteBishop, whiteKing, whiteQueen, whiteBishop, whiteKnight, whiteRook], [whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn], [blank, blank, blank, blank, blank, blank, blank, blank],[blank, blank, blank, blank, blank, blank, blank, blank],[blank, blank, blank, blank, blank, blank, blank, blank], [blank, blank, blank, blank, blank, blank, blank, blank], [blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn], [blackRook, blackKnight, blackBishop, blackKing, blackQueen, blackBishop, blackKnight, blackRook]])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            highlightColor = transparentRed
        else:
            highlightColor = transparentWhite
    screen.fill((102, 51, 153))
    for y in range(8):
        for x in range(8):
            GenerateBoard(x, y)
            piece = GeneratePiece(board[y, x], [x*squareSize, y*squareSize])
            screen.blit(piece.image, piece.pos)
    screenSize = pygame.display.get_window_size()
    squareSize = int(min(screenSize)/8)
    mouseX = int(pygame.mouse.get_pos()[0])
    mouseY = int(pygame.mouse.get_pos()[1])
    mousePos = (int(mouseX/squareSize)*squareSize, int(mouseY/squareSize)*squareSize)
    highlight = pygame.Surface((squareSize, squareSize), flags=pygame.SRCALPHA)
    HighlightSquare(highlightColor, mousePos)
    pygame.display.update()
    clock.tick(60)