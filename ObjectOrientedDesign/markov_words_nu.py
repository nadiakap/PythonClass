import random
import numpy as np
class MarkovText:
    def __init__(self, k, text):
            self.d={}
            self.k=k
            self.text=text
            for i in range(len(self.text)-self.k):
                key=str(text[i:i+self.k])
                if key not in self.d.keys():
                    self.d[key]=[]
                    self.d[key].append(self.text[i+self.k])  
                else:
                    self.d[key].append(self.text[i+self.k])
            print(self.d)
                
    def frequency(self, k, text):
            self.stats={}
            self.text=text
            for i in range(  len(self.text)-k  ):
                key=str(text[i:i+k])

                if key not in self.stats.keys():
                    self.stats[key]=1     
                else:
                   self.stats[key]=self.stats[key]+1
                   
            return  self.stats
        
    def get_d(self) :  
        return self.__d
                
    def maketext(self, s):
            given_string=self.text[0:self.k]
            temp_string = given_string
            new_text=given_string
            for i in range(s):
                if temp_string not in self.__d.keys():
                    #cannot make prediction, guessing letter 'a'
                    guess='e'
                else:
                    guess=sample(self.__d,temp_string)
                    temp_string = temp_string[1:]+guess
                          
                new_text+=guess    
        
            return new_text
        

def sample(d, s):               
                lst=d[s]
                total=len(lst)
                return lst[random.randint(0,total-1)]
'''
def sample2(d, s):
            elements = ['m', 't', 'g','e','l']
            probabilities = [4/13, 2/13,5/13,1/13,1/13]
            
            np.random.choice(elements, 10, p=probabilities)   
            lst=d[s]
            total=len(lst)
            return lst[random.randint(0,total-1)]
'''        
def deleteSymbolsFromText(text,symbols):
     #removing spaces between words
     text_tmp=text
     for s in symbols:
        l_text=text_tmp.split(s)
        text_tmp=''.join(l_text)
     return text_tmp
    
if __name__ == '__main__':
    """
    Below is some sample code that uses the MarkovText class to generate some
    text from a text file.
    """
    #scaramouche = open('./scaramouche.txt', 'r')
    scaramouche = open('scaramouche1.txt', 'r')
    text = scaramouche.read()
   
    #text='Below is some sample code that uses the MarkovText'

    #text=deleteSymbolsFromText(text_0,['/',' ',',','.'])
    M = MarkovText(3, text)
    
    #print(M.k)
    #print(M.get_d())
    
    #print(M.maketext(100))
    #print(M.frequency(3,text))
    



            