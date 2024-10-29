import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pandas import read_csv, options
import numpy as np
options.mode.copy_on_write = True

def model(x,a,b,c):
    return a*(x**2)+b*x+c

data = read_csv("C:/Users/638278/Downloads/NApop.csv")
x=data['Year'].astype(float)
y=data['Population']
for i, pop in enumerate(y.values):
    y[i] = float(pop.strip().replace(' ', ''))
    
params, covar = curve_fit(model, x, y)
print(params, covar, np.linalg.cond(covar), np.diag(covar), sep='\n\n')
plt.scatter(x, y)
plt.plot(x, model(x, *params))
plt.show()
