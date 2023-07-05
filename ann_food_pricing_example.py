# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:40:04 2023

@author: dmitr
"""
import pandas as pd
import numpy as np

#perceptron function with identity activation
def perceptron(w,xx):
    s = 0
    m = xx.shape[0]
    nn = w.shape[0]
    k = int(nn/(2*m))
    for j in range(k):
        for i in range(m):
            s += xx.iloc[i]*w[i*(j+1)]*w[nn-j-1]
    return s
#sum of suares objective f
def sumsquares(w,f,x,y):
    """
    f - function to fit
    X, y - observations
    """
    s=0
    n = x.shape[0]
    for i in range(n):
        #s += 1+y[i]+x[i]
        s += abs(y[i]-f(w,x.iloc[i]))
    return np.sqrt(s)  

data_file = 'NutritionFacts.xlsx'

df = pd.read_excel(data_file,header=0,index_col = 0)
y = np.asarray(df['NewCost'])
X = df.drop(['Cost','Serving Size','NewCost'],axis=1)
n = X.shape[0]
m = X.shape[1]

from scipy.optimize import fmin
#k - number of neurons in the hidden layer. 
k = 2
w0 =np.random.rand(m*k*2)
print(perceptron(w0,X.iloc[0]))
print(sumsquares(w0,perceptron,X,y))
res = fmin(sumsquares,w0,args=(perceptron,X,y,))