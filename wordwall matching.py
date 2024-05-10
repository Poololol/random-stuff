import pynput
import time
import pytesseract
import keyboard
from PIL import ImageGrab
mouse = pynput.mouse.Controller()
fullscreen = True
atSchool = False
sleepTime = .1
def end():
    mouse.position = (1500,500)
    quit()
keyboard.add_hotkey('q', end)
pytesseract.pytesseract.tesseract_cmd ='/Users/638278/AppData/Local/Programs/Tesseract-OCR/tesseract.exe' if atSchool else '/Users/braed/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
slotsArea1S = (480, 80, 0, 950) if fullscreen else (400, 200, 0, 700) 
slotsArea2S = (0+5, 86, 1475, 995) if fullscreen else (0+5, 200, 1100, 700) 
wordBank1S = (27, 86, 170, 930) if fullscreen else (160, 240, 240, 700)
wordBank2S = (170, 86, 313, 930) if fullscreen else (240, 240, 320, 700)
slotsArea1H = (501, 86, 1130, 995) if fullscreen else (400, 200, 1100, 700) 
slotsArea2H = (1280, 86, 1905, 995) if fullscreen else (400, 200, 1100, 700) 
wordBank1H = (30, 91, 180, 977) if fullscreen else (160, 240, 240, 700)
wordBank2H = (175, 91, 333, 980) if fullscreen else (240, 240, 320, 700)
slotsArea1 = slotsArea1S if atSchool else slotsArea1H
slotsArea2 = slotsArea2S if atSchool else slotsArea2H
wordBank1 = wordBank1S if atSchool else wordBank1H
wordBank2 = wordBank2S if atSchool else wordBank2H
slot1X = 365
slot1Y = 101
slotGapX = 1140-364
slotGapY = 59
slotdict = {}
word1X = 35
word1Y = 100
answerBad = '''apagar
to turn off
castigar
to punish
contaminar
to pollute
destruir
to destroy
reciclar
to recycle
reducir
to reduce
usar el transporte público
to use public transportation
talar los árboles
to cut down trees
proteger el planeta
to protect the planet
el medioambiente
the environment
la deforestación
deforestation
la contaminación
the pollution
las fábricas
factories
los químicos
chemicals
el derrame de petróleo
oil spill
las latas
cans
el cartón
cardboard
el papel
paper
las botellas de vidrio
glass bottles
las botellas de plástico
plastic bottles
las bolsas de plástico
plastic bags
pasar leyes
to pass laws
pagar multas
to pay fines
la energía solar
solar energy
la energía nuclear
nuclear energy
la energía hidroeléctrica
hydroelectric power
la energía eólica
wind energy
habrá más...
there will be more...
la selva tropical
the rain forest
el clima
the climate
'''
splitAnswers = answerBad.split('\n')
answers = {}
mergers = ['la energía', 'proteger', 'el derrame', 'las botellas', 'el', 'los', 'la', 'usar el transporte', 'las bolsas', 'la selva', 'talar los', ]
for i in range(len(splitAnswers)-1):
    if i%2==0:
        answers = answers | {splitAnswers[i]: splitAnswers[i+1]}
#print(answers)
time.sleep(1)
mouse.position = (952, 534)
time.sleep(sleepTime)
mouse.click(pynput.mouse.Button.left)
time.sleep(2)
cap = ImageGrab.grab(bbox=slotsArea1, include_layered_windows=True)
slotstr:str = pytesseract.image_to_string(cap, lang ='eng')
slots = slotstr.replace('\n\n', '\n').replace('!', '').replace('}', '').replace("‘", '').replace('“', '').split('\n')
cap = ImageGrab.grab(bbox=slotsArea2, include_layered_windows=True)
slotstr:str = pytesseract.image_to_string(cap, lang ='eng')
slots += slotstr.replace('\n\n', '\n').replace('!', '').replace('}', '').replace("‘", '').replace('“', '').split('\n')
slots.remove('')
slots.remove('')
for i, slot in enumerate(slots):
    slot = slot.strip()
    #print(i, slot, i//15, i%15)
    position = (slot1X+slotGapX*(i//15), slot1Y+slotGapY*(i%15))
    #print(position, i, i//15, i%15)
    slotdict = slotdict | {slot: position}
cap = ImageGrab.grab(bbox=wordBank1, include_layered_windows=True)
wordstr:str = pytesseract.image_to_string(cap, lang='spa')
words = wordstr.replace('\n\n', '\n').replace('!', '').replace('}', '').replace("‘", '').replace('“', '').split('\n')
cap = ImageGrab.grab(bbox=wordBank2, include_layered_windows=True)
wordstr:str = pytesseract.image_to_string(cap, lang='spa')
words += wordstr.replace('\n\n', '\n').replace('!', '').replace('}', '').replace("‘", '').replace('“', '').split('\n')
dele = []
for i in range(len(words)):
    if words[i] in mergers:
        words[i] = words[i]+ ' ' + words[i+1]
        dele.append(i+1)
for i, delet in enumerate(dele):
    words.pop(delet-i)
words.remove('')
words.remove('')
print(words.__len__())
#print(answers)
print(slotdict.__len__())
for i, word in enumerate(words):
    mouse.position = (word1X, word1Y)
    time.sleep(sleepTime)
    mouse.press(pynput.mouse.Button.left)
    time.sleep(sleepTime)
    mouse.position = slotdict[answers[word]]
    time.sleep(sleepTime)
    mouse.release(pynput.mouse.Button.left)
    time.sleep(sleepTime)
mouse.position = (975, 1033)
time.sleep(sleepTime)
mouse.click(pynput.mouse.Button.left)
#print(slots)