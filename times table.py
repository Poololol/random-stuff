import numpy
x = 14
y = 71
grid = numpy.zeros((y,x))
for i in range(y):
    for j in range(x):
        grid[i,j] = (i+1)*(j+1)
print(grid)