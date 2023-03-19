import scipy.optimize as sopt
import pandas as pd
import numpy as np
# Read data
data_file = 'DietDataFormatted.xlsx'
df_A = pd.read_excel(data_file,sheet_name='NutritionalInfo',header = 0,index_col = 0)
A = np.transpose(df_A.to_numpy())
df_b = pd.read_excel(data_file,sheet_name='Requirements',header = 0,index_col = 0)
b = df_b.to_numpy()[1]
b_lower = -df_b.to_numpy()[0]
df_c = pd.read_excel(data_file,sheet_name='UnitCosts',header = None,index_col = 0)
c = df_c.to_numpy().flatten()

A_lower = -A
A_ub = np.vstack([A,A_lower])
b_ub = np.vstack([b,b_lower]).flatten()

bounds = (0, 4)
bounds1 = (0, 3)
bounds2 = (0, 7)
bounds = (bounds,bounds,bounds,bounds1,bounds,bounds2)
res=sopt.linprog(c,A_ub=A_ub,b_ub=b_ub,bounds=bounds)
print ('**********************************************************')   
print ('cost of daily meal, optimized:', res.fun)
print ('**********************************************************')   
print ('here is the meal plan ( number of servings of each food):')
for i in range(len(df_A.index)):
    print (df_A.index[i], ':', res.x[i])

print ('**********************************************************')    
print ('you are getting these nutrients:')    
for j in range(len(df_A.columns)):
    nutrient_j = 0.0
    for i in range(len(df_A.index)):
        nutrient_j += A[j,i]*res.x[i]
    print (df_A.columns[j] , ':', nutrient_j)    


