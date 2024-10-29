import matplotlib.pyplot as plt
import opensimplex
import numpy as np
import utils
from PIL import Image

size = (250,250)
scale = 75
layers = 3
noiseLayers = []
freq = 10
amp = 1

n1 = Image.new("RGB", size=size)
n1Pix = n1.load()
n2 = Image.new("RGB", size=size)
n2Pix = n2.load()
n3 = Image.new("RGB", size=size)
n3Pix = n3.load()
n12 = Image.new("RGB", size=size)
n12Pix = n12.load()
for _ in range(layers):
    noiseLayers.append(opensimplex.noise2array(np.arange(0, size[0]/freq, 1/freq), np.arange(0, size[1]/freq, 1/freq))/amp)
    freq*=2
    amp*=.5
#print(noiseLayers)
for x in range(size[0]):
    for y in range(size[1]):
        c = int(utils.remap(-1, 1, 0, 255, noiseLayers[0][x][y]))
        n1Pix[x,y] = (c, c, c)
for x in range(size[0]):
    for y in range(size[1]):
        c = int(utils.remap(-1, 1, 0, 255, noiseLayers[1][x][y]))
        n2Pix[x,y] = (c,c,c)
for x in range(size[0]):
    for y in range(size[1]):
        c = int(utils.remap(-1, 1, 0, 255, noiseLayers[2][x][y]))
        n3Pix[x,y] = (c,c,c)
for x in range(size[0]):
    for y in range(size[1]):
        for i in range(layers):
            c+=int(utils.remap(-1,1,0,255,noiseLayers[i][x][y]))
        c = int(c/layers)
        n12Pix[x,y] = (c,c,c)

f = plt.figure()
plt.subplot(221)
plt.xticks([])
plt.yticks([])
plt.title('Noise Layer 1')
plt.imshow(np.asarray(n1))

plt.subplot(222)
plt.xticks([])
plt.yticks([])
plt.title('Noise Layer 2')
plt.imshow(n2)

plt.subplot(223)
plt.xticks([])
plt.yticks([])
plt.title('Noise Layer 3')
plt.imshow(np.asarray(n3))

plt.subplot(224)
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.title('Combined Noise Layers')
plt.imshow(n12)

plt.show()