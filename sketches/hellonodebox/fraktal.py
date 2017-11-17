coreimage = ximport("coreimage")
canvas = coreimage.canvas(150, 150)

def fractal(x, y, depth=64):
    z = complex(x, y)
    o = complex(0, 0)
    for i in range(depth):
        if abs(o) <= 2: o = o*o + z
        else: 
            return i
    return 0 #default, black
 
pixels = []
w = h = 150
for i in range(w):
    for j in range(h):
        v = fractal(float(i)/w, float(j)/h)
        pixels.append(color(v/10.0, v/20.0, v/10.0))
 
l = canvas.append(pixels, w, h)


c = coreimage.canvas(150, 150)
l = c.append(canvas)


c.draw()