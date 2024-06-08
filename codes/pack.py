import tkinter as tk

window = tk.Tk()

# Posicionando um frame com pack
# que por padrão tem uma largura e uma altura definida e é posicionado
# logo abaixo do último elemento e centralizado
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

# Fazendo o frame ocupar toda a largura
frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

# Fazendo o frame ser posicionado à esquerda e preencher toda a altura
# disponível a ele
frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(side=tk.LEFT, fill=tk.Y)

# Mais opções de side
# tk.TOP
# tk.BOTTOM
# tk.LEFT
# tk.RIGHT

# Também é possível usar tk.BOTH para o elemento se expandir para todos os lados

window.mainloop()
