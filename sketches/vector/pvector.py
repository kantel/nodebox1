import math

class PVector():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, v):
        self.x += v.x
        self.y += v.y
        
    def sub(self, v):
        self.x -= v.x
        self.y -= v.y
    
    # Multiplikation mit einem Skalar
    def mult(self, n):
        self.x *= n
        self.y *= n
    
    # Division durch einen Skalar
    def div(self, n):
        self.x /= n
        self.y /= n
    
    # Magnitude
    def mag(self):
        return(math.sqrt(self.x*self.x + self.y*self.y))
    
    # Normalisierung
    def normalize(self):
        m = self.mag()
        if (m != 0):
            self.div(m)
