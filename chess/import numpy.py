import numpy
dasd = numpy.ndarray((2,2), dtype=str)
a = numpy.arange(6).reshape(2,3)
for x in numpy.nditer(a):
    print(x, end=' ')