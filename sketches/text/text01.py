str = open("davis.txt").read()

fill(0.2)
rect(0, 0, WIDTH, HEIGHT)

fill(1)
font("Garamond-Bold", 32)
text("Angela Davis", 20, 30)

font("Garamond", 22)
lineheight(1.4)
text(str, 20, 70, width = 460)

font("Garamond-Italic")
text("(Wikipedia)", 20, 420)