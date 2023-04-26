import tkinter as tk
from PIL import ImageTk, Image

# Abre a imagem
imagem = Image.open('Python-logo.png')

# Cria a janela
janela = tk.Tk()

# Cria o objeto PhotoImage
photo = ImageTk.PhotoImage(imagem)

# Cria o widget de imagem e adiciona à janela
label = tk.Label(janela, text="", image=photo)
label.pack()

# Exibe a janela
janela.mainloop()