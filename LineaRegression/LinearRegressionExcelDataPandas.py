#from scipy.optimize import curve_fit
#import matplotlib.pyplot as pl
import pandas as pd

data_file = 'AppleInputData.csv'
#C:/Users/udlern/DesktopAppleInputData.csv
my_data = pd.read_csv(data_file)
print(type(my_data))
print(my_data.shape)

