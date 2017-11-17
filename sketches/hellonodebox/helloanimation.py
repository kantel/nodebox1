size(480, 200)
speed(30)

def setup():
    global x, y, dir
    x = WIDTH/2 + 16
    y = HEIGHT/2 - 16
    dir = -2

def draw():
    global x, y, dir
    background(0.0, 0.9, 0.3)
    image("assets/hildegrund.gif", x, y)
    x += dir
    if x > WIDTH-32:
        x = WIDTH - 32
        dir *= -1
    if x <= 0:
        x = 0
        dir *= -1