coreimage = ximport("coreimage")

size(400, 400)
canvas = coreimage.canvas(300, 300)

def fractal(x, y, depth=64):
    z = complex(x, y)
    o = complex(0, 0)
    for i in range(depth):
        if abs(o) <= 2: o = o*o + z
        else:
            return i
    return 0 #default, black

pixels = []
w, h = WIDTH, HEIGHT
offset = 50
for i in range(w):
    for j in range(h):
        v = fractal(float(i)/w, float(j)/h)
        pixels.append(color(v/5.0, v/20.0, v/50.0))

l = canvas.append(pixels, w, h)
canvas.draw(offset, offset)

print("I did it, Babe!")