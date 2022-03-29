size(600, 600)
grid = ximport("grid")
from random import shuffle

images = files("images/*.jpg")

g = grid.create(2, 2, WIDTH, HEIGHT)
g.top.left.split(2, 2)
g.top.left.bottom.right.split(2, 2)

shuffle(images)
g.content = images
g.content.repeat = True

g.styles.margin = 1
g.styles.fit = True
g.styles.align = "center", "bottom"

g.draw()