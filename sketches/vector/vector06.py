import math
size(540, 320)
speed(60)

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
        
location = PVector(100, 100)
velocity = PVector(1.0, 3.3)
    
def draw():
    fill(1.0)
    rect(0, 0, WIDTH, HEIGHT)
    
    mouse = PVector(MOUSEX, MOUSEY)
    center = PVector(WIDTH/2, HEIGHT/2)
    
    mouse.sub(center)
    
    mouse.normalize()
    mouse.mult(150)
    
    nofill()
    stroke(0)
    translate(WIDTH/2, HEIGHT/2)
    line(0, 0, mouse.x, mouse.y)
