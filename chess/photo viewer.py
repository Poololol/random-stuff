import pygame
from tkinter import filedialog
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
file = filedialog.askopenfilename()
image = pygame.image.load(file).convert_alpha()
while True:
    screenSize = screen.get_size()
    pygame.draw.rect(screen, (0,0,0),  ((0,0), screenSize))
    imageSize = image.get_size()
    scalar = min(screenSize)/min(imageSize)
    image = pygame.transform.scale_by(image, scalar)
    screen.blit(image, ((screenSize[0]/2)-(imageSize[0]/2), (screenSize[1]/2)-(imageSize[1]/2)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_CTRL and event.dict['key'] == pygame.K_o:
                file = filedialog.askopenfilename()
                image = pygame.image.load(file).convert_alpha()
    pygame.display.update()
    clock.tick(60)