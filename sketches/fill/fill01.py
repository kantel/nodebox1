size(360, 360)
margin = 20
background(0)
for x in range(20):
    x *= 16
    for y in range(0,20):
        y *= 16
        image("macpaint/28.gif", x, y)
        