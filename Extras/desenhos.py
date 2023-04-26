import numpy as np
import matplotlib.pyplot as plt

# Função paramétrica para desenhar um coração
def heart_parametric(t):
    x = 16*np.sin(t)**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    return x, y

# Função paramétrica para desenhar uma borboleta
def butterfly_parametric(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin((t/12) - np.pi)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin((t/12) - np.pi)**5)
    return x, y

# Função paramétrica para desenhar a curva do Batman
def batman_parametric(t):
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    
    for i, ti in enumerate(t):
        x[i] = np.sin(ti) * (np.abs(np.cos(ti))**0.5 / ((np.abs(ti) + 0.1)*(1.1 - np.abs(ti)))) + 0.5*np.cos(ti)*np.sign(np.sin(ti))
        y[i] = (np.abs(ti)**0.1) * (4 - 3.8 * np.sin(4*ti) - 0.85 * np.cos(6*ti) - 0.45 * np.sin(10*ti) + 0.5 * np.sin(28*ti))
        
    return x, y

# Cria uma figura com três subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Define os valores de t para cada curva
t_heart = np.linspace(0, 2*np.pi, 1000)
t_butterfly = np.linspace(0, 2*np.pi, 1000)
t_batman = np.linspace(-7*np.pi/4, 7*np.pi/4, 1000)

# Desenha a curva do coração no primeiro subplot
x_heart, y_heart = heart_parametric(t_heart)
axs[0].plot(x_heart, y_heart, color='red')
axs[0].set_title('Coração')

# Desenha a curva da borboleta no segundo subplot
x_butterfly, y_butterfly = butterfly_parametric(t_butterfly)
axs[1].plot(x_butterfly, y_butterfly, color='green')
axs[1].set_title('Borboleta')

# Desenha a curva do Batman no terceiro subplot
x_batman, y_batman = batman_parametric(t_batman)
axs[2].plot(x_batman, y_batman, color='blue')
axs[2].set_title('Batman')

# Mostra o gráfico resultante
plt.show()
