# Color
size(500, 500)

for i in range(HEIGHT/2):
    c = color(random(), random(), random())
    stroke(c)
    strokewidth(1)
    line(0, i, WIDTH, i)

for i in range(HEIGHT/2 + 1, HEIGHT):
    c = color(random(), random(), random())
    c.saturation = 1.0
    # c.brightness = 1.0
    stroke(c)
    strokewidth(2)
    line(0, i, WIDTH, i)

    