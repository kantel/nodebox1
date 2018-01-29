import math

size(500, 500)
colormode(RGB, range = 255)

# Konstanten
a = 1.5732
# a = 1.35
h = 0.02
max = 10.0e+9

x0 = 0.01
y0 = -0.02
cosa = math.cos(a)
sina = math.sin(a)

fill(20)
rect(0, 0, WIDTH, HEIGHT)
x = x0
y = y0
for j in range(50):
    for i in range(1500):
        if (x < max) and (y < max):
            x1 = x*cosa - (y - x*x)*sina
            y = x*sina + (y - x*x)*cosa
            x = x1
            p = (x + 1.25)*180
            q = (1.4 - y)*180
            if (i < 250):
                fill(183, 116, 64)
            elif (i < 500):
                fill(17, 42, 106)
            elif (i < 750):
                fill(159, 53, 233)
            elif (i < 1000):
                fill(57, 218, 56)
            elif (i < 1250):
                fill(67, 254, 211)
            else:
                fill(212, 251, 69)
            oval(p, q, 2, 2)
    x = x0 + j*h
    y = y0 + j*h

fill(255)
fontsize(14)
msg = "Quadratische Henon-Gleichung für a = {}".format(a)
text(msg, 20, WIDTH - 20)