import matplotlib.pyplot as plt
from numpy import log, e
import matplotlib.markers
import tkinter.filedialog
from tkinter import ttk
from tkinter import *
import scipy.optimize
import numpy as np
import tkinter
import pandas
import scipy
import scipy.special

def OpenFile():
    global data
    with tkinter.filedialog.askopenfile(filetypes=[('.csv', '.csv')]) as file:
        data = pandas.read_csv(file)
        filename = file.name
    btext.set(f'File: {filename.rsplit("/")[-1]}')
    columns = data.columns
    cx.set_menu('Column X', *columns)
    cy.set_menu('Column Y', *columns)
def RunModel():
    bounds = None
    try: 
        model, bounds = models[opt.get()]
    except TypeError:
        model = models[opt.get()]
    xr = data[colx.get()].astype(str)
    x = []
    for i, val in enumerate(xr.values):
        val = val.replace(',', '').strip().replace(' ', '')
        xr[i] = float(val)
        #x.append(float(val))
    
    yr = data[coly.get()].astype(str)
    y = []
    for i, val in enumerate(yr.values):
        val: str = val
        val = val.replace(',', '').strip().replace(' ', '')
        yr[i] = float(val)
        #y.append(float(val))
    x = xr.astype(float)
    y = yr.astype(float)
    #x /= max(x)
    #y /= max(y)
    x = np.array(x)
    y = np.array(y)
    if bounds:
        params, covar = scipy.optimize.curve_fit(model, np.longdouble(x), np.longdouble(y), bounds=bounds)
        print(f'Variables are bounded to {bounds}')
    else:
        params, covar = scipy.optimize.curve_fit(model, x, y)
    print(params, opt.get())
    plt.scatter(x, y)
    plt.plot(np.longdouble(x), model(np.longdouble(x), *params))
    plt.show()
models = {'Linear': (lambda x,m,b:m*x+b), 'Quadratic': (lambda x,a,b,c:a*x*x+b*x+c), 'Cubic': (lambda x,a,b,c,d: a*x*x*x+b*x*x+c*x+d), 'Exponential': (lambda x,a,b:a*b**x), 'Logarithmic': (lambda x,a,b: a+b*log(x)), 'Logistic': ((lambda x,a,b,c,d: a*scipy.special.expit(b*x+c)-d))}
root = Tk()
opt = tkinter.StringVar()
colx = tkinter.StringVar()
coly = tkinter.StringVar()
frm = ttk.Frame(root, padding=50)
frm.grid()
btext = tkinter.StringVar(value='Open Data File')
b = ttk.Button(frm, textvariable=btext, command=OpenFile, width=50)
b.grid(column=0, columnspan=3, row=0)
ttk.Label(frm, text="Select Model").grid(column=0, row=1)
ttk.OptionMenu(frm, opt, 'Model', *models.keys()).grid(column=1, columnspan=2, row=1)
ttk.Label(frm, text="Select Columns").grid(column=0, row=2)
cx = ttk.OptionMenu(frm, colx, 'Column X', *[])
cx.grid(column=1, row=2)
cy = ttk.OptionMenu(frm, coly, 'Column Y', *[])
cy.grid(column=2, row=2)
ttk.Button(frm, text='Run Model', command=RunModel, width=50).grid(column=0, columnspan=3, row=3)
root.mainloop()
