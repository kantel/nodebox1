coreimage = ximport("coreimage")

size(300, 300)

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
left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5

for i in range(w):
    cr = left + i*(right - left)/w
    for j in range(h):
        ci = bottom + j*(top - bottom)/h
        v = mandelbrot(cr, ci)
        pixels.append(color(v/10.0, v/20.0, v/10.0))

l = canvas.append(pixels, w, h)
# print(pixels)
canvas.draw()