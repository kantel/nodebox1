# Particles und Confetti
# Nach dem Processing (Java) Sketch von Daniel Shiffmann
# aus: The Nature of Code, o.O., 2012, Seite 166ff

size(500, 500)
speed(30)
colormode(RGB)

from pvector import PVector

#---------------------Klassendefinitionen ------------------------

class Particle(object):
    
    def __init__(self, l):
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(random(-1.5, 1.5), random(-2.0, 2.0))
        self.location = l.get()
        self.lifespan = 255
    
    def run(self):
        self.update()
        self.display()
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= 2
    
    def display(self):
        colorrange(255)
        stroke(0, 0, 0)
        fill(255, 140, 0, self.lifespan)
        ellipse(self.location.x, self.location.y, 20, 20)
        
    def isDead(self):
        if self.lifespan <= 0:
            return True
        else:
            return False

class Confetti(Particle):
    
    def __init__(self, l):
        Particle.__init__(self, l)
        self.velocity = PVector(random(-2.5, 2.5), random(-2.0, 2.0))
        self.theta = 0.0
    
    def display(self):
        colorrange(255)
        stroke(0, 0, 0)
        fill(124, 252, 0, self.lifespan)
        rotate(self.theta)
        rect(self.location.x, self.location.y, 20, 20)


#----------------------------------------------------------------------            
            
particles = []
confetti  = []

def setup():
    global loc
    loc = PVector(WIDTH/2, 50)

def draw():
    global loc
    background("#1f2838")
    r = random()
    if r < 0.5:
        particles.append(Particle(loc))
    else:
        confetti.append(Confetti(loc))
    for i in range(len(particles) - 1, 0, -1):
        particles[i].run()
        if particles[i].isDead():
            particles.pop(i)
    for i in range(len(confetti) -1 , 0, -1):
        confetti[i].run()
        confetti[i].theta += 0.7
        if confetti[i].theta >= 360:
            confetti[i].theta = 0.0
        if confetti[i].isDead():
            confetti.pop(i)
