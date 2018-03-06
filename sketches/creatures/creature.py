from pvector import PVector

class Creature:
    
    def __init__(self, l, size = 4.0):
        self.location = l
        self.acceleration = PVector(0.0, 0.05)
        self.velocity = PVector(0, 0)
        self.size = size
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
    
    def display(self):
        stroke(0.0, 0.0, 0.0)
        fill(1.0, 0.0, 0.0)
        ellipse(self.location.x, self.location.y, self.size, self.size)
    
    def run(self):
        self.update()
        self.display()
        
        
