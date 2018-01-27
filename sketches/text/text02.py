size(322, 603)

frog_j = open("froschjap.txt").read()
frog_d = open("froschd.txt").read()

fill(0.2)
rect(0, 0, WIDTH, HEIGHT)

image("frog.jpg", 0, 0, 322, 603)

fill("#5c2018")
font("Garamond-Bold", 32)
text("Frosch-Haiku", 20, 80)

font("Hiragino Kaku Gothic Pro", 14)
text(frog_j, 20, 130)

font("Garamond-Bold", 14)
lineheight(1.6)
text(frog_d, 110, 116)