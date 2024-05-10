import pynput
import keyboard
keyboard.add_hotkey('p',  lambda: print(pynput.mouse.Controller().position))
while True:
    pass