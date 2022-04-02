tt = "Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich."

size(500, 500)
margin = 10

fill(30.0/255)
rect(margin, margin, WIDTH - 2*margin, HEIGHT - 2*margin) 

fill(127.0/255, 199.0/255, 175.0/255)
font("Comic Helvetic Heavy", 58)
text("Comic Helvetic", 40, 100)
fill(237.0/255, 118.0/255, 112.0/255)
font("Comic Helvetic Medium", 44)
text(tt, 40, 180, width = 450)
text("🤡", 40, 420)