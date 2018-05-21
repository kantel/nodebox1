coreimage = ximport("coreimage")

size(500, 500)

canvas = coreimage.canvas(WIDTH, HEIGHT)

def mandelbrot(x, y, depth = 64):
    z = complex(x, y)
    o = complex(0, 0)
    for i in range(depth):
        if abs(o) <= 2:
            o = o*o + z
        else:
            return(i)
    return(0)

pixels = []
w = WIDTH
h = HEIGHT

for i in range(w):
    for j in range(h):
        v = mandelbrot(float(i)/w, float(j)/h)
        pixels.append(color(v/10.0, v/20.0, v/10.0))

l = canvas.append(pixels, w, h)
# print(pixels)
canvas.draw()