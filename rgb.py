import pygame
import utils
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.

    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)

    """
    return (1 - t) * a + t * b


def inv_lerp(a: float, b: float, v: float) -> float:
    """Inverse Linar Interpolation, get the fraction between a and b on which v resides.

    Examples
    --------
        0.5 == inv_lerp(0, 100, 50)
        0.8 == inv_lerp(1, 5, 4.2)

    """
    return (v - a) / (b - a)


def remap(i_min: float, i_max: float, o_min: float, o_max: float, v: float) -> float:
    """Remap values from one linear scale to another, a combination of lerp and inv_lerp.

    i_min and i_max are the scale on which the original value resides,
    o_min and o_max are the scale to which it should be mapped.

    Examples
    --------
        45 == remap(0, 100, 40, 50, 50)
        6.2 == remap(1, 5, 3, 7, 4.2)

    """
    return lerp(o_min, o_max, inv_lerp(i_min, i_max, v))
def Draw(color1, color2, scale):
    screenSize = screen.get_size()
    xMulti = screenSize[0]/255
    yMulti = screenSize[1]/255
    image = pygame.Surface(screenSize, pygame.SRCALPHA)
    
    for x in range(int(screenSize[0]*-.5), int(screenSize[0]*.5)):
        for y in range(int(screenSize[1]*-.5), int(screenSize[1]*.5)):
            xc = remap(0, (screenSize[0]/2)**2, 0, 255, (x**2))
            yc = remap(0, (screenSize[1]/2)**2, 0, 255, (y**2))
            axyc = (xc+yc)/2
            r = remap(0,255, color1[0], color2[0], axyc*(1-scale))
            g = remap(0,255, color1[1], color2[1], axyc*(1-scale))
            b = remap(0,255, color1[2], color2[2], axyc*(1-scale))
            a = remap(0,255, color1[3], color2[3], axyc*(1-scale))
            image.set_at((int(x+(screenSize[0]/2)), int(y+screenSize[1]/2)), (r,g,b, a))
    screen.blit(image, (0,0))
x=55
value=.5
prev=.1
Draw((0,0,0,0),(255,255,255,255), 0)
while True:
    screenSize = screen.get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.WINDOWRESIZED:
            Draw((0,0,0,0),(255,255,255,255), value)
    if value != prev:
        pygame.draw.rect(screen, (255,2,2), ((0,0),screenSize), width=0)
        Draw((0,0,0,64),(0,0,0,200), value)
    prev = value
    value, x = utils.Slider(30, 80, x, 40, screen)
    #va = value/50
    pygame.display.update()
    clock.tick(60)