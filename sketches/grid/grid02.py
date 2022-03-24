from random import randint

colormode(RGB, range = 255)
size(475, 610)

simcode2 = [(92,97,130), (79,164,165), (202,166,122), (212,117,100)]

molnar = [(160, 60, 235), (200, 5, 20), (55, 188, 25), (15, 35, 250),
          (125, 235, 250),(240, 245, 15)]

gridsize = 66
dia = gridsize - 8
background(30, 30, 30)
for x, y in grid(7, 9, gridsize, gridsize):
    fill(color(molnar[randint(0, len(molnar) - 1)]))
    rect(10 + x, 10 + y, dia, dia)
    fill(color(simcode2[randint(0, len(simcode2) - 1)]))
    if randint(0, 100) < 50:
        oval(10 + x, 10 + y, dia, dia)
    else:
        star(10 + dia/2 + x, 10 + dia/2 + y, 6, 30, 10)