import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

# Com .place, ao invés de .pack, é possível/necessário
# especificar a localização onde o elemento ficará
# e o elemento é posicionado de modo que o seu canto
# superior esquerda fique na posição especificada.
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()
