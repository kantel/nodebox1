coreimage = ximport("coreimage")

size(600, 600)
canvasw, canvash = 550, 550
canvas = coreimage.canvas(canvasw, canvash)

left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5

def mandel(x, y, depth=64):
    c = complex(x, y)
    z = complex(0, 0)
    for i in range(depth):
        if abs(z) <= 2:
            z = z*z + c
        else:
            return i
    return 0                           # Default, Schwarz

pixels = []
w, h = canvasw, canvash
offset = 25
for i in range(h):
    ci = bottom + i*(top - bottom)/h   # Imaginärteil
    for j in range(w):
        cr = left + j*(right - left)/w # Realteil
        v = mandel(cr, ci)
        pixels.append(color(v/5.0, v/20.0, v/40.0))

l = canvas.append(pixels, w, h)
canvas.draw(offset, offset)

print("I did it, Babe!")