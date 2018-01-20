size(540, 320)
speed(60)
x, y = 100, 100
xspeed = 1
yspeed = 3.3

#def setup():
#    pass

     
def draw():
    global x, y, xspeed, yspeed
    fill(1.0)
    rect(0, 0, WIDTH, HEIGHT)

    
    x += xspeed
    y += yspeed
    
    # Check for bouncing
    if (x > WIDTH - 16) or (x < 0):
        xspeed *= -1
    if (y > HEIGHT -16) or (y < 0):
        yspeed *= -1
    
    stroke(0)
    fill(1.0, 0, 0)
    oval(x, y, 16, 16)