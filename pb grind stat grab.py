import pytesseract
from PIL import Image
import numpy as np
import pyperclip
pytesseract.pytesseract.tesseract_cmd ='/Users/braed/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
path = "C:/Users/braed/Pictures/Screenshot 2024-07-04 1404001.png"
def processImage(image: Image.Image) -> list[str]:
    raw: str = pytesseract.image_to_string(image, lang ='eng', config='--psm 6')
    split = raw.split('\n')
    while True:
        try:
            split.remove('')
        except ValueError:
            break
    return split
def ImagePreprocess(image: Image.Image) -> Image.Image:
    image = image.convert('RGBA')
    imData = np.array(image)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = imData.T # Temporarily unpack the bands for readability
    # Replace white with red... (leaves alpha values alone...)
    white_areas = (red <= 150) & (green <= 150) & (blue <= 150)
    imData[..., :-1][white_areas.T] = (0, 0, 0) # Transpose back needed
    return Image.fromarray(imData)
image = ImagePreprocess(Image.open(path))
maps = processImage(image.crop((0,0,400,image.height)))
maps[0] = 'Total'
times = processImage(image.crop((400,0,600,image.height)))
fins = processImage(image.crop((700,0,900,image.height)))
resets = processImage(image.crop((900,0,1100,image.height)))
respawns = processImage(image.crop((1100,0,1300,image.height)))
data = {}
for i, mapName in enumerate(maps):
    data[mapName] = {'Time Spent': times[i], 'Num Fins': fins[i], 'Num Resets': resets[i], 'Num Respawns': respawns[i]}
pyperclip.copy(str(data))
#print(respawns)
#print((maps, len(maps)), (times, len(times)), (fins, len(fins)), (respawns, len(respawns)), sep='\n\n')