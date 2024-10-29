import sys
import matplotlib.pyplot as plt
import pyperclip
import math
import numpy as np
from PIL import Image
file = sys.argv[1]
img = Image.open(file)
if img.mode == 'P':
    img = img.convert('RGBA', palette=img.palette)
f = plt.figure()
ax = plt.subplot(121)
ax.set_facecolor('000000')
plt.xticks([])
plt.yticks([])
plt.title('Original Image')
imgplot = plt.imshow(np.asarray(img))
pixels = img.load()
newImg = Image.new(img.mode, img.size)
print(img.palette)
pixelsNew = ""
pixNew = newImg.load()
def dectobin(dec):
    binary = 0
    for n in range(1,9):
        binary+=((10**(n-1))*math.floor((dec%(2**(n)))/(2**(n-1))))
    binary = str(binary)
    if len(binary) == 1:
        return f'0{binary}'
    else:
        return binary
#print(dectobin(1))
for j in range(img.size[0]):
    for i in range(img.size[1]):
        l=[]
        m=[]
        for k in range(3):
            l.append(dectobin(int((255/3)*math.floor((3*pixels[i,j][k]+(85*1.5))/255)/64)))
            m.append(85*int((pixels[i,j][k]+85/2)/85))
        pixelsNew += f'{dectobin(int(pixels[i,j][0])/64)}{l[0]}{l[1]}{l[2]},'
        pixNew[i,j] = (m[0], m[1], m[2])
img.close()
ax = plt.subplot(122)
ax.set_facecolor('000000')
plt.xticks([])
plt.yticks([])
plt.title('8-Bit Image')
plt.imshow(np.asarray(newImg))
plt.show()
#print(pixelsNew)
newImg.close()
#pyperclip.copy(pixelsNew[0:-1])
