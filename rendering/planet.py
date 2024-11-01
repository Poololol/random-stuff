import pygame
import utils
import copy
import math
import numpy as np
import opensimplex
from numba import njit, jit
import pygame_gui
import pygame_gui.elements as gui
import time
import timeit

screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font(None, 20)
screenSize = screen.get_size()
debug = False
screenshotKey = pygame.K_F2
debugKey = pygame.K_F3

def draw_text(text:str, surface: pygame.Surface = screen):
    text = font.render(text, True, utils.white)
    surface.blit(text, (0,0))
def XRot(angle):
    return np.array([[1,0,0], [0,math.cos(angle),-math.sin(angle)], [0,math.sin(angle), math.cos(angle)]])
def YRot(angle):
    return np.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
def DrawCircle(radius, noise):
    for x in range(-radius,radius):
        for y in range(-radius,radius):
                if x*x+y*y<=radius**2:
                    normal = utils.Coordinate(-(radius-x)/radius+1, (radius-y)/radius-1)
                    normal.z = math.sqrt(1-normal.x**2+normal.y**2)
                    normal = normal.Normalize()
                    lightPower = normal.dot(-lightDirection.Normalize() * lightIntensity)
                    n = noise[0][x+radius][y+radius]
                    if n<-.2:
                        color = utils.Coordinate(0,0,1)
                    elif n<0:
                        color = utils.Coordinate(.2,.2,1)
                    elif n<.2:
                        color = utils.Coordinate(196, 180, 74)/255
                    elif n<.75:
                        color = utils.Coordinate(0,1,0)
                    else:
                        color = utils.Coordinate(.25,.25,.25)
                    color *= lightPower
                    screen.set_at((x+250,y+250), color.Color())
def DrawCircleNumpy(radius: float, noise:np.ndarray, lightDirection: utils.Coordinate, lightIntensity: float, screenSize):
    '''Code mostly generated by ChatGPT from other function'''
    t1 = time.time()
    # Precompute grid of x, y coordinates
    x = np.arange(-radius, radius)
    y = np.arange(-radius, radius)
    xGrid, yGrid = np.meshgrid(x, y)
    # Condition for circle
    insideCircle = xGrid**2 + yGrid**2 <= radius**2
    t4 = time.time()
    print(f'1 Took: {t4-t1} seconds')
    # Flatten inside_circle indices for selected points
    xCircle = xGrid[insideCircle]
    yCircle = yGrid[insideCircle]
    # Precompute normal vectors for points inside the circle
    normalX = (-(radius - xCircle) / radius + 1)
    normalY = ((radius - yCircle) / radius - 1)
    normalZ = np.sqrt(1 - normalX**2 + normalY**2)
    t5 = time.time()
    print(f'2 Took: {t5-t4} seconds')
    # Normalize normal vectors
    normalMagnitude = np.sqrt(normalX**2 + normalY**2 + normalZ**2)
    normalX /= normalMagnitude
    normalY /= normalMagnitude
    normalZ /= normalMagnitude
    t6 = time.time()
    print(f'3 Took: {t6-t5} seconds')
    # Compute dot product with light direction for points inside circle
    lightPower = (normalX * -lightDirection.x +
                normalY * -lightDirection.y +
                normalZ * -lightDirection.z) * lightIntensity
    print(lightPower[30000])
    t7 = time.time()
    print(f'4 Took: {t7-t6} seconds')
    # Access noise and reshape it for the inside circle
    n = np.zeros(xCircle.shape)
    for i in range(numOctives):
        n += noise[i][0][xCircle + radius, yCircle + radius] # Assuming noise is a 2D array
    '''x_idx = xCircle + radius
    y_idx = yCircle + radius
    n = np.sum([noise[i][0][x_idx, y_idx] for i in range(numOctives)], axis=0)'''
    #n = np.sum(noise[:, 0, xCircle + radius, yCircle + radius], axis=0)
    t82 = time.time()
    print(f'4.5 Took: {t82-t7} seconds')
    # Compute color for each point inside the circle
    colors = np.zeros((len(xCircle), 3))  # Preallocate color array for insideCircle points
    n = np.where(n > 1, 1, n) # Correct for slight errors that result in values greater than 1
    t8 = time.time()
    print(f'5 Took: {t8-t82} seconds')
    for layer in colorLayers:
        colors[:, 0] = np.where(n <= layer[0], layer[1][0], colors[:, 0])
        colors[:, 1] = np.where(n <= layer[0], layer[1][1], colors[:, 1])
        colors[:, 2] = np.where(n <= layer[0], layer[1][2], colors[:, 2])
    # Apply lighting to colors for points inside the circle
    colors *= lightPower[:, np.newaxis]
    t9 = time.time()
    print(f'6 Took: {t9-t8} seconds')
    # Now draw the points inside the circle on the screen
    array = pygame.surfarray.pixels3d(screen)
    t2 = time.time()
    print(f'Pre-rendering Took: {t2-t1} seconds')
    DrawPoints(xCircle, yCircle, colors, noise, radius, array, screenSize, day, n, lightPower)
    t3 = time.time()
    print(f'Rendering Took: {t3-t2} seconds')
    print(f'Total Rendering Time: {t3-t1} seconds\n')
@njit
def DrawPoints(xCircle, yCircle, colors, noise, radius, array, screenSize: tuple[int, int], day, no=0, light=0):
    xOff = int(screenSize[0]/2)
    yOff = int(screenSize[1]/2)
    for i, (xi, yi) in enumerate(zip(xCircle, yCircle)):
        color = (colors[i][0] * 255, colors[i][1] * 255, colors[i][2] * 255)  # Convert color to integer tuple (RGB)
        # Set the pixel on the screen
        n=0
        for o in range(numOctives):
            n += noise[o][0][xi +radius][yi +radius]
        n2 = noise2[0][xi + radius][yi + radius]>.250 and noise3[xi + radius][yi + radius]>.50
        if day:
            if sum(color) >= 10: #should probably change this so can have dark terrain
                    array[xi + xOff][yi + yOff] = color
            else:
                if n >= .1:
                    array[xi + xOff][yi + yOff] = (lightsColor[0] if n2 else abs(color[0]/15), lightsColor[1] if n2 else abs(color[1]/15), lightsColor[2] if n2 else abs(color[2]/15))
                else:
                    array[xi + xOff][yi + yOff] = (abs(color[0]/15), abs(color[1]/15), abs(color[2]/15))
        else:
            if sum(color) >= 10: #this too
                array[xi + xOff][yi + yOff] = color
                if  n >= .1 and n <= .7 and n2:
                    array[xi + xOff][yi + yOff] = lightsColor
            else:
                if n >= .1:
                    array[xi + xOff][yi + yOff] = (lightsColor[0] if n2 else abs(color[0]/15), lightsColor[1] if n2 else abs(color[1]/15), lightsColor[2] if n2 else abs(color[2]/15))
                else:
                    array[xi + xOff][yi + yOff] = (abs(color[0]/15), abs(color[1]/15), abs(color[2]/15))

def DrawPointsNumpy(xCircle:np.ndarray, yCircle:np.ndarray, colors:np.ndarray, noise, radius:float, array:np.ndarray, screenSize: tuple[int, int], day:bool, n:np.ndarray, light:np.ndarray):
    xOff = int(screenSize[0]/2)
    yOff = int(screenSize[1]/2)
    color = (colors[:, 0] * 255, colors[:, 1] * 255, colors[:, 2] * 255)  # Convert color to integer tuple (RGB)
    # Set the pixel on the screen
    xi = xCircle
    yi = yCircle
    n2 = np.where((noise2[0]>.250), np.where(noise3>.5, True, False), False)
    #n2 = noise2[0][xi + radius][yi + radius]>.250 and noise3[xi + radius][yi + radius]>.50
    if day:
        np.where(light>=10)
        return
        if light >= 10: #should probably change this so can have dark terrain
                array[xi + xOff][yi + yOff] = color
        else:
            if n >= .1:
                array[xi + xOff][yi + yOff] = (lightsColor[0] if n2 else abs(color[0]/15), lightsColor[1] if n2 else abs(color[1]/15), lightsColor[2] if n2 else abs(color[2]/15))
            else:
                array[xi + xOff][yi + yOff] = (abs(color[0]/15), abs(color[1]/15), abs(color[2]/15))
    else:
        if sum(color) >= 10: #this too
            array[xi + xOff][yi + yOff] = color
            if  n >= .1 and n <= .7 and n2:
                array[xi + xOff][yi + yOff] = lightsColor
        else:
            if n >= .1:
                array[xi + xOff][yi + yOff] = (lightsColor[0] if n2 else abs(color[0]/15), lightsColor[1] if n2 else abs(color[1]/15), lightsColor[2] if n2 else abs(color[2]/15))
            else:
                array[xi + xOff][yi + yOff] = (abs(color[0]/15), abs(color[1]/15), abs(color[2]/15))
def HorizontalGradient(rect: pygame.Rect, topcolor, bottomcolor):
    "Code Taken from vgrade example"
    surf = pygame.Surface(rect.size)
    topcolor = np.array(topcolor, copy=False)*255
    bottomcolor = np.array(bottomcolor, copy=False)*255
    diff = bottomcolor - topcolor
    width = surf.get_size()[0]
    # create array from 0.0 to 1.0 triplets
    column = np.arange(width, dtype="float") / width
    column = np.repeat(column[:, np.newaxis], [3], 1)
    # create a single column of gradient
    column = topcolor + (diff * column).astype("int")
    # make the column a 3d image column by adding X
    column = column.astype("uint8")[np.newaxis, :, :]
    column = column.reshape((width,1,3))
    # 3d array into 2d array
    grad =  pygame.surfarray.map_array(surf, column)
    pygame.surfarray.blit_array(surf, grad)
    screen.blit(surf, rect.topleft)
def ColorPicker(mousePos, picking = False) -> pygame.Color:
    # do i need this?
    global colorPickerRect
    if picking:
        pass
    else:
        colorPickerRect = pygame.Rect(mousePos, (50,50))
def sorter(item):
    return item[0]
def ConvertColor(color: tuple[float, float, float] |  pygame.Color, type: str = 'rgb') -> pygame.Color | tuple[float, float, float]:
    '''
    type is either 'rgb' or '01' \n
    Converts to type from the other
    '''
    if type == 'rgb':
        color2 = pygame.Color(int(color[0]*255), int(color[1]*255), int(color[2]*255))
        return color2
    else:
        return (color[0]/255, color[1]/255, color[2]/255)
def AlignContainer(container:gui.UIAutoResizingContainer, pos: tuple[int, int], align: str = 'TL') -> None:
    '''align = ['TL', 'TR']'''
    offset = 0
    for i, element in enumerate(container.elements):
        if element.get_element_ids()[1] == 'container':
            offset += 1
        else:
            i -= offset
            element.set_dimensions((int(150*screenSize[0]/500), 20))
            element.set_relative_position((10, 10+30*i))
        element.rebuild()
    minHeight = container.bottom_element.rect.bottom-container.top_element.rect.top + 20
    minWidth = container.right_element.rect.right-container.left_element.rect.left + 20
    if align == 'TR':
        container.set_position((screenSize[0]-(minWidth+pos[0]), pos[1]))
        print(f'Old Min Rect = {container.min_edges_rect}')
        container.min_edges_rect = pygame.Rect(screenSize[0]-(minWidth+pos[0]), pos[1], minWidth, minHeight)
        print(f'New Min Rect = {container.min_edges_rect}')
    elif align == 'TL':
        container.set_position((pos[0], pos[1]))
        print(f'Old Min Rect = {container.min_edges_rect}')
        container.min_edges_rect = pygame.Rect(pos[0], pos[1], minWidth, minHeight)
        print(f'New Min Rect = {container.min_edges_rect}')
    else:
        raise FutureWarning('Other alignments not implemented')
    container.set_dimensions((1,1)) # Force the container to resize
colorPickerRect = pygame.Rect(1,1,1,1)
radius = 150
lightDirection = utils.Coordinate(x=0, y=0, z=-1).Normalize()
print(lightDirection)
lightIntensity = 1
numOctives = 10
octives = []
freq = 100
amp = 1
scale = 50
day = True
colorLayers = [[1, (1, 1, 1)], [0.1, (0.5, 0, 0.5)], [0, (0.2, 0.2, 1)], [-0.2, (0, 0, 1)]]
colorPicking = False
colorMoving = False
colorChanging = False
gradient = False
lightsColor = (255,255,255)
mousePos = (0,0)
mouseRect = pygame.Rect(mousePos, (1,1))
print(f'Calculating Noise...')
t1 = time.time()
opensimplex.seed(123)
for i in range(numOctives):
    noise = opensimplex.noise3array(np.arange(-750/freq, 750/freq, 1/freq), np.arange(-750/freq, 750/freq, 1/freq), np.array([1]))/amp
    octives.append(noise)
    freq/=2
    amp/=.5
octives = np.array(octives)
opensimplex.seed(1234)
noise2 = opensimplex.noise3array(np.arange(-750/scale, 750/scale, 1/scale), np.arange(-750/scale, 750/scale, 1/scale), np.array([1]))
noise3 = opensimplex.noise2array(np.arange(-750, 750, 1), np.arange(-750, 750, 1))
print(f'Noise Calculated in {time.time()-t1} seconds\n')

uiMan=pygame_gui.UIManager(screenSize, 'theme.json')

autoSettings = gui.UIAutoResizingContainer([5, 5, 170, 70], manager=uiMan, visible=1)
lightRotationY = gui.UIHorizontalSlider([10, 10, 150, 20], 0, (0, 2*math.pi), manager=uiMan, click_increment=.01, container=autoSettings)
lightsButton = gui.UIButton(pygame.Rect([10,40,150,20]), "Toggle Day Lights", manager=uiMan, container=autoSettings)


planetSettings = gui.UIAutoResizingContainer([screenSize[0]-175, 5, 170, 100], manager=uiMan, visible=1)
radiusSlider = gui.UIHorizontalSlider([10, 10, 150, 20], 150, (100, 250), manager=uiMan, click_increment=10, container=planetSettings)
gradientThing = gui.UIButton(pygame.Rect([10, 40, 150, 20]), '', manager=uiMan, container=planetSettings, visible=1)
gradientThing.hide()
gradientThing.border_width = 2
gradientRect = pygame.Rect(gradientThing.rect.left+gradientThing.border_width, gradientThing.rect.top+gradientThing.border_width, gradientThing.rect.width-2*gradientThing.border_width, gradientThing.rect.height-2*gradientThing.border_width)
Rvalue, Rx = utils.Slider(colorPickerRect.left+5, colorPickerRect.width-10, colorPickerRect.centerx, colorPickerRect.top+5, screen, utils.darkGray, utils.lightGray, False, True)
Gvalue, Gx = utils.Slider(colorPickerRect.left+5, colorPickerRect.width-10, colorPickerRect.centerx, colorPickerRect.top+5+(colorPickerRect.height/3), screen, utils.darkGray, utils.lightGray, False, True)
Bvalue, Bx = utils.Slider(colorPickerRect.left+5, colorPickerRect.width-10, colorPickerRect.centerx, colorPickerRect.top+5+2*(colorPickerRect.height/3), screen, utils.darkGray, utils.lightGray, False, True)
generatePlanetButton = gui.UIButton(pygame.Rect(10, 70, 150, 20), "Generate Planet", manager=uiMan, container=planetSettings)
while True:
    dt = clock.get_time()
    screenSize = screen.get_size()
    pygame.draw.rect(screen, utils.black, ((0,0),screenSize), width=0)
    #lightDirection = utils.Coordinate(lightDirection.array@YRot(.01)).Normalize()
    lightDirectionRotated = utils.Coordinate(xyz=lightDirection.array@YRot(lightRotationY.current_value))
    mousePos = pygame.mouse.get_pos()
    if lightsButton.pressed:
        day = not day
        print(f'Lights always on = { not day}')
    if generatePlanetButton.pressed:
        radius = int(radiusSlider.current_value)
    DrawCircleNumpy(radius, octives, lightDirectionRotated, lightIntensity, screenSize)
    s = pygame.Surface(screenSize, pygame.SRCALPHA)
    pygame.draw.rect(s, utils.darkGray + [200], autoSettings.rect, width=0)
    pygame.draw.rect(s, utils.darkGray + [200], planetSettings.rect, width=0)
    if debug:
        draw_text(str(round(clock.get_fps(), 5)))
        pygame.draw.rect(s, utils.blue + [100], planetSettings.min_edges_rect, width=0)
        pygame.draw.rect(screen, utils.yellow, gradientThing.rect, width=0)
        pygame.draw.rect(screen, utils.green, gradientRect, width=0)
        pygame.draw.rect(screen, utils.green, generatePlanetButton.rect, width=0)
    screen.blit(s, (0,0))
    if gradient:
        offset = 0
        for i in range(len(colorLayers)):
            if i != len(colorLayers)-1:
                segWidth = abs(colorLayers[i][0]-colorLayers[i+1][0])/2*gradientRect.width
                segWidth += .5
                HorizontalGradient(pygame.Rect(gradientRect.left+offset, gradientRect.top, segWidth, gradientRect.height), colorLayers[i][1], colorLayers[i+1][1])
                offset += (segWidth - .5)
            else:
                segWidth = abs(1+colorLayers[i][0])/2*gradientRect.width
                pygame.draw.rect(screen, ConvertColor(colorLayers[i][1], 'rgb'), pygame.Rect(gradientRect.left+offset, gradientRect.top, segWidth, gradientRect.height), width=0)
    else:
        offset = 0
        for i in range(len(colorLayers)):
            try:
                segWidth = abs(colorLayers[i][0]-colorLayers[i+1][0])/2*gradientRect.width
            except IndexError:
                segWidth = abs(1+colorLayers[i][0])/2*gradientRect.width
            segWidth += 1
            pygame.draw.rect(screen, ConvertColor(colorLayers[i][1], 'rgb'), pygame.Rect(gradientRect.left+offset, gradientRect.top, segWidth, gradientRect.height), width=0)
            offset += (segWidth - 1)
    uiMan.draw_ui(screen)
    if colorPicking:
        pygame.draw.rect(screen, (Rvalue*255, Gvalue*255, Bvalue*255), colorPickerRect, width=0)
        Rvalue, Rx = utils.Slider(colorPickerRect.left+5, colorPickerRect.width-10, Rx, colorPickerRect.top+7, screen, utils.darkGray, utils.lightGray, False, True)
        Gvalue, Gx = utils.Slider(colorPickerRect.left+5, colorPickerRect.width-10, Gx, colorPickerRect.top+7+((colorPickerRect.height-14)/2), screen, utils.darkGray, utils.lightGray, False, True)
        Bvalue, Bx = utils.Slider(colorPickerRect.left+5, colorPickerRect.width-10, Bx, colorPickerRect.top+7+((colorPickerRect.height-14)), screen, utils.darkGray, utils.lightGray, False, True)
    uiMan.update(dt/1000)
    events = pygame.event.get()
    for event in events:
        uiMan.process_events(event)
        if event.type == pygame.WINDOWRESIZED:
            screenSize = screen.get_size()
            uiMan.set_window_resolution(screenSize)

            radiusSlider.value_range = (100, int(min(screenSize)/2)) # Adjust the max radius to fill the screen

            AlignContainer(planetSettings, [5,5], 'TR')
            AlignContainer(autoSettings, [5,5], 'TL')
            gradientRect = gradientThing.rect.inflate((-gradientThing.border_width*2, -gradientThing.border_width*2))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.__dict__['pos']
            mouseRect = pygame.Rect(mousePos, (1,1))
            if gradientRect.colliderect(mouseRect):
                relativeMousePos = (mousePos[0]-gradientRect.left, mousePos[1]-gradientRect.top)
                scalePos = -(relativeMousePos[0]/(gradientRect.width/2)-1)
                print(f'Scaled Position: {scalePos}')
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED and debug:
            print(f"Slider Event: Value = {event.dict['value']}")
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            key = event.__dict__['key']
            if key == screenshotKey:
                utils.TakeScreenshot(screen)
            elif key == debugKey:
                debug = not debug
            if gradientRect.colliderect(mouseRect) and not colorPicking and key == pygame.K_p:
                ColorPicker(mousePos)
                colorPicking = True
            if colorPicking:
                if key == pygame.K_RETURN:
                    color = (Rvalue, Gvalue, Bvalue)
                    if colorChanging:
                        colorLayers[selectedLayer][1] = color
                        colorChanging = False
                    else:
                        colorLayers.append([scalePos, color])
                    colorLayers.sort(key=sorter, reverse=True)
                    print(f'Color Layers = {colorLayers}')
                    colorPicking = False
            if gradientRect.colliderect(mouseRect) and not colorMoving and key == pygame.K_m:
                separators = [layer[0] for layer in colorLayers]
                closestSep = [min(separators, key=lambda x:abs(x-scalePos))]
                closestSep.append(separators.index(closestSep[0]))
                colorMoving = True
                print(f'Closest Separator: {closestSep}')
            if colorMoving:
                if key == pygame.K_RETURN:
                    print(f'Selected Separator: {colorLayers[closestSep[1]][0]}')
                    mousePos = pygame.mouse.get_pos()
                    relativeMousePos2 = (mousePos[0]-gradientRect.left, mousePos[1]-gradientRect.top)
                    scalePos2 = -(relativeMousePos2[0]/(gradientRect.width/2)-1)
                    colorLayers[closestSep[1]][0] = scalePos2
                    colorMoving = False
                    if closestSep[0] == 1:
                        colorLayers.insert(0, [1, (.5,.5,.5)])
                    colorLayers.sort(key=sorter, reverse=True)
                    print(f'Color Layers = {colorLayers}')
            if gradientRect.colliderect(mouseRect) and not colorChanging and key == pygame.K_c:
                selectedLayer = 0
                for i in range(len(colorLayers)):
                    if scalePos < colorLayers[i][0]:
                        selectedLayer = i
                colorChanging = True
                ColorPicker(mousePos)
                Rx = utils.remap(0, 1, colorPickerRect.left+5, colorPickerRect.left+5+colorPickerRect.width-10, colorLayers[selectedLayer][1][0])
                Gx = utils.remap(0, 1, colorPickerRect.left+5, colorPickerRect.left+5+colorPickerRect.width-10, colorLayers[selectedLayer][1][1])
                Bx = utils.remap(0, 1, colorPickerRect.left+5, colorPickerRect.left+5+colorPickerRect.width-10, colorLayers[selectedLayer][1][2])
                colorPicking = True
                print(f'Selected Layer Index = {selectedLayer}')
    pygame.display.update()
    clock.tick(10)