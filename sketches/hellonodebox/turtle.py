size(550, 400)
 
lsystem = ximport("lsystem")
tree = lsystem.create()
 
# We'll import the Colors library to do shadows
# and a nice gradient background.
colors = ximport("colors")
clr = colors.rgb(0.1, 0.095, 0.075)
p = rect(0, 0, WIDTH, HEIGHT, draw=False)
colors.gradientfill(p, clr, clr.lighten(0.25))
 
# Use the Supershape library to create an organic segment.
w = h = 65
supershape = ximport("supershape")
leaf = supershape.path(0, 0, w, h, 3, 0.22, 0.4, 0.4)
 
# What's the total amount of time we need to draw 8 generations?
# We can then divide the time for each segment by this number
# to get a value from 1.0 down to 0.0
generations = 8
# done = tree.duration(generations)
done = 5
 
# Here's our own segment function.
# We'll use the relative time to individually color segments
# (as time progresses we adjust the opacity).
def segment(length, generation, time, id):
    
    time /= done
    colors.shadow(dx=0, dy=-10-10*time, alpha=time*0.2)
    fill(0.9, 0.9, 0.9, 0.4*time)
 
    push()
    rotate(90)
    scale(time+0.3)
    drawpath(leaf.copy())
    pop()

tree.segmentlength = w - 15
tree.segment = segment
# tree.draw(275, 400, generations, time=done)

speed(20)
def draw():
    background(0.22, 0.21, 0.16)
    tree.draw(250, 400, generations, time = FRAME*0.05, ease=5)

