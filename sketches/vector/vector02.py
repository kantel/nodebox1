size(540, 320)
speed(60)

class PVector():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, v):
        self.x += v.x
        self.y += v.y

location = PVector(100, 100)
velocity = PVector(1.0, 3.3)

#def setup():
#    pass

     
def draw():
    fill(1.0)
    rect(0, 0, WIDTH, HEIGHT)
    
    location.add(velocity)
    
    # Check for bouncing
    if (location.x > WIDTH - 16) or (location.x < 0):
        velocity.x *= -1
    if (location.y > HEIGHT -16) or (location.y < 0):
        velocity.y *= -1
    
    stroke(0)
    fill(1.0, 0, 0)
    oval(location.x, location.y, 16, 16)

