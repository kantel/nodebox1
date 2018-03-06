# Creature 2
from pvector import PVector
from creature import Creature
size(500, 500)
speed(30)
colormode(RGB, range=255)
background("#1f2838")


ants1 = []
ants2 = []

def setup():
    loc = PVector(WIDTH/2, HEIGHT/2)
    for ant1 in range(2):
        ants1.append(Creature(loc))
    for ant2 in range(1):
        ants2.append(Creature(loc, size = 8.0))
    
speed(30)

def draw():
    print(ants1[0].acceleration.x, ants1[0].acceleration.y)