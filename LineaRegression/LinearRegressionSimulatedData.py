import numpy as np

import scipy.optimize as so
import matplotlib.pyplot as pl
#import statsmodels
#import sklearn 


#function to model (and create) data
def func_line(x, m, b):
    return m * x  + b
 
pl.figure()   
# Generating clean data
x = np.linspace(0, 10, 100)  
y = func_line(x, 1, 2)
#pl.scatter(x, y,s=10)
#pl.plot(x, y, 'r-',ls='--', label="true line")
#print('y',y)

# Adding noise to the data
yn = y + np.random.normal(0,1,size=len(x))
pl.scatter(x, yn,s=10)

# Executing curve_fit on noisy data
popt, pcov = so.curve_fit(func_line, x, yn)
yExp = func_line(x, popt[0], popt[1])
pl.plot(x, yExp, label = 'fitted line')

print('fitted line slope = ', popt[0])
print('fitted line intercept = ', popt[1])

# popt returns the best fit values for parameters of
# the given model (func).

pl.legend()
pl.show()
