speed(30)
size(500, 500)
colormode(RGB, range = 255)



class Creature:
    
    def __init__(self, x, y, speed, size = 4, c = color(220, 0, 0)):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = c
        
        self.dx = 0
        self.dy = 0
    
    def move(self):
        v = self.speed
        self.dx = random(-v, v)
        self.dy = random(-v, v)
        
        self.dx = max(-v, min(self.dx, v))
        self.dy = max(-v, min(self.dy, v))
        
        self.x += self.dx
        self.y += self.dy
        
        # Checking Boundaries
        if self.x > WIDTH:
            self.x = self.dx
        elif self.x < 0:
            self.x = WIDTH - self.dx
        if self.y > HEIGHT:
            self.y = self.dy
        elif self.y < 0:
            self.y = HEIGHT - self.dy
    
    def display(self):
        fill(self.color)
        oval(self.x, self.y, self.size, self.size)
        

ants1 = []
ants2 = []

def setup():
    for i in range(25):
        ants1.append(Creature(random(20, WIDTH-20), random(20, HEIGHT-20),
                              speed = random(2.5, 3.5)))
    for j in range(10):
        ants2.append(Creature(random(80, WIDTH-80), random(80, HEIGHT-80),
                              speed = random(0.3, 0.7), 
                              size = 8, c = color(0, 180, 0)))


def draw():
    background("#1f2838")
    for ant in ants1:
        ant.move()
        ant.display()
    for ant in ants2:
        ant.move()
        ant.display()
