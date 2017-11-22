lsys = ximport("lsys")

background(0.3, 0.3, 0.3)
strokewidth( 1.0 )
stroke( 0 )
# nofill()
fill(1.0, 1.0, 0.1)

axiom = "F++F++F"
rules = {"F": "F-F++F-F"}
angle = 60
linelength = 2
depth = 5


s = lsys.LindenmayerSystem(axiom, rules, angle, angle, -angle,
                           linelength, depth)
s.drawlsystem(inset = 20)