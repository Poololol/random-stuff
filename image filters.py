import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import sys
try:
    file = sys.argv[1]
except IndexError:
    file = 'Pen Tool.png'
try:
    img = Image.open(file)
except FileNotFoundError:
    file = 'onedrive/programs/Pen Tool.png'
    img = Image.open(file)
try:
    imgFilter = sys.argv[2]
except IndexError:
    imgFilter = "Matrix"
if imgFilter == "Matrix":
    func = lambda r,g,b: (int(((r/255)**(7/5))*255), int(g), int(((b/255)**(8/5))*255))
else:
    func = lambda r,g,b: (int(r),int(g),int(b))
pixels = img.load()
imgNew = Image.new(img.mode, img.size)
pixelsNew = imgNew.load()
print(img.size)
for j in range(img.size[1]):
    for i in range(img.size[0]):
        #print(pixels[i,j])
        if file.endswith('.png'):
            r,g,b = func(pixels[i,j][0], pixels[i,j][1], pixels[i,j][2])
            pixelsNew[i,j] = (r, g, b, pixels[i,j][3])
        else:
            pixelsNew[i,j] = func(pixels[i,j][0], pixels[i,j][1], pixels[i,j][2])

f = plt.figure()
f.set_layout_engine('tight')

plt.subplot(121)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.imshow(np.asarray(img))

plt.subplot(122)
plt.title(f'Image w/ {imgFilter} Filter')
plt.xticks([])
plt.yticks([])
plt.imshow(np.asarray(imgNew))

plt.show()
