from random import randint

colormode(RGB, range = 255)

a1 = 150
newmoon = [(119, 124, 133, a1), (179, 185, 192, a1), (242, 119, 122, a1),
           (252, 163, 105, a1), (255, 212, 121, a1), (255, 238, 166, a1),
           (146, 209, 146, a1), (106, 176, 243, a1), (118, 212, 214, a1),
           (225, 166, 242, a1), (172, 141, 88, a1)]

a2 = 200
simcode = [(92, 97, 130, a2), (79, 164, 165, a2), (202, 166, 122, a2),
           (212, 117, 100, a2)]

WIDTH  = 800
HEIGHT = 800
size(WIDTH, HEIGHT)

strokewidth(10)
background(30, 30, 30)
for _ in range(15):
    dia =  randint(50, 200)
    margin = dia + 25
    x, y = randint(margin, WIDTH - margin), randint(margin, HEIGHT - margin)
    s = color(simcode[randint(0, len(simcode) - 1)])
    c = color(newmoon[randint(0, len(newmoon) - 1)])
    stroke(s)
    fill(c)
    circle(x, y, dia) 
