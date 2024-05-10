import pygame
import pyautogui
pygame.display.init()
clock = pygame.time.Clock()
#screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
while True:
    #print(pygame.mouse.get_pos())
    print(pyautogui.position())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(1)