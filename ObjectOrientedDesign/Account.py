#import datetime as dt
import pandas as pd
#import numpy as np
import datetime

#today = pd.datetime.today()
#print (today - BDay(4))


class Account:

  def __init__(self, initialBalance,openDate=None,interestRate=0,accountId = 0):
      self.currentBalance = initialBalance
      self.initialBalance = initialBalance
      self.openDate = openDate
      self.credit = initialBalance
      self.interestRate = interestRate
      self.accountId = accountId
      #dictionary of deposits and withdrawals with corresponding dates
      self.d={}

      self.transactionDates = []
      #[pd.Timestamp('2012-05-01'), pd.Timestamp('2012-05-02'), pd.Timestamp('2012-05-03')]
      self.transactionAmounts =[]
      
      #self.ts=pd.Series(np.random.randn(3), dates)
      
  def balance(self):
      return self.currentBalance
      
  def transaction(self,amount, date):    
      #add date of transaction to self.transactionDates    
      #add amount  of transaction to self.transactionAmounts 
      #change current balance
      #
      
      pass
  '''          
  def deposit(self, amount,date):
      self.currentBalance +=  amount
      self.credit+=amount
      key=str(date.month)+str(date.year)
      if key in self.d.keys():
          self.d[key]=self.d[key].append((date,amount))
      else:  
          self.d[key]=[]
          self.d[key]=self.d[key].append((date,amount))
          
  def withdraw(self, amount,date):
      self.currentBalance -= amount  
      key=str(date.month)+str(date.year)
      if key in self.d.keys():
          self.d[key]=self.d[key].append((date,-amount))
      else:  
          self.d[key]=[]
          self.d[key]=self.d[key].append((date,-amount))
  '''    
  def availableCredit(self):
      if self.currentBalance<=0:
          if self.credit+self.currentBalance <=0:
               return 0
          else:
               return self.credit+self.currentBalance
      else:
          return self.credit
          
  def __str__(self):
       return  'account:'+ str(self.accountId) + '  balance = ' + str(self.currentBalance) 
       
  def __add__(self,other):
       return Account(self.currentBalance + other.currentBalance, accountId = 500)
       
  def __sub__(self,other):    
       return  Account(self.currentBalance - other.currentBalance, accountId = 0)
    
  def __divide__(self,other):    
      return  Account(self.currentBalance - other.currentBalance, accountId = 0)
  '''       
  def averageDailyBalance(self):
         #get today's date
         today = pd.datetime.today()
         #get previous month
         prev_month=today.month-1
         #sub_dates, sub_amount - get  values that correspond to previous month transactions from self.transactionDates and self.transactionAmounts
  '''
  #get balance at the specified date in the past 
  def balanceAt(date):
      pass
  '''       
  def averageDailyBalance(self):
         today = pd.datetime.today()
         #a-compute difference between balnces on end and begin periods
         bl=self.currentBalance+self.initialBalance
         #b-compute endPeriod-beginPeriod
         if pd.datetime.today()>self.openDate:
              t =  pd.datetime.today()-self.openDate
         return bl/int(t)
  '''
  def averageInterest(self,beginPeriod, endPeriod):
         #average daily rate = annualRate/360
         #return (average daily rate * average balance)
         return self.interestRate/360*self.averageDailyBalance()
     
  def interestAccrued(self):
      #compute interest accrued over previous month
      #algorithm:
      #compute daily average balnace P.
      #this computation should account for deposits and withdrawals
      #that happened during previous month. 
      #Then compute accrued interest as P*self.interestRate*30/360
      pass
  
  def set_history(self, filename):
       date1 = datetime.date(2021,10,10)
       self.d[date1] = 100    
    
x = Account(100,accountId = 234)
#filename = 'transactiondata.xls'
#x.set_history(filename)
print(x.balance())
ac = x.availableCredit()
'''
y = Account(200)

z = x - y
print(type(z))
print(x)
print(y)
print('z = ', z)
'''
