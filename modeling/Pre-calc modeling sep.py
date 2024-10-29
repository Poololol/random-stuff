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
ebikeSalesMult = 1000

f = plt.figure('Quadratic')
#plt.subplot(221)
x = np.arange(2017,2030, .1)
y = ((20666.6666699*(x**2))-(83348833.3464*x)+(8.4036942513*(10**10)))/ebikeSalesMult
x2 = [2018,2019,2021,2022]
y2 = np.array([369000, 423000, 750000, 928000])/ebikeSalesMult
dx = np.array([2026, 2029])
dy = ((20666.6666699*(dx**2))-(83348833.3464*dx)+(8.4036942513*(10**10)))/ebikeSalesMult
plt.title('E-Bike Sales vs. Time')
plt.xlabel('Year')
plt.ylabel('E-Bike Sales (Thousands)')
plt.plot(x, y, 'g-', x2, y2, 'bo', 2020, 416000/ebikeSalesMult, 'ko', dx, dy, 'go')
plt.legend(['Quadratic Model', 'Data', '2020 Data (Not Used)', 'Quadratic Predicions'])
plt.annotate(f'({dx[0]}, {round(dy[0],2)})', [dx[0]-3.3, dy[0]-.2])
plt.annotate(f'({dx[1]}, {round(dy[1],2)})', [dx[1]-3.3, dy[1]-.4])
#move_figure(f, 0, 0)

f= plt.figure('Exponential')
#plt.subplot(222)
x = np.arange(2017,2030, .1)
ye = (0.0464445*(e**(0.253331*(x-1955.7)))+21826.2)/ebikeSalesMult
x2 = [2018,2019,2021,2022]
y2 = np.array([369000, 423000, 750000, 928000])/ebikeSalesMult
dx = np.array([2026, 2029])
dye =  (0.0464445*(e**(0.253331*(dx-1955.7)))+21826.2)/ebikeSalesMult
plt.title('E-Bike Sales vs. Time')
plt.xlabel('Year')
plt.ylabel('E-Bike Sales (Thousands)')
plt.plot(x, ye, 'r-', x2, y2, 'bo', 2020, 416000/ebikeSalesMult, 'ko', dx, dye, 'ro')
plt.legend(['Exponential Model', 'Data', '2020 Data (Not Used)', 'Exponential Predictions'])
plt.annotate(f'({dx[0]}, {round(dye[0],2)})', [dx[0]-3.3, dye[0]+.2])
plt.annotate(f'({dx[1]}, {round(dye[1],2)})', [dx[1]-3.3, dye[1]+.2])

f = plt.figure('Average')
#plt.subplot(223)
x = np.arange(2017,2030, .1)
x2 = [2018,2019,2021,2022]
y2 = np.array([369000, 423000, 750000, 928000])/ebikeSalesMult
dx = np.array([2026, 2029])
dya = (dy+dye)/2
ya = (y+ye)/2
plt.title('E-Bike Sales vs. Time')
plt.xlabel('Year')
plt.ylabel('E-Bike Sales (Thousands)')
plt.plot(x, ya, 'c-', x2, y2, 'bo', 2020, 416000/ebikeSalesMult, 'ko', dx, dya, 'co')
plt.legend(['Average Model', 'Data', '2020 Data (Not Used)', 'Average Predictions'])
plt.annotate(f'({dx[0]}, {round(dya[0],2)})', [dx[0]+.2, dya[0]-.2])
plt.annotate(f'({dx[1]}, {round(dya[1],2)})', [dx[1]-.3, dya[1]-.4])

f = plt.figure('Quadratic + Exponential + Average')
#plt.subplot(224)
x = np.arange(2017,2030, .1)
y = ((20666.66*(x**2))-(83348833.35*x)+(8.4036942513*(10**10)))/ebikeSalesMult
ye = (0.0464445*(e**(0.253331*(x-1955.7)))+21826.2)/ebikeSalesMult
x2 = [2018,2019,2021,2022]
y2 = np.array([369000, 423000, 750000, 928000])/ebikeSalesMult
dx = np.array([2026, 2029])
dy = ((20666.66*(dx**2))-(83348833.35*dx)+(8.4036942513*(10**10)))/ebikeSalesMult
dye =  (0.0464445*(e**(0.253331*(dx-1955.7)))+21826.2)/ebikeSalesMult
ya = (y+ye)/2
plt.title('E-Bike Sales vs. Time')
plt.xlabel('Year')
plt.ylabel('E-Bike Sales (Thousands)')
plt.plot(x, y, 'g-', x, ye, 'r-', x, ya, 'c-', x2, y2, 'bo', 2020, 416000/ebikeSalesMult, 'ko', dx, dy, 'go', dx, dye, 'ro', dx, dya, 'co')
plt.legend(['Quadratic Model', 'Exponential Model', 'Average Model', 'Data', '2020 Data (Not Used)', 'Quadratic Predicions', 'Exponential Predictions', 'Average Predictions'])
plt.annotate(f'({dx[0]}, {round(dy[0],2)})', [dx[0]+.2, dy[0]-.2])
plt.annotate(f'({dx[1]}, {round(dy[1],2)})', [dx[1]-.3, dy[1]-.4])
plt.annotate(f'({dx[0]}, {round(dye[0],2)})', [dx[0]-2, dye[0]+.1])
plt.annotate(f'({dx[1]}, {round(dye[1],2)})', [dx[1]-2, dye[1]+.1])
#move_figure(f, 0, 0)


f = plt.figure('Battery Cost')
#plt.subplot(222)
x = np.arange(1994, 2030, .1)
y = (0.000152487*(e**(-0.17247*(x-2092.63))))+153.326
plt.title('Battery Cost vs. Time')
plt.xlabel('Year')
plt.ylabel('Cost per kWh of Capacity ($/kWh)')
plt.plot(x, y, 'g-', [1995,1997,1999,2003,2005,2010,2015], [3200,2500,1800,830,630,370,350], 'bo')
plt.legend(['Model', 'Data'])
#move_figure(f, int(screenSize[0]/2), 0)

f = plt.figure('Gas Prices Full')
#plt.subplot(223)
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

f = plt.figure('Gas Prices')
#plt.subplot(224)
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


f = plt.figure('Carbon Emissions Multi')
x = np.arange(2016, 2030, .1)
y = ((6.35*(10**9))*(e**(0.318598*(x-2040.78)))-(2.702*(10**6)))/100
x2 = [2018, 2019, 2020, 2021, 2022]
scale = 10**6/100
y2 = [1.6974*scale, 3.6432*scale, 5.5568*scale, 9.0068*scale, 13.2756*scale]
plt.title('Reduction in Carbon Emissions vs. Time')
plt.xlabel('Year')
plt.ylabel('CO2 (Millions of metric tons)')
plt.plot(x, y, 'g-', x, y*.5, 'c-', x2, y2, 'bo', x, y*.8, 'c-', x, y*.25, 'c-')
plt.legend(['Model', 'Percent', 'Data'])
plt.annotate('50%', (x[100], y[100]*.5+.1*scale))
plt.annotate('80%', (x[100], y[100]*.8+.1*scale))
plt.annotate('25%', (x[100], y[100]*.25+.1*scale))

f = plt.figure('Carbon Emissions')
x = np.arange(2016, 2030, .1)
y = ((6.35*(10**9))*(e**(0.318598*(x-2040.78)))-(2.702*(10**6)))/100
x2 = [2018, 2019, 2020, 2021, 2022]
scale = 10**6/100
y2 = [1.6974*scale, 3.6432*scale, 5.5568*scale, 9.0068*scale, 13.2756*scale]
plt.title('Reduction in Carbon Emissions vs. Time')
plt.xlabel('Year')
plt.ylabel('CO2 (Millions of metric tons)')
plt.plot(x, y, 'g-', x2, y2, 'bo')
plt.legend(['Model', 'Data'])

#f.set_layout_engine(layout='tight')
plt.show()
