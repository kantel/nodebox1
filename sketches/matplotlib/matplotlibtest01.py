import numpy as np
import matplotlib.pyplot as plt

# clear previous plots
# pyplots overlap between runs. If that's a desired feature, comment the following two lines.
plt.cla()
plt.clf()

x = np.linspace(-10, 10, 1000)

plt.plot(x, np.sin(x), "-r", label = "Sinus")
plt.plot(x, np.cos(x), "--g", label = "Cosinus")
plt.xticks([-10, 0, 10])
plt.yticks([-1, 0, 1])
plt.ylim(-2, 2)
plt.legend()
plt.grid()

# save the plot and load it as an image...
plt.savefig("sincos.svg", dpi = 300) # SVG für die Darstellung im Browser
plt.savefig("sincos.png", dpi = 150) # PNG für die Darstellung in Nodebox
image("sincos.png", 0, 0)