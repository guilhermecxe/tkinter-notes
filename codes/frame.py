import tkinter as tk

window = tk.Tk()

# Frame é uma forma de organizar elementos. Elementos
# correlatos podem ser armazenados em um mesmo frame

# Esses são alguns estilos que podem ser dados às bordas
# de elementos
# tk.FLAT
# tk.SUNKEN
# tk.RAISED
# tk.GROOVE
# tk.RIDGE

# Dando um estilo a um frame, os estilos só podem ser dados
# quando o tamanho da borda é maior que 0
frame_a = tk.Frame(relief=tk.RIDGE, borderwidth=5)
frame_b = tk.Frame(relief=tk.RIDGE, borderwidth=5)

# Adicionando o label ao frame A. Quando master não é
# especificado o elemento é adicinado diretamente à janela
# principal
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

# Adicionando um botão ao frame A e dando um estilo FLAT a ele
button_a = tk.Button(master=frame_a, text='Click here',
                     relief=tk.FLAT, bg='yellow')
button_a.pack()

# Label ao frame B
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Adicionando os frame à janela
frame_a.pack()
frame_b.pack()

window.mainloop()
