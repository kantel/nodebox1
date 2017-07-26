size(600, 320)
speed(30)

def setup():
    global xboy, xcat, xhorn, xpink
    xboy = xpink = -100
    xcat = xhorn = WIDTH - 10

def draw():
    global xboy, xcat, xhorn, xpink
    
    fill(0, 0.25, 0.25)
    rect(0, 0, WIDTH, HEIGHT)
    
    image("images/boy.png", xboy, 40)
    image("images/catgirl.png", xcat, -40)
    image("images/horngirl.png", xhorn, 120)
    image("images/pinkgirl.png", xpink, 200)
    xboy += 4
    xcat -= 3
    xhorn -= 5
    xpink += 3
    if xboy > WIDTH + 10:
        xboy = -50
    if xcat < -101:
        xcat = WIDTH + 10
    if xhorn < -101:
        xhorn = WIDTH + 10
    if xpink > WIDTH + 10:
        xpink = -100