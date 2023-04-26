import matplotlib.pyplot as plt
import numpy as np

def coracao(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

t = np.linspace(0, 2 * np.pi, 2000)
x, y = coracao(t)

plt.plot(x, y)
plt.axis('equal')
plt.show()
