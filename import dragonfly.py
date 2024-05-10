import dragonfly
import re
i=0
windows = dragonfly.Window.get_all_windows()
for window in windows:
    index = windows.index(window)
    windows[index] = window.executable
for title in sorted(windows):
    title:str = re.sub(r'.*?\\', '', title)
    if title != '':
        print(title, i)
    i+=1