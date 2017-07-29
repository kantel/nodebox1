from math import cos, sin, radians
d = 8.0
n = 5.0
k = n/d

size(400, 400)
fill(0, 0.25, 0.25)
rect(0, 0, WIDTH, HEIGHT)

nofill()

a = 0
while (a < 100): #TWO_PI
    stroke(0.5, 1, 0)
    strokewidth(0.5)
    beginpath()
    moveto(WIDTH/2, HEIGHT/2)
    r = 200*cos(radians(k*a))
    x = r*cos(radians(a))
    y = r*sin(radians(a))
    print(x, y)
    lineto(x, y)
    a += 0.02
    endpath()
