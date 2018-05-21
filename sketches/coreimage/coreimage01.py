coreimage = ximport("coreimage")
size(150, 150)

canvas = coreimage.canvas(WIDTH, HEIGHT)

l = canvas.append("leaf.jpg")
l = canvas.append("lily.tif")
canvas.draw()
