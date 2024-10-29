import pygame
import scipy.interpolate
import numpy
screen = pygame.display.set_mode((500,500))
screenSize = screen.get_size()
clock = pygame.time.Clock()
time = 0
length = 200
frames = 50
x = numpy.linspace(0, frames, frames)
y = numpy.ones(frames)
for frame in range(int(frames/2)):
    y[frame] = frame
for frame in range(int((frames+1)/2)):
    y[frames-1-frame] = frame
xVals = numpy.linspace(0, frames, length)
yNew = numpy.interp(xVals, x, y)
print(y)
while True:
    yVal = (yNew[time]+1)*16
    print(yVal)
    pygame.draw.rect(screen, (0,0,0), ((0,0),screenSize), width=0)
    pygame.draw.circle(screen, (255,255,255), (250, yVal), 5, width=0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    time += 1
    if time >= length:
        time = 0
    clock.tick(60)
