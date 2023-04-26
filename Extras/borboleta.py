import matplotlib.pyplot as plt
import numpy as np

def borboleta(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.power(np.sin(t/12), 5))
    y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.power(np.sin(t/12), 5))
    return x, y

t = np.linspace(0, 24*np.pi, 10000)
x, y = borboleta(t)

plt.plot(x, y)
plt.axis('equal')
plt.show()