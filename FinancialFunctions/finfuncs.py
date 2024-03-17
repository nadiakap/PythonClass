import numpy as np
import numpy_financial as npf
import pandas as pd
import scipy as sp

def read_data(filename):
     finfunc_df = pd.read_excel(filename,
                                 header=0,
                                 usecols=['ArgValues'])
     #variant 1
     my_data = list(finfunc_df['ArgValues'])
     rate = my_data[0]
     nper = my_data[1]
     pmt = my_data[2]
     pv = my_data[3]                          
     return (rate,nper,pmt,pv)

def my_pv(x, *params):
    
    return npf.fv(params[0],params[1],params[2],x)+112.68

print('***reading input data from Excel spreadsheet**')
r,n,pmt,pv = read_data('ExcelFinFuncData.xlsx')

print('**********printing result of computation*****')
#find future value of 100$ investment in 12 months, with annual rate 12%
fv = npf.fv(r,n/12,pmt,pv)
print('fv:',fv)

#find present value of investment that is worth 112$ in 12 months, with annual rate 12%
pv = npf.pv(r,n/12,pmt,fv)
#alernative computation using goalseek
#video on goalseek capabilities in Python
#https://www.google.com/search?q=scipy+fsolve+goal+seek+example&sca_esv=036e417f0382002b&source=hp&ei=4N_1Zb7VE6eg5NoP5YiCuAk&iflsig=ANes7DEAAAAAZfXt8AwExqGtoit5xCoddGgONiO0DDpk&ved=0ahUKEwi-xdL6r_mEAxUnEFkFHWWEAJcQ4dUDCA8&uact=5&oq=scipy+fsolve+goal+seek+example&gs_lp=Egdnd3Mtd2l6Ih5zY2lweSBmc29sdmUgZ29hbCBzZWVrIGV4YW1wbGUyCBAAGIAEGKIEMggQABiJBRiiBEiIU1C3C1iWTXABeACQAQCYAWKgAe4OqgECMzC4AQPIAQD4AQGYAh-gAo0QqAIKwgITEC4YAxiPARjlAhjHAxjqAhiMA8ICEBAAGAMYjwEY5QIY6gIYjAPCAhAQLhgDGI8BGOUCGOoCGIwDwgIREC4YgAQYsQMYgwEYxwEY0QPCAg4QLhiABBixAxjHARjRA8ICCxAAGIAEGLEDGIMBwgILEC4YgAQYxwEY0QPCAgUQLhiABMICDhAAGIAEGIoFGLEDGIMBwgIFEAAYgATCAggQABiABBixA8ICFBAuGIAEGLEDGIMBGMcBGNEDGNQCwgIIEC4YgAQYsQPCAggQLhixAxiABMICBhAAGBYYHsICCxAAGIAEGIoFGIYDwgIFECEYoAHCAgUQIRifBZgDEZIHBDMwLjGgB-OHAQ&sclient=gws-wiz#fpstate=ive&ip=1&vld=cid:f2e341a9,vid:OklMg-H1yAM,st:0
params = (0.01,12,0)
pv1 = sp.optimize.fsolve(my_pv,x0 = -89, args=params)

print('pv:',pv)
print('pv1:',pv1)

#find internal rate of return of cashflows
irr = npf.irr([fv,pv])
print('internal rate of return:',irr)

#find number of periods one should invest 100$ to get 112.68$ at the end of last period, if annual interest rate is 12%
print('nper:',np.round(npf.nper(r,pv,fv),2))
