from nodebox.graphics import *
def draw(canvas):
    canvas.clear()
    translate(250, 250)
    rotate(canvas.frame)
    rect(x=-50, y=-50, width=100, height=100)
canvas.size = 500, 500
canvas.run(draw)