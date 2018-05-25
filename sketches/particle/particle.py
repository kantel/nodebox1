# coding=utf-8
from pvector import PVector
from random import uniform

class Particle(object):
    
    def __init__(self, l):
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(uniform(-1.5, 1.5), uniform(-2.0, 2.0))
        # self.velocity = PVector(_ctx.random(-1.5, 1.5), _ctx.random(-2.0, 2.0))
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
        _ctx.colorrange(255)
        _ctx.stroke(0, 0, 0)
        _ctx.fill(255, 140, 0, self.lifespan)
        _ctx.ellipse(self.location.x, self.location.y, 20, 20)
        
    def isDead(self):
        if self.lifespan <= 0:
            return True
        else:
            return False

class Confetti(Particle):
    
    def __init__(self, l):
        Particle.__init__(self, l)
        self.velocity = PVector(uniform(-2.5, 2.5), uniform(-2.0, 2.0))
        # self.velocity = PVector(_ctx.random(-2.5, 2.5), _ctx.random(-2.0, 2.0))
        self.theta = 0.0
    
    def display(self):
        _ctx.colorrange(255)
        _ctx.stroke(0, 0, 0)
        _ctx.fill(124, 252, 0, self.lifespan)
        _ctx.rotate(self.theta)
        _ctx.rect(self.location.x, self.location.y, 20, 20)
