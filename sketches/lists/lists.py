size(480, 180)
background(0.1, 0.1, 0.2)
fill(1)
stroke(0.2)
strokewidth(1)
fontsize(16)

fruits = ["Apple", "Tomato", "Banana", "Orange", "Lemon"]
for i in range(len(fruits)):
    text(fruits[i], 25 + i*75, 25)

for i in range(len(fruits)):
    if fruits[i] == "Banana":
        a = i

fruits.pop(a)
for i in range(len(fruits)):
    text(fruits[i], 25 + i*75, 50)


del(fruits[fruits.index("Apple")])
for i in range(len(fruits)):
    text(fruits[i], 25 + i*75, 75)


fruits2 = [u"🍏", u"🍅", u"🍌", u"🍊", u"🍋"]
for i in range(len(fruits2)):
    text(fruits2[i], (i+1)*25, 100)

for i in range(len(fruits2)):
    if fruits2[i] == u"🍌":
        a = i

fruits2.pop(a)
for i in range(len(fruits2)):
    text(fruits2[i], (i+1)*25, 125)

del(fruits2[fruits2.index(u"🍏")])
for i in range(len(fruits2)):
    text(fruits2[i], (i+1)*25, 150)

