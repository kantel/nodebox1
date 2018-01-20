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
        
location = PVector(100, 100)
velocity = PVector(1.0, 3.3)

     
def draw():
    fill(1.0)
    rect(0, 0, WIDTH, HEIGHT)
    
    mouse = PVector(MOUSEX, MOUSEY)
    center = PVector(WIDTH/2, HEIGHT/2)
    
    mouse.sub(center)
    nofill()
    stroke(0)
    translate(WIDTH/2, HEIGHT/2)
    line(0, 0, mouse.x, mouse.y)
    
