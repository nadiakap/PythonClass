from scipy.optimize import curve_fit
import matplotlib.pyplot as pl
from numpy import genfromtxt
#import numpy as np
#import xlswriter

import statsmodels.api as os

data_file = 'AppleInputData.csv'
#C:/Users/udlern/DesktopAppleInputData.csv
my_data = genfromtxt(data_file,delimiter = ',',skip_header=1)
print(type(my_data))
print(my_data.shape)
x=my_data[:,3]
y=my_data[:,4]

# Creating a function to model and create data
def func(x, a, b):
    return a * x + b
#print ('pcov', pcov)

# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, y)
res = os.OLS(y,x)
res = res.fit()

yExp = func(x, *popt)

#print('yExp', yExp)
# popt returns the best fit values for parameters of
# the given model (func).

#print ('pcov', pcov)

pl.figure()
#pl.plot(x, yn, label='Data', marker='o')
pl.scatter(x, y,s=10)
pl.plot(x, yExp, 'r-',ls='--', label="fitted line")

pl.legend()
pl.show()
print('slope=',popt[0])
print('intercept=',popt[1])

