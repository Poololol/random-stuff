import pygame
import utils
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
check1 = utils.Setting.Checkbox((100,100), 10, 'Test 1')
check2 = utils.Setting.Checkbox((100,200), 20, 'Test 2')
check3 = utils.Setting.Checkbox((100,300), 30, 'Test 3')
check4 = utils.Setting.Checkbox((100,400), 40, 'Test 4')
button = utils.Setting.Button(utils.gray, utils.lightGray, utils.lightBlueishGray, utils.white, 'Button')
drop = utils.Setting.Dropdown([1,2,3,'test'], utils.darkGray, utils.lightGray, utils.blue)
while True:
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, utils.black, (0,0,500,500), width=0)
    check1.Render(screen, utils.white)
    check2.Render(screen, utils.white)
    check3.Render(screen, utils.white)
    check4.Render(screen, utils.white)
    button.Render(screen, (250, 100), 17, mousePos)
    drop.Render(screen, (250, 200), mousePos, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check1.Event(event)
            check2.Event(event)
            check3.Event(event)
            check4.Event(event)
            drop.Event(event)
            button.Clicked(event)
    clock.tick(60)
    pygame.display.update()
