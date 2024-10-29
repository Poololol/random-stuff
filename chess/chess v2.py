import pygame
import numpy
import sys
import inspect
from tkinter import filedialog
from datetime import datetime
sys.path.insert(0, '/Users/braed/OneDrive/programs/utils')
sys.path.insert(0, '/Users/638278/OneDrive/programs/utils')
from screenshot import TakeScreenshot
screen = pygame.display.set_mode((880, 640), pygame.RESIZABLE)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
transparentWhite = (255,255,255,127)
transparentGray = (32,32,32,127)
previousMove1Color = (222, 200, 56, 100)
previousMove2Color = (199, 170, 42, 100)
previousMove1  = (-1*80, 1*80)
previousMove2 = (-1*80, 3*80)
class Tile():
    def __init__(self) -> None:
        pass
    def Generate(self, x: int, y: int, tileSize: int):
        self.tile = pygame.draw.rect(screen, (170, 126, 88) if (x+y)%2 == 0 else (132, 67, 21), (x*tileSize, y*tileSize, tileSize, tileSize), width=0)
        return self
class Piece():
    def __init__(self) -> None:
        pass
    def Generate(self, xx: int, yy: int, tileSize: int, pie: str | pygame.Surface):
        if pie == 'Blank':
            self.x = xx
            self.y = yy
            self.piece = pie
            self.pieceStr = retrieve_name(pie)
            self.color = 'blank'
            return self
        screen.blit(pygame.transform.scale(pie, (tileSize, tileSize)), (xx*tileSize, yy*tileSize))
        self.x = xx
        self.y = yy
        self.piece = pie
        self.pieceStr = retrieve_name(pie)
        self.color = 'white' if pie == WBishop or pie == WKing or pie == WKnight or pie == WPawn or pie == WQueen or pie == WRook else 'black'
        if pie == BPawn:
            self.moves = [(0, 1)]
        elif pie == WPawn:
            self.moves = [(0, -1)]
        elif pie == BBishop or pie == WBishop:
            self.moves = [(-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), 
                          (-7, 7), (-6, 6), (-5, 5), (-4, 4), (-3, 3), (-2, 2), (-1, 1), (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)]
        elif pie == BRook or pie == WRook:
            self.moves = [(-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), 
                          (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        elif pie == BKing or pie == WKing:
            self.moves = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        elif pie == BQueen or pie == WQueen:
            self.moves = [(-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), 
                          (-7, 7), (-6, 6), (-5, 5), (-4, 4), (-3, 3), (-2, 2), (-1, 1), (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), 
                          (-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), 
                          (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        elif pie == BKnight or pie == WKnight:
            self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        return self
    def export(self):
        return [self.x, self.y, self.pieceStr, self.color]
    def load(self, x: int, y: int, piece: str, color: str):
        self.x = x
        self.y = y
        if piece == 'Blank':
            self.piece = 'Blank'
        elif piece == 'WBishop':
            self.piece = WBishop
        elif piece == 'BBishop':
            self.piece = BBishop
        elif piece == 'WKnight':
            self.piece = WKnight
        elif piece == 'BKnight':
            self.piece = BKnight
        elif piece == 'WRook':
            self.piece = WRook
        elif piece == 'BRook':
            self.piece = BRook
        elif piece == 'WKing':
            self.piece = WKing
        elif piece == 'BKing':
            self.piece = BKing
        elif piece == 'WQueen':
            self.piece = WQueen
        elif piece == 'BQueen':
            self.piece = BQueen
        elif piece == 'WPawn':
            self.piece = WPawn
        elif piece == 'BPawn':
            self.piece = BPawn
        self.pieceStr = piece
        self.color = color
        return self
def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_back.f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]
def GenerateBoard(tileSize: int, piece: numpy.ndarray):
    for x in range(8):
        for y in range(8):
            tiles[y,x] = Tile.Generate(Tile(), x, y, tileSize)
            pieces[y,x] = Piece.Generate(Piece(), x, y, tileSize, piece[y,x])
def UpdateBoard(tileSize: int, piece: numpy.ndarray):
    for x in range(8):
        for y in range(8):
            tiles[y,x] = Tile.Generate(Tile(), x, y, tileSize)
            pieces[y,x] = Piece.Generate(Piece(), x, y, tileSize, piece[y,x].piece)
def Swap(piece1: Piece, piece2: Piece):
    temp = piece1
    pieces[piece1.y, piece1.x] = piece2
    pieces[piece2.y, piece2.x] = temp
def HighlightSquare(color: pygame.Color, position: tuple[int, int]):
    highlight.fill((0,0,0,0))
    highlight.fill(color)
    screen.blit(highlight, position)
def ChangeColor(surface: pygame.Surface, repColor: pygame.Color):
    color = surface.get_at((int(surface.get_width()/2), int(surface.get_height()/2)))
    pixels = pygame.PixelArray(surface)
    pixels.replace(color, repColor, 0, (0.1,0.1,0.1))
    return pixels.make_surface()
def PieceBlank(destX: int, destY: int):
    try:
        return True if pieces[destY, destX].piece == 'Blank' else False
    except IndexError:
        return False
def LegalMove(destX: int, destY: int):
    return (destX, destY) in moves
def PieceCapturable(piece: Piece, destX: int, destY: int):
    return True if (piece.color != pieces[destY, destX].color and pieces[destY, destX].piece != BKing and pieces[destY, destX].piece != WKing) and piece.piece != WPawn and piece.piece != BPawn else False
def Castleable(piece: Piece, destX: int, destY: int):
    if piece.piece != BKing and piece.piece != WKing:
        return False 
    if pieces[destY, destX].piece != BRook and pieces[destY, destX].piece != WRook:
        return False
    if piece.color != pieces[destY, destX].color:
        return False
    if piece.color == 'white' and (pieces[7, 5].piece != 'Blank' or pieces[7, 6].piece != 'Blank'):
        return False
    if piece.color == 'black' and (pieces[0, 5].piece != 'Blank' or pieces[0, 6].piece != 'Blank'):
        return False
    if piece.color == 'white' and piece.piece != pieces[7,4].piece:
        return False
    if piece.color == 'black' and piece.piece != pieces[0,4].piece:
        return False
    if piece.color == 'white' and pieces[destY, destX].piece != pieces[7,7].piece:
        return False
    if piece.color == 'black' and pieces[destY, destX].piece != pieces[0,7].piece:
        return False
    if (destY, destX) == (7,0) or (destY, destX) == (0,0):
        return False
    return True
def LongCastleable(piece: Piece, destX: int, destY: int):
    if piece.piece != BKing and piece.piece != WKing:
        return False 
    if pieces[destY, destX].piece != BRook and pieces[destY, destX].piece != WRook:
        return False
    if piece.color != pieces[destY, destX].color:
        return False
    if piece.color == 'white' and (pieces[7, 1].piece != 'Blank' or pieces[7, 2].piece != 'Blank' or pieces[7, 3].piece != 'Blank'):
        return False
    if piece.color == 'black' and (pieces[0, 1].piece != 'Blank' or pieces[0, 2].piece != 'Blank' or pieces[0, 3].piece != 'Blank'):
        return False
    if piece.color == 'white' and piece.piece != pieces[7,4].piece:
        return False
    if piece.color == 'black' and piece.piece != pieces[0,4].piece:
        return False
    if piece.color == 'white' and pieces[destY, destX].piece != pieces[7,0].piece:
        return False
    if piece.color == 'black' and pieces[destY, destX].piece != pieces[0,0].piece:
        return False
    if (destY, destX) == (7,7) or (destY, destX) == (0,7):
        return False
    return True
def PawnCapturable(piece: Piece, destX: int, destY: int):
    dest = (destX, destY)
    return True if (((dest == (piece.x+1, piece.y+1) or dest == (piece.x-1, piece.y+1)) and piece.piece == BPawn) or ((dest == (piece.x+1, piece.y-1) or dest == (piece.x-1, piece.y-1)) and piece.piece == WPawn)) and (piece.color != pieces[destY, destX].color and pieces[destY, destX].piece != BKing and pieces[destY, destX].piece != WKing) else False
def AvailableMove(piece: Piece, destX: int, destY: int):
    return True if ((PieceBlank(destX, destY) == True or PieceCapturable(piece, destX, destY)) and LegalMove(destX, destY)) or (Castleable(piece, destX, destY) or LongCastleable(piece, destX, destY)) or (PawnCapturable(piece, destX, destY) and not PieceBlank(destX, destY)) else False
BRook = pygame.image.load('rook.png').convert_alpha()
BPawn = pygame.image.load('pawn.png').convert_alpha()
BKnight = pygame.image.load('knight.png').convert_alpha()
BBishop = pygame.image.load('bishop.png').convert_alpha()
BKing = pygame.image.load('king.png').convert_alpha()
BQueen = pygame.image.load('queen.png').convert_alpha()
WRook = pygame.image.load('WRook.png').convert_alpha()
WPawn = pygame.image.load('WPawn.png').convert_alpha()
WKing = pygame.image.load('WKing.png').convert_alpha()
WQueen = pygame.image.load('WQueen.png').convert_alpha()
WKnight = pygame.image.load('WKnight.png').convert_alpha()
WBishop = pygame.image.load('WBishop.png').convert_alpha()
piece = 1
moves = []
tiles = numpy.ndarray((8,8), Tile)
screenSize = screen.get_size()
tileSize = int(min(screenSize[0], screenSize[1])/8)
pieces = numpy.ndarray((8,8), Piece)
highlight = pygame.Surface((tileSize, tileSize), flags=pygame.SRCALPHA)
highlightColor = transparentWhite
startPieces = numpy.array(([BRook  , BKnight, BBishop,  BQueen,  BKing , BBishop, BKnight,  BRook],
                           [BPawn  ,  BPawn ,  BPawn ,  BPawn ,  BPawn ,  BPawn ,  BPawn ,  BPawn],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           [WPawn  ,  WPawn ,  WPawn ,  WPawn ,  WPawn ,  WPawn ,  WPawn ,  WPawn],
                           [WRook  , WKnight, WBishop, WQueen , WKing  , WBishop, WKnight,  WRook]))
GenerateBoard(tileSize, startPieces)
while True:
    pygame.draw.rect(screen, black, ((0, 0), screenSize))
    UpdateBoard(tileSize, pieces)
    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    mouseTile = (int(mouseX/tileSize), int(mouseY/tileSize))
    mouseTilePos = (int(mouseX/tileSize)*tileSize, int(mouseY/tileSize)*tileSize)
    mouseInBounds = True if max(mouseTile) < 8 else False
    legalMove = mouseTile in moves
    highlight = pygame.Surface((tileSize, tileSize), flags=pygame.SRCALPHA)
    HighlightSquare(highlightColor, mouseTilePos)
    HighlightSquare(previousMove1Color, previousMove1)
    HighlightSquare(previousMove2Color, previousMove2)
    if piece == 2:
        moves = []
        numMoves = 0
        for move in piece1.moves:
            tile = (piece1.x+move[0], piece1.y+move[1])
            dot = pygame.Surface((tileSize, tileSize), pygame.SRCALPHA)
            if PieceBlank(tile[0], tile[1]):
                pygame.draw.circle(dot, transparentGray, (tileSize/2, tileSize/2), tileSize/6.5)
                numMoves += 1
            screen.blit(dot, (tile[0]*tileSize, tile[1]*tileSize))
            moves.append(tile)
        if piece1.piece == BPawn and pieces[piece1.y, piece1.x].piece == startPieces[piece1.y, piece1.x] and PieceBlank(piece1.x+0, piece1.y+2):
            tile = (piece1.x+0, piece1.y+2)
            dot = pygame.Surface((tileSize, tileSize), pygame.SRCALPHA)
            pygame.draw.circle(dot, transparentGray, (tileSize/2, tileSize/2), tileSize/6.5)
            numMoves += 1
            screen.blit(dot, (tile[0]*tileSize, tile[1]*tileSize))
            moves.append(tile)
        if piece1.piece == WPawn and pieces[piece1.y, piece1.x].piece == startPieces[piece1.y, piece1.x] and PieceBlank(piece1.x+0, piece1.y-2):
            tile = (piece1.x+0, piece1.y-2)
            dot = pygame.Surface((tileSize, tileSize), pygame.SRCALPHA)
            pygame.draw.circle(dot, transparentGray, (tileSize/2, tileSize/2), tileSize/6.5)
            numMoves += 1
            screen.blit(dot, (tile[0]*tileSize, tile[1]*tileSize))
            moves.append(tile)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            TakeScreenshot(screen, event, datetime.now())
            if event.mod & pygame.KMOD_CTRL and event.dict['key'] == pygame.K_s:
                filename = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('txt', '.txt')])
                file = open(filename.name, mode='w')
                for x in range(8):
                    for y in range(8):
                        file.write(str(pieces[y,x].export()))
                        file.write('''
                        ''')
                file.close()
            if event.mod & pygame.KMOD_CTRL and event.dict['key'] == pygame.K_o:
                filename = filedialog.askopenfile(filetypes=[('txt', '.txt')])
                file = open(filename.name, mode='r')
                for x in range(8):
                    for y in range(8):
                        pieces[y,x].piece = 'Blank'
                        data = file.readline().replace('[','').replace(']','').replace("'",'').replace(' ','').split(',')
                        pieces[y,x] = Piece.load(pieces[y,x], data[0], data[1], data[2], data[3])
                file.close()
        elif event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            previousMove1 = (previousMove1[0]/tileSize, previousMove1[1]/tileSize)  
            previousMove2 = (previousMove2[0]/tileSize, previousMove2[1]/tileSize)
            tileSize = int(min(screenSize)/8)
            previousMove1 = (previousMove1[0]*tileSize, previousMove1[1]*tileSize)  
            previousMove2 = (previousMove2[0]*tileSize, previousMove2[1]*tileSize)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.__dict__['button'] == 1 and piece == 1 and mouseInBounds and not PieceBlank(mouseTile[0], mouseTile[1]):
                piece1 = pieces[mouseTile[1], mouseTile[0]]
                #print('piece1: {}'.format(piece1.piece))
                piece = 2
            elif event.__dict__['button'] == 1 and piece == 2 and mouseInBounds:
                piece2 = pieces[mouseTile[1], mouseTile[0]]
                #print('piece2: {}'.format(piece2.piece))
                piece = 1
                if AvailableMove(piece1, mouseTile[0], mouseTile[1]):
                    if PieceCapturable(piece1, mouseTile[0], mouseTile[1]) or PawnCapturable(piece1, mouseTile[0], mouseTile[1]):
                        pieces[mouseTile[1], mouseTile[0]].piece = 'Blank'
                    if Castleable(piece1, mouseTile[0], mouseTile[1]):
                        if piece1.color == 'white':
                            Swap(piece1, pieces[7,6])
                            Swap(piece2, pieces[7,5])
                        else:
                            Swap(piece1, pieces[0,6])
                            Swap(piece2, pieces[0,5])
                    elif LongCastleable(piece1, mouseTile[0], mouseTile[1]):
                        if piece1.color == 'white':
                            Swap(piece1, pieces[7,2])
                            Swap(piece2, pieces[7,3])
                        else:
                            Swap(piece1, pieces[0,2])
                            Swap(piece2, pieces[0,3])
                    else:
                        Swap(piece1, piece2)
                    previousMove1 = (piece1.x*tileSize, piece1.y*tileSize)  
                    previousMove2 = (piece2.x*tileSize, piece2.y*tileSize)
    pygame.display.update()
    clock.tick(60)