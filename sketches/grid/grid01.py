from random import randint

colormode(RGB, range = 255)
size(480, 640)

newmoon = [(119, 124, 133), (179, 185, 192), (242, 119, 122),
           (252, 163, 105), (255, 212, 121), (255, 238, 166),
           (146, 209, 146), (106, 176, 243), (118, 212, 214),
           (225, 166, 242), (172, 141, 88)]

simcode = [(92, 97, 130), (79, 164, 165), (202, 166, 122),
           (212, 117, 100)]

gridsize = 66
dia = gridsize - 8
for x, y in grid(7, 9, gridsize, gridsize):
    fill(color(newmoon[randint(0, len(newmoon) - 1)]))
    rect(10 + x, 10 + y, dia, dia)
    fill(color(simcode[randint(0, len(simcode) - 1)]))
    if randint(0, 100) < 50:
        oval(10 + x, 10 + y, dia, dia)
    else:
        star(10 + dia/2 + x, 10 + dia/2 + y, 6, 30, 10)