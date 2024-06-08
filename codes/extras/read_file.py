import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

def askopenfile():
    # Se o usuário cancelar a seleção de um arquivo é gerado um erro,
    # porque file não irá conter name
    file = filedialog.askopenfile(mode='r', title='Select a file', filetypes=(('txt files', '*.txt'),))
    print(file.name)
    print(file.readlines())

btn = tk.Button(text='Obter arquivo', command=askopenfile)
btn.pack()

window.mainloop()
