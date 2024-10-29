import pyperclip
width = 300
height = 100
depth = 300
offset = (0, -200, 150)
corner = ((250-(width/2))-offset[0], (250-(height/2))-offset[1], (150-(depth/2))-offset[2])
output = []
output.append((corner[0], corner[1], corner[2]))
output.append((corner[0]+width, corner[1], corner[2]))
output.append((corner[0], corner[1]+height, corner[2]))
output.append((corner[0]+width, corner[1]+height, corner[2]))
output.append((corner[0], corner[1], corner[2]+depth))
output.append((corner[0]+width, corner[1], corner[2]+depth))
output.append((corner[0], corner[1]+height, corner[2]+depth))
output.append((corner[0]+width, corner[1]+height, corner[2]+depth))
pyperclip.copy(str(output))
print(output)