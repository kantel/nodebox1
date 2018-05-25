# Particles und Confetti
# Nach dem Processing (Java) Sketch von Daniel Shiffmann
# aus: The Nature of Code, o.O., 2012, Seite 166ff
# Dieses Mal mit externer Bibliothek

size(500, 500)
speed(30)
colormode(RGB)

from pvector import PVector
pt = ximport ("particle")


            
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
        particles.append(pt.Particle(loc))
    else:
        confetti.append(pt.Confetti(loc))
    for i in range(len(particles) - 1, 0, -1):
        particles[i].run()
        if particles[i].isDead():
            particles.pop(i)
            # print("Particels: ", len(particles))
    for i in range(len(confetti) -1 , 0, -1):
        confetti[i].run()
        confetti[i].theta += 0.7
        if confetti[i].theta >= 360:
            confetti[i].theta = 0.0
        if confetti[i].isDead():
            confetti.pop(i)
            # print("Konfetti: ", len(confetti))
