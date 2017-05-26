str = open("assets/boxer.txt").read()
fill(0.2)
rect(0, 0, WIDTH, HEIGHT)

fill(1)
font("Palatino", 24)
text("Seltsame Zeichen", 20, 30)

font("Palatino", 16)
lineheight(1.4)
text(str, 20, 60, width=400)