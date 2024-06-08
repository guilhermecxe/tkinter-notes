import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
# Usando uma lista para configurar duas linhas ao mesmo tempo do grid
window.rowconfigure([0, 1], minsize=100)

'''
Um elemento dentro de um grid é sempre posicionado ao centro,
mas existem outras formas de posicionar:
"n" ou "N": centro superior
"e" ou "E": centro à direita
"s" ou "S": centro inferior
"w" ou "W": centro à esquerda

Mas ainda é possível combinar as letras
"ne": direita superior
"sw": esquerda inferior
...

Além disso é possível fazer com que o elemento de uma célula
ocupe mais do seu disponível.
"ns": o elemento ocupado de cima a baixo da sua célula do grid
"we": o elemento ocupado da esqueda à direit da sua célula do grid
"nsew": O elemento ocupa seu espaço em todas as direções
'''

label1 = tk.Label(text='A', bg='yellow')
label1.grid(row=0, column=0, sticky='ew')

label2 = tk.Label(text='B', bg='yellow')
label2.grid(row=1, column=0, sticky='ns')

window.mainloop()
