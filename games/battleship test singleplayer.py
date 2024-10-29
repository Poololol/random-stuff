import pygame
import utils
import copy
screen = pygame.display.set_mode((1100, 550), pygame.RESIZABLE)
font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()
screenSize = screen.get_size()
gridSize = 50
ship = 1
direction = 0
ships = [(5, utils.lightGray), (4, utils.gray), (3, utils.darkGray), (3, utils.lightBlue), (2, utils.lightBlueishGray)]
shipPlacements = []
shipTiles = []
hits = []
misses = []
class Ship():
    def __init__(self, tile, length, color, direction):
        self.tile = tile
        self.pos = tile[0]*gridSize, tile[1]*gridSize
        self.length = length
        self.color = color
        self.dir = direction
        for i in range(length):
            if direction == 0:
                shipTiles.append((tile[0]+i-11,tile[1]))
            elif direction == 1:
                shipTiles.append((tile[0]-11,tile[1]+i))
            elif direction == 2:
                shipTiles.append((tile[0]-i-11,tile[1]))
            elif direction == 3:
                shipTiles.append((tile[0]-11,tile[1]-i))
    def Render(self, gridSize):
        for i in range(self.length):
            if self.dir == 0:
                pygame.draw.rect(screen, self.color, ((self.tile[0]+i)*gridSize, self.pos[1], gridSize, gridSize), width=0)
            elif self.dir == 1:
                pygame.draw.rect(screen, self.color, (self.pos[0], (self.tile[1]+i)*gridSize, gridSize, gridSize), width=0)
            elif self.dir == 2:
                pygame.draw.rect(screen, self.color, ((self.tile[0]-i)*gridSize, self.pos[1], gridSize, gridSize), width=0)
            elif self.dir == 3:
                pygame.draw.rect(screen, self.color, (self.pos[0], (self.tile[1]-i)*gridSize, gridSize, gridSize), width=0)
def ValidPlacement(tile, dir, length):
    if tile[0] < 12 or tile[1] == 0:
        return False
    if dir == 0 and tile[0]<23-length:
        return True
    if dir == 1 and tile[1]<12-length:
        return True
    if dir == 2 and tile[0]>10+length:
        return True
    if dir == 3 and tile[1]>length-1:
        return True
    return False
def ValidGuess(tile):
    if tile[0] == 0:
        return False
    if tile[0] > 10:
        return False
    if tile[1] == 0:
        return False
    if tile in hits:
        return False
    if tile in misses:
        return False
    return True
while True:
    screenSize = screen.get_size()
    mousePos = pygame.mouse.get_pos()
    mouseTile = (int(mousePos[0]/gridSize), int(mousePos[1]/gridSize))
    mouse = pygame.Rect(mousePos, (1,1))
    pygame.draw.rect(screen, utils.black, ((0,0), screenSize), width=0)
    for i in range(22):
        if i%11 != 0:
            text = font.render(str(i%11), True, utils.white)
            pos = ((i+.5)*gridSize-text.get_width()/2, .5*gridSize-text.get_height()/2)
            screen.blit(text, pos)
        for j in range(11):
            if i%11 == 0 and j != 0:
                text = font.render(utils.alphabet[j-1], True, utils.white)
                pos = ((i+.5)*gridSize-text.get_width()/2, (j+.5)*gridSize-text.get_height()/2)
                screen.blit(text, pos)
            tile = (i*gridSize, j*gridSize, gridSize, gridSize)
            selectedTile = (i,j)
            if ship and mouseTile[0]>11 and mouseTile[1]>0:
                for o in range(ships[ship-1][0]):
                    if direction == 0 and selectedTile == (mouseTile[0]+o, mouseTile[1]) and mouseTile[0]<23-ships[ship-1][0]:
                        pygame.draw.rect(screen, ships[ship-1][1], tile, width=0)
                    elif direction == 1 and selectedTile == (mouseTile[0], mouseTile[1]+o) and mouseTile[1]<12-ships[ship-1][0]:
                        pygame.draw.rect(screen, ships[ship-1][1], tile, width=0)
                    elif direction == 2 and selectedTile == (mouseTile[0]-o, mouseTile[1]) and mouseTile[0]>10+ships[ship-1][0]:
                        pygame.draw.rect(screen, ships[ship-1][1], tile, width=0)
                    elif direction == 3 and selectedTile == (mouseTile[0], mouseTile[1]-o) and mouseTile[1]>ships[ship-1][0]-1:
                        pygame.draw.rect(screen, ships[ship-1][1], tile, width=0)
            for boat in shipPlacements:
                boat.Render(gridSize)
    for miss in misses:
        pygame.draw.circle(screen, utils.white, (miss[0]*gridSize+gridSize/2, miss[1]*gridSize+gridSize/2), gridSize/4, width=0)
        pygame.draw.circle(screen, utils.white, ((miss[0]+11)*gridSize+gridSize/2, (miss[1])*gridSize+gridSize/2), gridSize/4, width=0)
    for hit in hits:
        pygame.draw.circle(screen, utils.red, (hit[0]*gridSize+gridSize/2, hit[1]*gridSize+gridSize/2), gridSize/4, width=0)
        pygame.draw.circle(screen, utils.red, ((hit[0]+11)*gridSize+gridSize/2, (hit[1])*gridSize+gridSize/2), gridSize/4, width=0)
    for x in range(22):
        for y in range(11):
            tile = (x*gridSize, y*gridSize, gridSize, gridSize)
            pygame.draw.rect(screen, utils.white, tile, width=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                utils.TakeScreenshot(screen)
            if event.key == pygame.K_r:
                direction+=1
                direction%=4
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ship:
                if ValidPlacement(mouseTile, direction, ships[ship-1][0]):
                    shipPlacements.append(Ship(mouseTile, ships[ship-1][0], ships[ship-1][1], direction))
                    ship+=1
                    if ship == 6:
                        ship = None
            else:
                if ValidGuess(mouseTile):
                    if mouseTile in shipTiles:
                        hits.append(mouseTile)
                        #print(hits)
                    else:
                        misses.append(mouseTile)
                        #print(misses)
    pygame.display.update()
    clock.tick(60)
