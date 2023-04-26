import numpy as np
import matplotlib.pyplot as plt

def draw_batman():
    # Primeira equação
    x = np.linspace(-8, 8, 1000)
    y1 = 1.5*np.sqrt(-np.abs(np.abs(x)-1)*np.abs(3-np.abs(x))/((np.abs(x)-1)*(3-np.abs(x)))) * \
         (1+np.abs(np.abs(x)-3)/(np.abs(x)-3))*np.sqrt(1-np.power(x/7,2)) + \
         (4.5+0.75*(np.abs(x-0.5)+np.abs(x+0.5))-2.75*(np.abs(x-0.75)+np.abs(x+0.75))) * \
         (1+np.abs(1-np.abs(x))/(1-np.abs(x)))
    
    # Segunda equação
    y2 = -3*np.sqrt(1-np.power(x/7,2))*np.sqrt(np.abs(np.abs(x)-4)/(np.abs(x)-4))
    
    # Terceira equação
    y3 = np.abs(x/2)-0.0913722*(x*x)-3+np.sqrt(1-np.power((np.abs(np.abs(x)-2)-1),2))
    
    # Quarta equação
    y4 = (2.71052+(1.5-0.5*np.abs(x))-1.35526*np.sqrt(4-np.power(np.abs(x)-1,2))*np.sqrt(np.abs(np.abs(x)-1)/(np.abs(x)-1)))
    
    # Plotagem das curvas
    plt.plot(x, y1, 'b')
    plt.plot(x, y2, 'b')
    plt.plot(x, y3, 'b')
    plt.plot(x, y4, 'b')
    
    plt.xlim(-8, 8)
    plt.ylim(-4, 4)
    plt.axis('off')
    plt.show()

draw_batman()
