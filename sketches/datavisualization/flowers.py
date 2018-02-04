size(480, 480)
background("#1f2838")

def flower(x, y):
    clr = color(random(0.5, 1), random(0.5), random(0.5))
    fill(clr)
    stroke(0.6)
    strokewidth(1)
    
    transform(CORNER)
    translate(x, y)
    r = random(10) + 5
    for i in range(10):
        rotate(36)
        line(0, 0, 15, 15)
        oval(10, 10, r, r)
    reset()
    
for i in range(60):
    flower(random(WIDTH), random(HEIGHT))