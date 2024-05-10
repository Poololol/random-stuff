import pygame
import numpy
screen = pygame.display.set_mode(size=(500,500))
clock = pygame.time.Clock()
pygame.font.init()
screenSize = pygame.Surface.get_size(screen)
squareSize = min(screenSize)/5
myFont = pygame.font.Font(None, int(min(screenSize)/10))
rng = numpy.random.default_rng()
total = 0
term = [2,3,4,5,6,7,8,9]
definition = [10,15,20,25,30,35,40,45]
tiles = numpy.array((term, definition)).reshape(4,4)
rng.shuffle(tiles, 0)
rng.shuffle(tiles, 1)
numpy.rot90(tiles)
tiles = numpy.reshape(tiles, (2,8))
rng.shuffle(tiles, 0)
rng.shuffle(tiles, 1)
numpy.rot90(tiles)
numpy.transpose(tiles, (0,1))
rng.shuffle(tiles, 0)
rng.shuffle(tiles, 1)
numpy.rot90(tiles)
tiles = numpy.reshape(tiles, (4,4))
tileColor = (200,200,200)
textColor = (255,255,255)
timer = 0
numCardsUp = 0
card = 0
score = 0
card1 = 0
card2 = .1
class Tile():
    def __init__(self, value, state, x, y, flipped):
        self.value = value
        self.state = state
        self.x = x
        self.y = y
        self.flipped = flipped
    def Generate(self):
        self.rect = pygame.draw.rect(screen, tileColor, (self.x*(squareSize+25)+12.5, self.y*(squareSize+25)+12.5, squareSize, squareSize), width=0)
        if self.state == 1:
            text = myFont.render(str(self.value), True, textColor)
            screen.blit(text, ((self.x*(squareSize+25)+12.5)+(squareSize/2)-(text.get_width()/2), (self.y*(squareSize+25)+12.5)+(squareSize/2)-(text.get_height()/2)))
        return self
board = numpy.ndarray((4,4), dtype=Tile)
for x in range(4):
    for y in range(4):
        tile = Tile(tiles[y,x], 0, x, y, 0)
        board[y,x] = Tile.Generate(tile)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    mousePos = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePos, (1,1))
    states = numpy.zeros((4,4))
    for x in range(4):
        for y in range(4):
            mouseDown = pygame.mouse.get_pressed()[0]
            tile = Tile(tiles[y,x], board[y,x].state, x, y, board[y,x].flipped)
            board[y,x] = Tile.Generate(tile)
            #if board[y,x].flipped == 1:
                #print('{} {} {}'.format(x,y,board[y,x].flipped))
            for a in range(4):
                    for b in range(4):
                        states[a,b] = board[a,b].state
            if pygame.Rect.colliderect(mouseRect, tile.rect):
                if mouseDown and numpy.sum(states) < numCardsUp + 2:
                    tile.state = 1
            if numpy.sum(states) >= numCardsUp + 2:
                if tile.state == 1 and card == 0:
                    card1 = tile.value
                    card1Pos = (tile.x, tile.y)
                    card = 1
                elif tile.state == 1 and card == 1:
                    card2 = tile.value
                    card2Pos = (tile.x, tile.y)
                    card = 2
                if card1/card2 == 5 or card1/card2 == 0.2 or card1/card2 == 10000 and card == 2:
                    score = score + 1
                    numCardsUp = numCardsUp + 2
                    board[card1Pos].flipped = 1
                    board[card2Pos].flipped = 1
                    print(card1)
                    print(card2)
                    print(card1/card2)
                    print('    ')
                    for a in range(4):
                        for b in range(4):
                            print('{} {} {}'.format(a,b,board[a,b].flipped))
                    card = 0
                    card1 = .1
                    card2 = .001
                elif card == 2:
                    card = 0
                if timer >= 600:
                    timer = 0
                    for a in range(4):
                        for b in range(4):
                            if board[b,a].flipped == 0:
                                board[a,b].state = 0
                else:
                    timer = timer + 1
            board[y,x] = Tile.Generate(tile)
    pygame.display.update()
    clock.tick(60)