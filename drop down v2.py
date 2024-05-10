import pygame
import utils
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
screenSize = screen.get_size()
clock = pygame.time.Clock()
pygame.font.init()
myFont = pygame.font.SysFont('arialbold', int(screenSize[0]/11))
options = [1,'Test',3]
selected = 1
opened = False
while True:
    pygame.draw.rect(screen, utils.black, ((0,0), screenSize), width=0)
    mousePos = pygame.mouse.get_pos()
    dropdown = pygame.Rect((100,100,100,30))
    if utils.Mouseover(mousePos, dropdown):
        pygame.draw.rect(screen, utils.lightGray, dropdown, width=0)
    else:
        pygame.draw.rect(screen, utils.gray, dropdown, width=0)
    text = myFont.render(str(options[selected]), True, utils.white)
    screen.blit(text, (dropdown.left+2, dropdown.top+2))
    dropdownOptions = []
    if opened:
        pygame.draw.line(screen, utils.white, (dropdown.right-5, dropdown.bottom-5), (dropdown.right-(dropdown.height/2), dropdown.top+5), width=2)
        pygame.draw.line(screen, utils.white, (dropdown.right-(dropdown.height/2), dropdown.top+5), (dropdown.right-dropdown.height+5, dropdown.bottom-5), width=2)
        for i, option in enumerate(options):
            text = myFont.render(str(option), True, utils.white)
            dropdownOption = pygame.Rect(dropdown.left, dropdown.bottom+dropdown.height*i, dropdown.width, dropdown.height)
            dropdownOptions.append(pygame.draw.rect(screen, utils.gray, dropdownOption, width=0))
            screen.blit(text, (dropdownOption.left+2, dropdownOption.top+2))
            pygame.draw.rect(screen, utils.darkGray, dropdownOption, width=1)
    else:
        pygame.draw.line(screen, utils.white, (dropdown.right-5, dropdown.top+5), (dropdown.right-(dropdown.height/2), dropdown.bottom-5), width=2)
        pygame.draw.line(screen, utils.white, (dropdown.right-(dropdown.height/2), dropdown.bottom-5), (dropdown.right-dropdown.height+5, dropdown.top+5), width=2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if utils.Mouseover(event.__dict__['pos'], dropdown):
                opened = not opened
            if opened:
                for i, option in enumerate(dropdownOptions):
                    if utils.Mouseover(event.__dict__['pos'], option):
                        selected = i
                        opened = False
    mouseDown = pygame.mouse.get_pressed()[0]
    pygame.display.update()
    clock.tick(60)