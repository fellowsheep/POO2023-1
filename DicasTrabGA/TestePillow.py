import tkinter as tk
from PIL import ImageTk, Image

# Abre a imagem
imagem = Image.open('python_icon.png')
fator_escala = 3.0

# Calcula as novas dimensões da imagem
largura, altura = imagem.size
nova_largura = int(largura * fator_escala)
nova_altura = int(altura * fator_escala)

imagem = imagem.resize((nova_largura, nova_altura))

# Cria a janela
janela = tk.Tk()

# Define o título da janela
janela.title('Testando as bibliotecas Pillow e Tk')


# Define as dimensões da janela
largura_janela = 800
altura_janela = 600
janela.geometry('{}x{}'.format(largura_janela, altura_janela))

# Calcula as coordenadas para centralizar a imagem
largura_imagem, altura_imagem = imagem.size
x = (largura_janela - largura_imagem) // 2
y = (altura_janela - altura_imagem) // 2


# Cria o objeto PhotoImage
photo = ImageTk.PhotoImage(imagem)

# Cria o widget de imagem e adiciona à janela
label = tk.Label(janela, text="", image=photo)
label.place(x=x, y=y)

# Exibe a janela
janela.mainloop()