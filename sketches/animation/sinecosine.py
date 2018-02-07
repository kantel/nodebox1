# Sinus und Cosinus
import math

size(500, 400)
speed(30)
background(1)
colormode(HSB)


def setup():
    global a, b, co
    a = 0
    b = 0
    co = 0

def draw():
    global a, b, co
    
    x0 = math.sin(a)*(WIDTH-20)/2
    y0 = math.cos(a)*(HEIGHT-20)/2
    x1 = math.sin(b)*(WIDTH-20)/2
    y1 = math.cos(b)*(HEIGHT-20)/2
    
    translate(WIDTH/2, HEIGHT/2)
    strokewidth(10)
    stroke(co)
    line(x0, y0, x1, y1)
    
    a += 0.02
    b += 0.05
    co += 00.1
    if co > 1:
        co = 0
    