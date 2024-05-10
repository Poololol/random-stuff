import pytesseract
from PIL import ImageGrab
import pygame
import pyautogui
import keyboard
clock = pygame.time.Clock()
pygame.display.init()
answers = {'This is a test': 'iuksau', 'test2': 'ldld'}
button = [0, (350, 600), (1000, 600), (200, 900), (1000, 900)]
run = False
def pause():
    global run
    run = not run
    print('aa')
def quitProgram():
    pygame.display.quit()
    quit()
keyboard.add_hotkey('q', quitProgram)
keyboard.add_hotkey('p', pause)
def imToString():
    pytesseract.pytesseract.tesseract_cmd ='/Users/638278/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
    cap = ImageGrab.grab(bbox=(0, 130, 1000, 483), include_layered_windows=True)
    q:str = pytesseract.image_to_string(cap, lang ='eng')
    cap = ImageGrab.grab(bbox=(36, 563, 694, 738), include_layered_windows=True)
    a1:str = pytesseract.image_to_string(cap, lang ='eng')
    cap = ImageGrab.grab(bbox=(770, 552, 1453, 751), include_layered_windows=True)
    a2:str = pytesseract.image_to_string(cap, lang ='eng')
    cap = ImageGrab.grab(bbox=(24, 795, 721, 994), include_layered_windows=True)
    a3:str = pytesseract.image_to_string(cap, lang ='eng')
    cap = ImageGrab.grab(bbox=(767, 797, 1445, 999), include_layered_windows=True)
    a4:str = pytesseract.image_to_string(cap, lang ='eng')
    return list((q, a1, a2, a3, a4))
while True:
    if run:
        text = imToString()
        for i in range(0,5):
            text[i] = text[i].strip('\n')
            if i!=0:
                try:
                    if answers[text[0]] == text[i]:
                        pyautogui.click(button[i][0], button[i][1])
                        clock.tick(.5)
                        pyautogui.click()
                except KeyError:
                    pass
    

    '''
    b = ImageGrab.grab(bbox=(640, 550, 825, 625), include_layered_windows=True)
    a = pytesseract.image_to_string(b, lang='eng')
    print(a)
    if a == 'Next Round':
        pyautogui.click(750, 575)
    '''