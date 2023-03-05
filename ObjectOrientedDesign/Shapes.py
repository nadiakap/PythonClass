import math

class Circle:
    
    def setRadius(self, r):
           self.r = r
           self.area = math.pi * self.r * self.r

class Square:
    
    def __init__(self, s):
          self.side = s
          self.area = self.side * self.side
             
    def setSide(self, side):
           self.side = side
           self.area = self.side * self.side
           
    def getSide(self):
           return self.side
       
    def getArea (self):
          return self.side * self.side
    
    def setArea (self, area):
          self.side = area**0.5
          self.area = area
     
    def __str__(self):
          return "Square with side " + str(self.side)
    
    def __add__(self,y):
          return Square(self.getArea() + y.getArea())
    
    def __sub__(self,y):
            return Square(self.getArea() - y.getArea())

if __name__=='__main__':   
    
    #create circle with radius 1
    c = Circle()
    c.setRadius(1)
    
    #print the circle
    print(c)
    
    #create two squares and some them up
    y = Square(5)
    y.setSide(2)
    print('square y:', y)
    z = Square(5)
    print('square z:', z)
    x = y + z
    
    #subtract squares
    print('square x:', x)
    x1 = y - z
