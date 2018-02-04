size(480, 480)
background(0.1, 0.1, 0.2)

data = "michdeuchtesisteinwiesel"
# data = u"当時の通常作品の7倍ほどに匹敵する製作費をかけ"

fill(1)
stroke(0.2)
strokewidth(1)

for i in range(50):
    font("Zapfino", random(200))
    # font("HanziPen TC", random(200))
    rotate(random(360))
    x, y = random(WIDTH*0.5), random(HEIGHT*1.5)
    char = choice(data)
    p = textpath(char, x, y)
    drawpath(p)
