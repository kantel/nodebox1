from math import sin, cos

size(640, 480)
stroke(0.2)

palette = [color(189/255.0, 183/255.0, 110/255.0),
           color(0.0, 100/255.0, 0.0),
           color(34/255.0, 139/255.0, 105/255.0),
           color(152/255.0, 251/255.0, 152/255.0),
           color(85/255.0, 107/255.0, 47/255.0),
           color(139/255.0, 69/255.0, 19/255.0),
           color(154/255.0, 205/255.0, 50/255.0),
           color(107/255.0, 142/255.0, 35/255.0),
           color(139/255.0, 134/255.0, 78/255.0),
           color(139/255.0, 115/255.0, 85/255.0)]

xmax = 600
xmitte = 300
ymax = 440

level = 12
# w1 = 0.36   # Winkel 1
# w2 = 0.48   # Winkel 2

w1 = w2 = 0.5

def drawPythagoras(a1, a2, b1, b2, level):
    if (level > 0):
        # Eckpunkte berechnen
        n1 = -b2 + a2
        n2 = -a1 + b1
        c1 = b1 + n1
        c2 = b2 + n2
        d1 = a1 + n1
        d2 = a2 + n2
        # Start-Rechteck zeichnen
        fill(palette[(level-1)%10])
        beginpath(a1 + xmitte, ymax - a2)
        lineto(b1 + xmitte, ymax - b2)
        lineto(c1 + xmitte, ymax - c2)
        lineto(d1 + xmitte, ymax - d2)
        endpath()
        e1 = d1 + w1*(c1 - d1) + w2*n1
        e2 = d2 + w1*(c2 - d2) + w2*n2
        # Schenkel-Quadrate zeichnen
        drawPythagoras(e1, e2, c1, c2, level-1)
        drawPythagoras(d1, d2, e1, e2, level-1)

drawPythagoras(-(xmax/10), 0, xmax/20, 0, level)

print("I did it, Babe!")

