size(480, 480)
background(0.1, 0.1, 0.2)

data = "michdeuchtesisteinwiesel"

fill(1)
stroke(0.2)
strokewidth(1)
font("Zapfino")

for i in range(50):
    fontsize(random(200))
    rotate(random(360))
    x, y = random(WIDTH*0.5), random(HEIGHT*1.5)
    char = choice(data)
    p = textpath(char, x, y)
    drawpath(p)
