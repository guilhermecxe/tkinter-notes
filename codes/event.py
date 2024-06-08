import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    print(event.char)

'''
.bind liga um evento a uma função, no caso, estamos ligando
o pressionar de uma tecla à função handle_keypress
'''
window.bind("<Key>", handle_keypress)

window.mainloop()
