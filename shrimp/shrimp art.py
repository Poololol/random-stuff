import pygame
import utils
import random
import copy
import math
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
screenSize = screen.get_size()
menuBackgroundColor = utils.darkGray
backgroundColor = utils.wood
deck:list[list[tuple]] = []
colors:list[tuple] = [utils.red, utils.pink, utils.yellow, utils.lightBlue, utils.orange, utils.green, utils.purple]
players:dict[list] = {}
menu = True
optionNum = 3
optionNum2 = 4
optionNum3 = 6
numOfEachColor = 24
cardSpacing = 5
turn = 1
a = 0
numCardsPerPerson = 4
cooldown = 0
cooldown2 = 0
cooldown3 = 0
colors1 = copy.deepcopy(colors)
colors2 = copy.deepcopy(colors)
flipCardBank = False
flipCardSteal = False
chooseSteal = False
borderSize = 0
showCardTime = 45
global numPlayers
c=0
seed = random.randint(0,999)
#seed = 866
'''intersting seeds
574 = 1 color  p3
596 = 1 color  p4
834 = 1 color  p4
752 = 2 colors p1 2-2
707 = 2 colors p2 2-2
357 = 2 colors p3 2-2
822 = 2 colors p4 2-2
964 = 2 colors p1 3-1
655 = 2 colors p2 3-1
492 = 2 colors p3 3-1
971 = 2 colors p4 3-1
963 = 2 colors p1,2 3-1 2-2
427 = 2 colors p2,4 3-1 2-2
246 = 2 colors p4,3 3-1 2-2
972 = 3 colors p1-4
866 = 4 colors p1-4
'''
print('Seed:', seed)
random.seed(seed)
for color in colors:
    for x in range(numOfEachColor):
        index = colors1.index(color)
        colors1.remove(color)
        colors2.remove(color)
        rc = colors1[random.randint(0,len(colors1)-1)]
        deck.append([color, rc])
        index2 = colors2.index(rc)
        colors2.remove(rc)
        deck[c].append(colors2[random.randint(0,len(colors2)-1)])
        colors1.insert(index-1, color)
        colors2.insert(index2-1, rc)
        colors2.insert(index-1, color)
        c+=1
random.shuffle(deck)
#print(players)
def RotatePoint(x, y, angle):
    angle = math.radians(angle)
    x -= screenSize[0]/2
    y -= screenSize[1]/2
    nx = (x*math.cos(angle))-(y*math.sin(angle))
    ny = (x*math.sin(angle))+(y*math.cos(angle))
    nx += screenSize[0]/2
    ny += screenSize[1]/2
    return nx,ny
def NextTurn(numPlayers):
    global a
    global turn
    a += 1
    turn += 1
    if turn > numPlayers:
        turn = 1
frame = 0
offset = 0,0
cardWidth = screenSize[0]/20 if screenSize[0] < 750 else screenSize[0]/25
cardHeight = int((cardWidth/2.5))*3.5
buttonSize = cardWidth*1.5
pos = utils.Coordinate((screenSize[0]/2)+cardWidth, (screenSize[1]/2)-(cardHeight/2))
cardBackFull = pygame.image.load('cardBack.png').convert_alpha()
cardBack = pygame.transform.scale(cardBackFull.subsurface(cardBackFull.get_bounding_rect()), (cardWidth, cardHeight))
cardFrontFull = pygame.image.load('cardFront.png').convert_alpha()
cardFront = utils.ReplaceColor(pygame.transform.scale(cardFrontFull.subsurface(cardFrontFull.get_bounding_rect()), (cardWidth, cardHeight)),utils.Hex('990030'), utils.gray)
coloredCards = {}
for i in range(len(colors)):
    coloredCards[str(colors[i])] = utils.ReplaceColor(cardFront, utils.Hex('ffffff'), colors[i])
#print(coloredCards)
while menu:
    screenSize = screen.get_size()
    pygame.draw.rect(screen, menuBackgroundColor, ((0, 0), screenSize), width=0)
    optionNum, numPlayers, cooldown = utils.Arrows('Number of Players', [2,3,4,5,6,7,8,15], utils.white, optionNum, screen, (20, 350), cooldown)
    optionNum2, numCardsPerPerson, cooldown2 = utils.Arrows('Num Cards per Person', [1,2,3,4,5,6,7,8,9], utils.white, optionNum2, screen, (20, 400), cooldown2)
    optionNum3, numCardsToWin, cooldown3 = utils.Arrows('Num Cards to Win', [i for i in range(5,20)], utils.white, optionNum3, screen, (20, 450), cooldown3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_RETURN:
                menu = False
    pygame.display.update()
    clock.tick(60)
for playera in range(numPlayers):
    players[playera] = [[[deck[i*(numPlayers)+playera][0], 1] for i in range(numCardsPerPerson)]]
    players[playera].append(0)
stealFrom = [pygame.Rect(0,0,0,0) for i in range(numPlayers)]
while True:
    screenSize = screen.get_size()
    Font = pygame.font.Font(None, int(screenSize[1]/20))
    smallFont = pygame.font.Font(None, int(screenSize[1]/27))
    mousePos = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePos, (1, 1))
    pygame.draw.rect(screen, backgroundColor, ((0, 0), screenSize), width=0)
    random.seed(seed)
    b = random.randint(-3,-1)
    screen.blit(utils.ReplaceColor(utils.ReplaceColor(utils.ReplaceColor(utils.ReplaceColor(cardBack, utils.Hex('ffffff'), deck[a][b+1]), utils.Hex('464646'), deck[a][b+2]), utils.Hex('b4b4b4'), deck[a][b+3]),utils.Hex('990030'), utils.gray), ((screenSize[0]/2)-(cardWidth/2)-borderSize, (screenSize[1]/2)-(cardHeight/2)-borderSize, cardWidth+(borderSize*2), cardHeight+(borderSize*2)))
    i = 0
    bank = pygame.Rect((screenSize[0]/2)-2-buttonSize, (screenSize[1]/2)+buttonSize, buttonSize, buttonSize)
    steal = pygame.Rect((screenSize[0]/2)+3, (screenSize[1]/2)+buttonSize, buttonSize-.5, buttonSize)
    pygame.draw.rect(screen, utils.lightGray if pygame.Rect.colliderect(mouseRect, bank) else utils.gray, bank)
    pygame.draw.rect(screen, utils.lightGray if mouseRect.colliderect(steal) else utils.gray, steal)
    text = smallFont.render('Bank', True, utils.white)
    screen.blit(text, (bank.centerx-text.get_width()/2, bank.centery-(text.get_height()/2)+1))
    text = smallFont.render('Steal', True, utils.white)
    screen.blit(text, (steal.centerx-text.get_width()/2, steal.centery-(text.get_height()/2)+1))
    if flipCardBank:
        screen.blit(coloredCards[str(deck[a][0])], pos)
        #print(frame-flipTime)
        if frame - flipTimeBank >= showCardTime:
            #print(RotatePoint(screenSize[0]/2, (screenSize[1]/2)-(cardHeight*1.5), 360/numPlayers*(-turn-1)))
            pointToGo = RotatePoint(screenSize[0]/2, (screenSize[1])-(cardHeight*1.5), 360/numPlayers*(turn-1))
            #print(pointToGo)
            #print(360/numPlayers*(-turn-1))
            pos = utils.lerp2d((((screenSize[0]/2)+cardWidth), ((screenSize[1]/2)-(cardHeight/2))), (pointToGo[0], pointToGo[1]), (frame-flipTimeBank-showCardTime)/25)
            #offset = -cardWidth*1.5, screenSize[1]/2-cardHeight*1.5
            #print(offset)
        if (frame-flipTimeBank-showCardTime)/25 >= 1:
            #print(deck[a], deck[a][0])
            #print(players[turn-1])
            if [deck[a][0], 1] in players[turn-1][0]:
                players[turn-1][0].append([deck[a][0], 1])
                temp = copy.deepcopy(players[turn-1][0])
                for variable in temp:
                    if variable == [deck[a][0], 1]:
                        players[turn-1][-1] += 1
                        players[turn-1][0].remove(variable)
            else:
                players[turn-1][0].append([deck[a][0], 1])
            flipCardBank = False
            #print(players[turn-1])
            NextTurn(numPlayers)
            pos = utils.Coordinate(((screenSize[0]/2)+cardWidth), ((screenSize[1]/2)-(cardHeight/2)))
    if flipCardSteal:
        pygame.draw.rect(screen, utils.white, (pos.x-borderSize, pos.y-borderSize, cardWidth+borderSize*2, cardHeight+borderSize*2), width=0)
        pygame.draw.rect(screen, deck[a][0], (pos.x, pos.y, cardWidth, cardHeight))
        if frame - flipTimeSteal >= showCardTime:    
            pointToGo = RotatePoint(screenSize[0]/2, (screenSize[1])-(cardHeight*1.5), 360/numPlayers*(playerNumSteal-1))
            pos = utils.lerp2d((((screenSize[0]/2)+cardWidth), ((screenSize[1]/2)-(cardHeight/2))), (pointToGo[0], pointToGo[1]), (frame-flipTimeSteal-showCardTime)/25)
        if (frame-flipTimeSteal-showCardTime)/25 >= 1:
            numCards = 0
            #print(players[playerNumSteal-1])
            for variable in players[playerNumSteal-1][0]:
                if variable ==  [deck[a][0], 1]:
                    numCards +=1
            #print(numCards)
            if [deck[a][0], 1] in players[playerNumSteal-1][0]:
                players[playerNumSteal-1][0].append([deck[a][0], 1])
                for x in range(numCards+1):
                    players[turn-1][0].append([deck[a][0], 1])
                    players[playerNumSteal-1][0].remove([deck[a][0], 1])
            else:
                players[playerNumSteal-1][0].append([deck[a][0], 1])
            flipCardSteal = False
            NextTurn(numPlayers)
            pos = utils.Coordinate(((screenSize[0]/2)+cardWidth), ((screenSize[1]/2)-(cardHeight/2)))
    for player in players.items():
        player = copy.deepcopy(player)
        player = player[1:]
        #print(player)
        angle = (360/numPlayers)*i*-1
        cards = pygame.Surface(screenSize, pygame.SRCALPHA)
        j = 0
        playerCards = copy.deepcopy(player[0][0])
        newlist = [] 
        duplist = []
        for cardy in playerCards:
            append = True
            if len(newlist) > 0:
                for newCard in newlist:
                    if cardy[0] != newCard[0]:
                        pass
                    else:
                        duplist.append(cardy)
                        append = False
                        break
            if append == True:
                newlist.append(cardy)
        #print(newlist)
        alist = []
        for x in newlist:
            alist.append(x[0])
        for x in duplist:
            #print(newlist[newlist.index(x)])
            newlist[alist.index(x[0])][1] += 1
        #print(newlist)
        newlist = sorted(newlist, key=lambda car: car[1], reverse=True)
        if turn == i+1:
            pygame.draw.rect(cards, utils.darkGray, (screenSize[0]/2-10, screenSize[1]-cardHeight*2-cardSpacing-20, 20, 20), width=0)
        for card in newlist:
            cards.blit(coloredCards[str(card[0])], ((screenSize[0]/2)-(cardWidth/2)+((j-((len(newlist)-1)/2))*(cardSpacing+cardWidth)), screenSize[1]-(cardHeight*2)))
            #print(str(card[1]), frame,j)
            text = Font.render(str(card[1]), True, utils.black)
            cards.blit(text, ((screenSize[0]/2)-(cardWidth/2)+((j-((len(newlist)-1)/2))*(cardSpacing+cardWidth))-text.get_width()/2+cardWidth/2, screenSize[1]-(cardHeight*1.5)-(text.get_height()/2)))
            j += 1
        if chooseSteal and turn != i+1:
            point = (screenSize[0]/2-buttonSize/2, screenSize[1]-(cardHeight*2)-borderSize-cardSpacing-buttonSize)
            stealFrom[i] = pygame.draw.polygon(cards, (0,0,0,0), [RotatePoint(point[0], point[1], -angle), RotatePoint(point[0], point[1]+buttonSize, -angle), RotatePoint(point[0]+buttonSize, point[1]+buttonSize, -angle), RotatePoint(point[0]+buttonSize, point[1], -angle)])
            pygame.draw.polygon(cards, utils.lightGray if mouseRect.colliderect(stealFrom[i]) else utils.gray, [(point[0], point[1]), (point[0], point[1]+buttonSize), (point[0]+buttonSize, point[1]+buttonSize), (point[0]+buttonSize, point[1])])
        text = Font.render(f'Player {i+1}', True, utils.lightGray)
        cards.blit(text, ((screenSize[0]/2)-(text.get_width()/2), screenSize[1]-text.get_height()-((cardHeight-text.get_height())/2)))
        text = Font.render(f'{player[0][-1]}', True, utils.white)
        cards.blit(text, (screenSize[0]/2+20, screenSize[1]-text.get_height()-cardHeight*2-cardSpacing))
        if player[0][-1] >= numCardsToWin:
            text = Font.render(f'Player {i+1} Wins!!', True, utils.white)
            screen.blit(text, ((screenSize[0]/2)-(text.get_width()/2), screenSize[1]/2-text.get_height()/2))
        cards = pygame.transform.rotate(cards, angle)
        i += 1
        screen.blit(cards, ((screenSize[0]-cards.get_width())/2, (screenSize[1]-cards.get_height())/2))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            pos = utils.Coordinate(((screenSize[0]/2)+cardWidth), ((screenSize[1]/2)-(cardHeight/2)))
            cardWidth = screenSize[0]/20 if screenSize[0] < 750 else screenSize[0]/25
            cardHeight = int((cardWidth/2.5))*3.5
            buttonSize = cardWidth*1.5
            cardFrontRect = cardFrontFull.get_bounding_rect()
            cardFront = utils.ReplaceColor(pygame.transform.scale(cardFrontFull.subsurface((cardFrontRect.left, cardFrontRect.top, cardFrontRect.width+1, cardFrontRect.height+1)), (cardWidth, cardHeight)),utils.Hex('990030'), utils.gray)
            cardBackRect = cardBackFull.get_bounding_rect()
            cardBack = utils.ReplaceColor(pygame.transform.scale(cardBackFull.subsurface((cardBackRect.left, cardBackRect.top, cardBackRect.width+1, cardBackRect.height+1)), (cardWidth, cardHeight)),utils.Hex('990030'), utils.gray)
            for i in range(len(colors)):
                coloredCards[str(colors[i])] = utils.ReplaceColor(cardFront, utils.Hex('ffffff'), colors[i])
        if event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_F2:
                utils.TakeScreenshot(screen)
                text = Font.render(f'Screenshot Saved', True, utils.lightGray)
                screen.blit(text, (10,10))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.__dict__['button'] == 1:
                if mouseRect.colliderect(bank):
                    #print(turn)
                    flipCardBank = True
                    flipTimeBank = frame
                    #NextTurn(numPlayers)
                if mouseRect.colliderect(steal):
                    chooseSteal = True
                playerNumSteal = 1
                for button in stealFrom:
                    if mouseRect.colliderect(button):
                        #print(playerNumSteal)
                        #NextTurn(numPlayers)
                        chooseSteal = False
                        flipCardSteal = True
                        flipTimeSteal = frame
                        break
                    playerNumSteal += 1
    pygame.display.update()
    pygame.display.set_caption(f'FPS:{clock.get_fps()}')
    frame += 1
    clock.tick(60)