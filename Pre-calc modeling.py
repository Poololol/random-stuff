import matplotlib.figure
import matplotlib.backends.backend_qt
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from math import e
def move_figure(f:matplotlib.figure.Figure, x, y):
    m:matplotlib.backends.backend_qt.FigureManagerQT = f.canvas.manager
    w = m.window
    w.resize(int(screenSize[0]/2), int(screenSize[1]/2)-32)
    w.move(x, y)
screenSize = (1536, 1024-48)

f = plt.figure(1)
plt.subplot(221)
x = np.arange(2017,2030, .1)
y = ((20666.66*(x**2))-(83348833.35*x)+(8.4036942513*(10**10)))/1000000
ye = (0.0464445*(e**(0.253331*(x-1955.7)))+21826.2)/1000000
x2 = [2018,2019,2021,2022]
y2 = np.array([369000, 423000, 750000, 928000])/1000000
dx = np.array([2026, 2029])
dy = ((20666.66*(dx**2))-(83348833.35*dx)+(8.4036942513*(10**10)))/1000000
dye =  (0.0464445*(e**(0.253331*(dx-1955.7)))+21826.2)/1000000
plt.title('E-Bike Sales vs. Time')
plt.xlabel('Year')
plt.ylabel('E-Bike Sales (Millions)')
plt.plot(x, y, 'g-', x, ye, 'r-', x2, y2, 'bo', 2020, 416000/1000000, 'ko', dx, dy, 'go', dx, dye, 'ro')
plt.legend(['Quadratic Model', 'Exponential Model', 'Data', '2020 Data (Not Used)', 'Quadratic Predicions', 'Exponential Predictions'])
plt.annotate(f'({dx[0]}, {round(dy[0],2)})', [dx[0]+.2, dy[0]-.2])
plt.annotate(f'({dx[1]}, {round(dy[1],2)})', [dx[1]-.3, dy[1]-.4])
plt.annotate(f'({dx[0]}, {round(dye[0],2)})', [dx[0]-2, dye[0]+.1])
plt.annotate(f'({dx[1]}, {round(dye[1],2)})', [dx[1]-2, dye[1]+.1])
#move_figure(f, 0, 0)

#f = plt.figure(2)
plt.subplot(222)
x = np.arange(1994, 2030, .1)
y = (0.000152487*(e**(-0.17247*(x-2092.63))))+153.326
plt.title('Battery Cost vs. Time')
plt.xlabel('Year')
plt.ylabel('Cost per kWh of Capacity ($/kWh)')
plt.plot(x, y, 'g-', [1995,1997,1999,2003,2005,2010,2015], [3200,2500,1800,830,630,370,350], 'bo')
plt.legend(['Model', 'Data'])
#move_figure(f, int(screenSize[0]/2), 0)

#f = plt.figure(3)
plt.subplot(223)
x = np.arange(2015, 2030, .1)
y = .18*x-360.685
x2 = [2016, 2017, 2018, 2019, 2021, 2023]
y2 = [2.14,2.42,2.72,2.60,3.01,3.52]
x3 = np.arange(1992, 2016, 1)
y3 = [1.09,1.07,1.08,1.11,1.20,1.20,1.03,1.14,1.48,1.42,1.35,1.56,1.85,2.27,2.57,2.80,3.25,2.35,2.78,3.52,3.62,3.51,3.36,2.43]
x4 = [2020, 2022]
y4 = [2.17, 3.95]
plt.title('Gas Prices vs. Time')
plt.xlabel('Year')
plt.ylabel('Gas Prices ($/gal)')
plt.plot(x, y, 'g-', x2, y2, 'bo', x4, y4, 'ko', x3, y3, 'ro')
plt.legend(['Model', 'Data', 'Outlier Data (Not Used)', 'Data before 2016 (Not Used)'])
#move_figure(f, 0, int(screenSize[1]/2))

#f = plt.figure(4)
plt.subplot(224)
x = np.arange(2015, 2030, .1)
y = .18*x-360.685
x2 = [2016, 2017, 2018, 2019, 2021, 2023]
y2 = [2.14,2.42,2.72,2.60,3.01,3.52]
x4 = [2020, 2022]
y4 = [2.17, 3.95]
plt.title('Gas Prices vs. Time')
plt.xlabel('Year')
plt.ylabel('Gas Prices ($/gal)')
plt.plot(x, y, 'g-', x2, y2, 'bo', x4, y4, 'ko')
plt.legend(['Model', 'Data ', 'Outlier Data (Not Used)'])
#move_figure(f, int(screenSize[0]/2), int(screenSize[1]/2))

#plt.tight_layout(top=0.959,bottom=0.063,left=0.043,right=0.99,hspace=0.217,wspace=0.115)
f.set_layout_engine(layout='tight')
plt.show()