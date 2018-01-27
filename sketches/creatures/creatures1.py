size(600, 600)

class Creature:
    
    def __init__(self, x, y, speed = 1.0, size = 4.0):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        
        self._vx = 0
        self._vy = 0
        
    def wandering(self):
        v = self.speed
        self._vx += random(-v, v)
        self._vy += random(-v, v)
        
        self._vx = max(-v, min(self._vx, v))
        self._vy = max(-v, min(self._vy, v))
        
        self.x += self._vx
        # checking boundaries
        if self.x > WIDTH:
            self.x = self._vx
        elif self.x < 0:
            self.x = WIDTH - self._vx
        self.y += self._vy
        # checking boundaries
        if self.y > HEIGHT:
            self.y = self._vy
        elif self.y < 0:
            self.y = WIDTH - self._vy

ants1 = []
ants2 = []

def setup():
    for i in range(25):
        ants1.append (Creature(WIDTH/2, HEIGHT/2, speed = random(1.5, 2.5)))
    for j in range(10):
        ants2.append (Creature(WIDTH/2, HEIGHT/2, speed = random(0.3, 0.7), size = 8.0))
    
speed(30)

def draw():
    fill(0.2)
    rect(0, 0, WIDTH, HEIGHT)
    
    fill(0, 0.9, 0)
    for ant in ants1:
        ant.wandering()
        oval(ant.x, ant.y, ant.size, ant.size)
    
    fill(0.7, 0, 0)
    for ant in ants2:
        ant.wandering()
        oval(ant.x, ant.y, ant.size, ant.size)
        