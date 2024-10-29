import matplotlib.pyplot as plt
import matplotlib.markers
import scipy.optimize
import numpy as np
import pandas
import math

pandas.options.mode.copy_on_write = True
def model(x, a, b, c):
    y = a*x*x+b*x+c
    return y

'''data = pandas.read_csv("C:/Users/638278/Downloads/bf34f6e8-4dd0-11ef-a154-3860777c1fe6.csv")
x = data['Year'].astype(int)
y = data['Population']
for i, pop in enumerate(y.values):
    pop = pop.replace(',', '')
    y[i] = float(pop)'''

data = pandas.read_csv("C:/Users/638278/Downloads/NApop.csv")
x = data['Year'].astype(int)
xp = x[75:]
xd = x[0:75]
y = data['Population']
yd = []
yp = []
for i, pop in enumerate(y.values):
    pop:str = pop
    pop = pop.strip()
    pop = pop.replace(' ', '')
    if x[i] <= 2024:
        yd.append(float(pop))
        y[i] = float(pop)
    else:
        yp.append(float(pop))
        y[i] = float(pop)
paramBounds = [[-np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf]]

'''np.random.seed(1)
data = [np.arange(10, 110, 1), (np.arange(10, 110, 1) + (20*(np.random.rand((100))-.5)))**4]
x = data[0]
y = data[1]'''

x2 = np.arange(x[0], x.tolist()[-1]+50, 1)
f = plt.figure()
plt.scatter(xd, yd, s=5**2, c='tab:blue')
plt.scatter(xp, yp, s=5**2, c='tab:blue', marker=matplotlib.markers.MarkerStyle('o', 'none'))
params, covar = scipy.optimize.curve_fit(model, xd, yd, bounds=paramBounds)
params2, covar2 = scipy.optimize.curve_fit(model, x, y, bounds=paramBounds)
params3, covar3 = scipy.optimize.curve_fit(model, xp, yp, bounds=paramBounds)
print(f'Equation: {params2[0]}x^2+{params2[1]}x+{params2[2]}')
print(np.linalg.cond(covar), np.diag(covar))
plt.plot(x2, model(x2, *params), 'tab:orange')
plt.plot(x2, model(x2, *params2), 'r')
plt.plot(x2, model(x2, *params3), 'tab:cyan')
plt.legend(['Data', 'Predicted Data', 'Model w/ Data', 'Model w/ all Data', 'Model w/ Pred. Data'])
axis = f.axes[0]
axis.set_ybound(upper=800000)
plt.show()
