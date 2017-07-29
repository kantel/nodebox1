from math import sin, radians

size(500, 500)
speed(30)

def setup():
    global frame
    frame = 1

def draw():
    global frame
    frame += 1
    
    fill(0, 0.25, 0.25)
    rect(0, 0, WIDTH, HEIGHT)
    
    for i in range(30):
        nofill()
        stroke(0.5, 1, 0)
        strokewidth(1)
        
        rotate(12)
        
        v = sin(radians(frame))*i*20
        autoclosepath(False)
        beginpath(WIDTH/2, HEIGHT/2)
        curveto(v, -v, v, v, 400, 400)
        endpath()