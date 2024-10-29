import pygame
import numpy
import inspect
import utils
#from tkinter import filedialog
from datetime import datetime
import time
screen = pygame.display.set_mode((880, 640), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
black = (0,0,0)
white = (255,255,255)
gray = (32,32,32)
lightGray = (64, 64, 64)
transparentWhite = (255,255,255,127)
transparentGray = (32,32,32,127)
tileColor1 = (170, 126, 88)
tileColor2 = (132, 67, 21)
previousMove1Color = (222, 200, 56, 100)
previousMove2Color = (199, 170, 42, 100)
previousMove1  = (-10*80, 1*80)
previousMove2 = (-10*80, 3*80)
checkHighlightColor = (255, 0, 0, 127)
turn = 'white'
whiteCastleable = True
blackCastleable = True
class Tile():
    def __init__(self) -> None:
        pass
    def Generate(self, x: int, y: int, tileSize: int, tileColor1: pygame.Color, tileColor2: pygame.Color):
        self.tile = pygame.draw.rect(screen, tileColor1 if (x+y)%2 == 0 else tileColor2, (x*tileSize, y*tileSize, tileSize, tileSize), width=0)
        return self
class Piece():
    def __init__(self) -> None:
        pass
    def Generate(self, xx: int, yy: int, tileSize: int, pie: str | pygame.Surface, start: bool, turn: str):
        if pie == 'Blank':
            self.x = xx
            self.y = yy
            self.piece = pie
            self.pieceStr = retrieve_name(pie)
            self.color = 'blank'
            self.moves = []
            return self
        screen.blit(pygame.transform.scale(pie, (tileSize, tileSize)), (xx*tileSize, yy*tileSize))
        self.x = xx
        self.y = yy
        self.piece = pie
        self.pieceStr = retrieve_name(pie)[0]
        self.color = 'white' if pie == WBishop or pie == WKing or pie == WKnight or pie == WPawn or pie == WQueen or pie == WRook else 'black'
        if start != True:
            self.moves = GenerateMoves(self.pieceStr, self.x, self.y, self, turn)
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
    def __str__(self):
        return f'({self.x}, {self.y}, {self.pieceStr})'
class Setting():
    def __init__(self, color, highlightColor) -> None:
        self.color = color
        self.highlightColor = highlightColor
    def GenerateDropdown(self, name, options, textColor, pos, size):
        self.name = name
        self.options = options
        self.type = 'dropdown'
        self.selected = options[0]
        self.pos = pos
        self.size = size
        self.utils = utils.Setting.Dropdown(options, self.color, self.highlightColor, textColor)
        return self
    def GenerateSlider(self, name, start, length, y):
        self.name = name
        self.start = start
        self.length = length
        self.y = y
        self.type = 'slider'
        return self
    def GenerateButton(self, name, color, mouseOverColor, textColor, func, pos = (1,1)):
        self.name = name
        self.type = 'button'
        self.utils = utils.Setting.Button(color, mouseOverColor, utils.white, textColor, name)
        self.func = func
        self.pos = pos
        return self
    def Display(settings: list):
        settings:list[Setting] = settings
        for setting in settings:
            if setting.type == 'slider':
                try:
                    setting.value, setting.x = utils.Slider(setting.start, setting.length, setting.x, setting.y, screen, knobColor=utils.gray, outline=black)
                except AttributeError:
                    setting.value, setting.x = utils.Slider(setting.start, setting.length, setting.start+(setting.length/2), setting.y, screen)
            elif setting.type == 'button':
                utils.Setting.Button.Render(setting.utils, screen, setting.pos, 17, mousePos)
            elif setting.type == 'dropdown':
                utils.Setting.Dropdown.Render(setting.utils, screen, setting.pos, mousePos, setting.size)
    def __str__(self) -> str:
        return f'{self.type}, {self.name}'
def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_back.f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]
def GenerateBoard(tileSize: int, piece: numpy.ndarray, tileColor1: pygame.Color, tileColor2: pygame.Color, turn: str):
    for x in range(8):
        for y in range(8):
            tiles[y,x] = Tile.Generate(Tile(), x, y, tileSize, tileColor1, tileColor2)
            pieces[y,x] = Piece.Generate(Piece(), x, y, tileSize, piece[y,x], True, turn)
def UpdateBoard(tileSize: int, piece: numpy.ndarray, tileColor1: pygame.Color, tileColor2: pygame.Color, turn: str):
    for x in range(8):
        for y in range(8):
            tiles[y,x] = Tile.Generate(Tile(), x, y, tileSize, tileColor1, tileColor2)
            pieces[y,x] = Piece.Generate(Piece(), x, y, tileSize, piece[y,x].piece, False, turn)
def SwapPieces(piece1: Piece, piece2: Piece) -> Piece:
    pieces[piece1.y, piece1.x] = Piece.Generate(Piece(), piece1.x, piece1.y, tileSize, piece2.piece, False, turn)
    pieces[piece2.y, piece2.x] = Piece.Generate(Piece(), piece2.x, piece2.y, tileSize, piece1.piece, False, turn)
    return pieces[piece2.y, piece2.x]
def HighlightSquare(color: pygame.Color, position: tuple[int, int]):
    highlight.fill((0,0,0,0))
    highlight.fill(color)
    screen.blit(highlight, position)
def PieceBlank(destX: int, destY: int):
    try:
        return True if pieces[destY, destX].piece == 'Blank' else False
    except IndexError:
        return False
def LegalMove(destX: int, destY: int):
    return (destX, destY) in moves
def PieceCapturable(piece: Piece, destX: int, destY: int):
    try:
        return True if (piece.color != pieces[destY, destX].color and pieces[destY, destX].piece != BKing and pieces[destY, destX].piece != WKing) and piece.piece != WPawn and piece.piece != BPawn else False
    except IndexError:
        return False
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
def GenerateMoves(pieceStr: str, x: int, y: int, piece: Piece, turn: str):
    moves = []
    if 'Rook' in pieceStr:
        for yy in range(1, 8):
            King = False
            try:
                King = 'King' in pieces[y+yy, x].pieceStr
            except IndexError:
                pass
            if PieceBlank(x, y+yy) or King:
                moves.append((0, yy))
            elif PieceCapturable(piece, x, y+yy):
                moves.append((0, yy))
                break
            else:
                break
        for yy in range(1, 8):
            try:
                if PieceBlank(x, y-yy):
                    moves.append((0, -yy))
                elif PieceCapturable(piece, x, y-yy) or 'King' in pieces[y-yy, x].pieceStr:
                    moves.append((0, -yy))
                    break
                else:
                    break
            except IndexError:
                pass
        for xx in range(1, 8):
            try:
                if PieceBlank(x+xx, y) or 'King' in pieces[y, x+xx].pieceStr:
                    moves.append((xx, 0))
                elif PieceCapturable(piece, x+xx, y):
                    moves.append((xx, 0))
                    break
                else:
                    break
            except IndexError:
                pass
        for xx in range(1, 8):
            try:
                if PieceBlank(x-xx, y)or 'King' in pieces[y, x-xx].pieceStr:
                    moves.append((-xx, 0))
                elif PieceCapturable(piece, x-xx, y):
                    moves.append((-xx, 0))
                    break
                else:
                    break
            except IndexError:
                pass
    if 'Bishop' in pieceStr:
        for xy in range(1,8):
            if PieceBlank(x+xy, y+xy):
                moves.append((xy, xy))
            elif PieceCapturable(piece, x+xy, y+xy):
                moves.append((xy, xy))
                break
            else:
                break
        for xy in range(1,8):
            if PieceBlank(x-xy, y+xy):
                moves.append((-xy, xy))
            elif PieceCapturable(piece, x-xy, y+xy):
                moves.append((-xy, xy))
                break
            else:
                break
        for xy in range(1,8):
            if PieceBlank(x+xy, y-xy):
                moves.append((xy, -xy))
            elif PieceCapturable(piece, x+xy, y-xy):
                moves.append((xy, -xy))
                break
            else:
                break
        for xy in range(1,8):
            if PieceBlank(x-xy, y-xy):
                moves.append((-xy, -xy))
            elif PieceCapturable(piece, x-xy, y-xy):
                moves.append((-xy, -xy))
                break
            else:
                break
    if 'Queen' in pieceStr:
        for xy in range(1,8):
            if PieceBlank(x+xy, y+xy):
                moves.append((xy, xy))
            elif PieceCapturable(piece, x+xy, y+xy):
                moves.append((xy, xy))
                break
            else:
                break
        for xy in range(1,8):
            if PieceBlank(x-xy, y+xy):
                moves.append((-xy, xy))
            elif PieceCapturable(piece, x-xy, y+xy):
                moves.append((-xy, xy))
                break
            else:
                break
        for xy in range(1,8):
            if PieceBlank(x+xy, y-xy):
                moves.append((xy, -xy))
            elif PieceCapturable(piece, x+xy, y-xy):
                moves.append((xy, -xy))
                break
            else:
                break
        for xy in range(1,8):
            if PieceBlank(x-xy, y-xy):
                moves.append((-xy, -xy))
            elif PieceCapturable(piece, x-xy, y-xy):
                moves.append((-xy, -xy))
                break
            else:
                break
        for yy in range(1, 8):
            if PieceBlank(x, y+yy):
                moves.append((0, yy))
            elif PieceCapturable(piece, x, y+yy):
                moves.append((0, yy))
                break
            else:
                break
        for yy in range(1, 8):
            if PieceBlank(x, y-yy):
                moves.append((0, -yy))
            elif PieceCapturable(piece, x, y-yy):
                moves.append((0, -yy))
                break
            else:
                break
        for xx in range(1, 8):
            if PieceBlank(x+xx, y):
                moves.append((xx, 0))
            elif PieceCapturable(piece, x+xx, y):
                moves.append((xx, 0))
                break
            else:
                break
        for xx in range(1, 8):
            if PieceBlank(x-xx, y):
                moves.append((-xx, 0))
            elif PieceCapturable(piece, x-xx, y):
                moves.append((-xx, 0))
                break
            else:
                break
    if 'King' in pieceStr:
        if PieceBlank(x, y-1) or PieceCapturable(piece, x, y-1):
            moves.append((0, -1))
        if PieceBlank(x+1, y-1) or PieceCapturable(piece, x+1, y-1):
            moves.append((1, -1))
        if PieceBlank(x+1, y) or PieceCapturable(piece, x+1, y):
            moves.append((1, 0))
        if PieceBlank(x+1, y+1) or PieceCapturable(piece, x+1, y+1):
            moves.append((1, 1))
        if PieceBlank(x, y+1) or PieceCapturable(piece, x, y+1):
            moves.append((0, 1))
        if PieceBlank(x-1, y+1) or PieceCapturable(piece, x-1, y+1):
            moves.append((-1, 1))
        if PieceBlank(x-1, y) or PieceCapturable(piece, x-1, y):
            moves.append((-1, 0))
        if PieceBlank(x-1, y-1) or PieceCapturable(piece, x-1, y-1):
            moves.append((-1, -1))
    if 'Knight' in pieceStr:
        if PieceBlank(x+1, y-2) or PieceCapturable(piece, x+1, y-2):
            moves.append((1, -2))
        if PieceBlank(x+2, y-1) or PieceCapturable(piece, x+2, y-1):
            moves.append((2, -1))
        if PieceBlank(x+2, y+1) or PieceCapturable(piece, x+2, y+2):
            moves.append((2, 1))
        if PieceBlank(x+1, y+2) or PieceCapturable(piece, x+1, y+2):
            moves.append((1, 2))
        if PieceBlank(x-1, y+2) or PieceCapturable(piece, x-1, y+2):
            moves.append((-1, 2))
        if PieceBlank(x-2, y+1) or PieceCapturable(piece, x-2, y+1):
            moves.append((-2, 1))
        if PieceBlank(x-2, y-1) or PieceCapturable(piece, x-2, y-1):
            moves.append((-2, -1))
        if PieceBlank(x-1, y-2) or PieceCapturable(piece, x-1, y-2):
            moves.append((-1, -2))
    if 'WPawn' in pieceStr:
        if PieceBlank(x, y-1):
            moves.append((0,-1))
    if 'BPawn' in pieceStr:
        if PieceBlank(x, y+1):
            moves.append((0,1))
    return moves
def SaveFile():
    filename = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('txt', '.txt')])
    file = open(filename.name, mode='w')
    file.write(turn)
    file.write('''
    ''')
    for x in range(8):
        for y in range(8):
            file.write(str(pieces[y,x].export()))
            file.write('''
            ''')
    file.close()
def OpenFile(filename:str=''):
    if filename == '':
        filename = filedialog.askopenfile(filetypes=[('txt', '.txt')])
        file = open(filename.name, mode='r')
    else:
        file = open(filename, mode='r')
    turn = file.readline()
    for x in range(8):
        for y in range(8):
            pieces[y,x].piece = 'Blank'
            data = file.readline().replace('[','').replace(']','').replace("'",'').replace(' ','').split(',')
            pieces[y,x] = Piece.load(pieces[y,x], data[0], data[1], data[2], data[3])
    file.close()
    turn = turn.replace('\n', '')
    return turn
def UpdateScreen(screen, previousMove1, previousMove2, tileSized):
    global screenSize
    global tileSize
    screenSize = screen.get_size()
    previousMove1 = (previousMove1[0]/tileSize, previousMove1[1]/tileSized)  
    previousMove2 = (previousMove2[0]/tileSize, previousMove2[1]/tileSized)
    tileSize = int(min(screenSize)/8)
    previousMove1 = (previousMove1[0]*tileSize, previousMove1[1]*tileSize)  
    previousMove2 = (previousMove2[0]*tileSize, previousMove2[1]*tileSize)
def Check(turn: str, king: tuple[int, int]):
    for piecer in numpy.nditer(pieces, flags=['refs_ok', 'external_loop']):
        for pieced in piecer:
            pieced: Piece = pieced
            if pieced.color != turn:
                for move in pieced.moves:
                    if (pieced.x + move[0], pieced.y+move[1]) == (king[0], king[1]):
                        return True
    return False
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
pieceImagesB = [BRook, BPawn, BKing, BQueen, BKnight, BBishop]
pieceImagesW = [WRook, WPawn, WKing, WQueen, WKnight, WBishop]
settingsButton = pygame.image.load('settings.png').convert_alpha()
settingsButton = utils.ReplaceColor(settingsButton, white, gray)
settings:list[Setting] = []
blankSetting = Setting(gray, lightGray)
piece = 1
moves = []
tiles = numpy.ndarray((8,8), Tile)
screenSize = screen.get_size()
tileSize = int(min(screenSize[0], screenSize[1])/8)
boardSize = tileSize*8, tileSize*8
pieces = numpy.ndarray((8,8), dtype=Piece)
highlight = pygame.Surface((tileSize, tileSize), flags=pygame.SRCALPHA)
highlightColor = transparentWhite
boardThemes = {'Brown': ((170, 126, 88), (132, 67, 21)), 'Black & White': ((222, 222, 222), (55, 55, 55)), 'Green': ((235,236,208), (115,149,82))}
pieceThemes = {'Black & White': ((0, 0, 0), (255, 255, 255))}
pieceTheme = 'Black & White'
settingsWindow = pygame.draw.rect(screen, (lightGray), (boardSize[0]+((screenSize[0]-boardSize[0])/4)-25, 64, (screenSize[0]-boardSize[0])/2+50, 250), width=0)
settings.append(Setting.GenerateDropdown(Setting(gray, lightGray), 'Board Theme', list(boardThemes), utils.white, (settingsWindow.left+10, settingsWindow.top+60), (settingsWindow.width-20, 20)))
settings.append(Setting.GenerateDropdown(Setting(gray, lightGray), 'Piece Theme', list(pieceThemes), utils.white, (settingsWindow.left+10, settingsWindow.top+90), (settingsWindow.width-20, 20)))
settings.append(Setting.GenerateButton(Setting(gray, lightGray), 'Export', utils.gray, utils.lightGray, utils.white, SaveFile, (settingsWindow.left+10, settingsWindow.top+120)))
settings.append(Setting.GenerateButton(Setting(gray, lightGray), 'Import', utils.gray, utils.lightGray, utils.white, OpenFile, (settingsWindow.left+85, settingsWindow.top+120)))
settings.append(Setting.GenerateSlider(Setting(gray, lightGray), name='Test', start=settingsWindow.left+10, length=settingsWindow.width-20, y=settingsWindow.top+40))
settingsOpen = False
mousePos = (0,0)
Setting.Display(settings)
startPieces = numpy.array(([BRook  , BKnight, BBishop,  BQueen,  BKing , BBishop, BKnight,  BRook],
                           [BPawn  ,  BPawn ,  BPawn ,  BPawn ,  BPawn ,  BPawn ,  BPawn ,  BPawn],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           ['Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank'],
                           [WPawn  ,  WPawn ,  WPawn ,  WPawn ,  WPawn ,  WPawn ,  WPawn ,  WPawn],
                           [WRook  , WKnight, WBishop, WQueen ,  WKing , WBishop, WKnight,  WRook]))
GenerateBoard(tileSize, startPieces, tileColor1, tileColor2, turn)
wking = (4,7)
bking = (4,0)
debug = False
while True:
    font = pygame.font.SysFont('arialbold', 20)
    boardSize = tileSize*8, tileSize*8
    pygame.draw.rect(screen, black, ((0, 0), screenSize))
    boardTheme = settings[0].selected
    previousPieceTheme = pieceTheme
    pieceTheme = settings[1].selected
    if pieceTheme != previousPieceTheme:
        for pieceImageB in pieceImagesB:
            utils.ReplaceColor(pieceImageB, pieceThemes[previousPieceTheme][0], pieceThemes[pieceTheme][0])
        for pieceImageW in pieceImagesW:
            utils.ReplaceColor(pieceImageW, pieceThemes[previousPieceTheme][1], pieceThemes[pieceTheme][1])
    UpdateBoard(tileSize, pieces, boardThemes[boardTheme][0], boardThemes[boardTheme][1], turn)
    settingsButton = pygame.transform.scale(settingsButton, (tileSize/1.25, tileSize/1.25))
    screen.blit(settingsButton, (screenSize[0]-settingsButton.get_width(), 0))
    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    mouseTile = (int(mouseX/tileSize), int(mouseY/tileSize))
    mouseTilePos = (int(mouseX/tileSize)*tileSize, int(mouseY/tileSize)*tileSize)
    mouseInBounds = True if max(mouseTile) < 8 else False
    mouseRect = pygame.Rect(mousePos, (1,1))
    legalMove = mouseTile in moves
    highlight = pygame.Surface((tileSize, tileSize), flags=pygame.SRCALPHA)
    if mouseInBounds:
        HighlightSquare(highlightColor, mouseTilePos)
    HighlightSquare(previousMove1Color, previousMove1)
    HighlightSquare(previousMove2Color, previousMove2)
    king = bking if turn == 'black' else wking
    if Check(turn, king):
        HighlightSquare(checkHighlightColor, (king[0]*tileSize, king[1]*tileSize))
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
        if piece1.piece == BPawn and pieces[piece1.y, piece1.x].piece == startPieces[piece1.y, piece1.x] and PieceBlank(piece1.x+0, piece1.y+2) and PieceBlank(piece1.x, piece1.y+1):
            tile = (piece1.x+0, piece1.y+2)
            dot = pygame.Surface((tileSize, tileSize), pygame.SRCALPHA)
            pygame.draw.circle(dot, transparentGray, (tileSize/2, tileSize/2), tileSize/6.5)
            numMoves += 1
            screen.blit(dot, (tile[0]*tileSize, tile[1]*tileSize))
            moves.append(tile)
        elif piece1.piece == WPawn and pieces[piece1.y, piece1.x].piece == startPieces[piece1.y, piece1.x] and PieceBlank(piece1.x+0, piece1.y-2) and PieceBlank(piece1.x, piece1.y-1):
            tile = (piece1.x+0, piece1.y-2)
            dot = pygame.Surface((tileSize, tileSize), pygame.SRCALPHA)
            pygame.draw.circle(dot, transparentGray, (tileSize/2, tileSize/2), tileSize/6.5)
            numMoves += 1
            screen.blit(dot, (tile[0]*tileSize, tile[1]*tileSize))
            moves.append(tile)
    if mouseRect.colliderect(pygame.Rect((screenSize[0]-settingsButton.get_width(), 0), (settingsButton.get_width(), settingsButton.get_height()))):
        settingsButton = utils.ReplaceColor(settingsButton, gray, lightGray)
    else:
        settingsButton = utils.ReplaceColor(settingsButton, lightGray, gray)
    if settingsOpen:
        settingsWindow = pygame.draw.rect(screen, lightGray, (boardSize[0]+((screenSize[0]-boardSize[0])/4)-25, 64, (screenSize[0]-boardSize[0])/2+50, 250), width=0)
        settings = list(reversed(settings))
        #t1= time.time()
        Setting.Display(settings)
        #t2 = time.time()
        #print(t2-t1)
        settings = list(reversed(list(settings)))
    if debug:
        text = font.render(str(clock.get_fps()), True, white)
        screen.blit(text, (1, 1))
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_F2:
                utils.TakeScreenshot(screen, datetime.now())
            if event.__dict__['key'] == pygame.K_F3:
                debug = not debug
            elif event.mod & pygame.KMOD_CTRL and event.dict['key'] == pygame.K_s:
                SaveFile()
            elif event.mod & pygame.KMOD_CTRL and event.dict['key'] == pygame.K_o:
                turn = OpenFile('check.txt')
        elif event.type == pygame.WINDOWRESIZED:
            UpdateScreen(screen, previousMove1, previousMove2, tileSize)
            boardSize = tileSize*8, tileSize*8
            settings = []
            settings.append(blankSetting.GenerateDropdown(name='Theme', options=['Black & White', 'Earthy']))
            settings.append(blankSetting.GenerateButton(name='Export Board'))
            settings.append(blankSetting.GenerateButton(name='Import Board'))
            settings.append(blankSetting.GenerateSlider(name='Test', start=boardSize[0]+((screenSize[0]-boardSize[0])/4), length=(screenSize[0]-boardSize[0])/2, y=settingsWindow.top+40))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for setting in settings:
                if setting.type == 'button':
                    if setting.utils.Clicked(event):
                        setting.func()
                elif setting.type == 'dropdown':
                    setting.selected = setting.options[setting.utils.Event(event)]
            if event.__dict__['button'] == 1 and mouseRect.colliderect(pygame.Rect((screenSize[0]-settingsButton.get_width(), 0), (settingsButton.get_width(), settingsButton.get_height()))) == True:
                settingsOpen = not settingsOpen
            elif event.__dict__['button'] == 1 and piece == 1 and mouseInBounds and not PieceBlank(mouseTile[0], mouseTile[1]):
                if pieces[mouseTile[1], mouseTile[0]].color == 'white' and turn == 'white':
                    piece1: Piece = pieces[mouseTile[1], mouseTile[0]]
                    piece = 2
                if pieces[mouseTile[1], mouseTile[0]].color == 'black' and turn == 'black':
                    piece1: Piece = pieces[mouseTile[1], mouseTile[0]]
                    piece = 2
            elif event.__dict__['button'] == 1 and piece == 2 and mouseInBounds:
                piece2 = pieces[mouseTile[1], mouseTile[0]]
                piece = 1
                if AvailableMove(piece1, mouseTile[0], mouseTile[1]):
                    pieceMoved = True
                    if PieceCapturable(piece1, mouseTile[0], mouseTile[1]) or PawnCapturable(piece1, mouseTile[0], mouseTile[1]):
                        pieces[mouseTile[1], mouseTile[0]].piece = 'Blank'
                    if Castleable(piece1, mouseTile[0], mouseTile[1]):
                        if piece1.color == 'white' and whiteCastleable:
                            SwapPieces(piece1, pieces[7,6])
                            SwapPieces(piece2, pieces[7,5])
                        elif piece1.color == 'black' and blackCastleable:
                            SwapPieces(piece1, pieces[0,6])
                            SwapPieces(piece2, pieces[0,5])
                        else:
                            pieceMoved = False
                    elif LongCastleable(piece1, mouseTile[0], mouseTile[1]):
                        if piece1.color == 'white' and whiteCastleable:
                            SwapPieces(piece1, pieces[7,2])
                            SwapPieces(piece2, pieces[7,3])
                        elif piece1.color == 'black' and blackCastleable:
                            SwapPieces(piece1, pieces[0,2])
                            SwapPieces(piece2, pieces[0,3])
                        else:
                            pieceMoved = False
                    else:
                        movedPiece = SwapPieces(piece1, piece2)
                        if movedPiece.pieceStr == 'BKing':
                            blackCastleable = False
                        if movedPiece.pieceStr == 'WKing':
                            whiteCastleable = False
                    if movedPiece.pieceStr == 'BKing':
                        bking = (movedPiece.x, movedPiece.y)
                    elif movedPiece.pieceStr == 'WKing':
                        wking = (movedPiece.x, movedPiece.y)
                    if pieceMoved:
                        turn = 'black' if turn == 'white' else 'white'
                        previousMove1 = (piece1.x*tileSize, piece1.y*tileSize)  
                        previousMove2 = (piece2.x*tileSize, piece2.y*tileSize)
    pygame.display.update()
    clock.tick()