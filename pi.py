import random
import matplotlib
numInside = 0
numOutside = 0
for i in range(1000000):
    x = (random.random()*2)-1
    y = (random.random()*2)-1
    if x**2+y**2<=1:
        numInside += 1
    else:
        numOutside += 1
print(numInside/numOutside)