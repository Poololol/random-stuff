import pygame
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
stair = pygame.image.load('stair.png').convert_alpha()
slab = pygame.image.load('slab.png').convert_alpha()
tops = []
bottoms = []
class Thing():
    def __init__(self) -> None:
        pass
    def Make(self, image, index):
        self.image = image
        self.index = index
        return self
for x in range(6):
    if x < 4:
        image = pygame.transform.rotate(stair, 90*x)
    else:
        image = pygame.transform.rotate(slab, 180*(x-4))
    tops.append(Thing.Make(Thing(), image, x))
for x in range(6):
    if x < 4:
        image = pygame.transform.rotate(stair, 90*x)
    else:
        image = pygame.transform.rotate(slab, 180*(x-4))
    bottoms.append(Thing.Make(Thing(), image, x))
while True:
    screenSize = screen.get_size()
    width = min(screenSize)/15
    height = width
    pygame.draw.rect(screen, (62, 93, 91), ((0,0),screenSize), width=0)
    for top in tops:
        for bottom in bottoms:
            screen.blit(pygame.transform.scale(top.image, (width, width)), ((top.index+1)*(width*2), (bottom.index+.2)*(width*2.5)))
            screen.blit(pygame.transform.scale(bottom.image, (width, width)), ((top.index+1)*(width*2), (bottom.index+.2)*(width*2.5)+height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(60)
