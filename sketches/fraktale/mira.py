# Mira-Abbildung

size(600, 600)
colormode(HSB, range = 255)

# Parameter
# a = 0.4
# b = 1.0
a = -0.48
b = 0.93


def mira(x):
    return (a*x - (1.0 - a)*(2.0*(x*x)/(1.0 + x*x)))

x = 4.0
y = 0.0

fill(0)
rect(0, 0, WIDTH, HEIGHT)

for i in range(25000):
    x1 = b*y + mira(x)
    y = -x + mira(x1)
    x = x1
    fill(i%255, 255, 255)
    oval(350 + (x*30.0), 310 - (y*30.0), 2, 2)

print("I did it, Babe!")