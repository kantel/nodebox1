# Particle-System
from pvector import PVector
size(560, 480)
speed(50)
colormode(RGB, range=255)
background("#1f2838")

class Particle(object):
    
    def __init__(self, l):
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(random(-1.0, 1.0), random(-2.0, 0.0))
        self.location = l.get()
        self.lifespan = 1.0
    
    def run(self):
        self.update()
        self.display()
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= random(0.0075, 0.009)
        # self.lifespan -= 0.008
    
    def display(self):
        stroke(color(0, 0, 0, 1))
        fill(color(255, 0, 0, self.lifespan))
        oval(self.location.x, self.location.y, 20, 20)
        
    def isDead(self):
        if self.lifespan <= 0:
            return True
        else:
            return False


particles = []

def setup():
    global loc
    loc = PVector(WIDTH/2, 50)

def draw():
    global loc
    fill(0.2, 0.2, 0.2)
    rect(0, 0, WIDTH, HEIGHT)
    particles.append(Particle(loc))
    for i in range(len(particles) - 1, 0, -1):
        particles[i].run()
        if particles[i].isDead():
            particles.pop(i)
            print(len(particles))