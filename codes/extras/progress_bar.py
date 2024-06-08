import tkinter as tk
from tkinter.ttk import Progressbar
import time

def open_new_window():
    def step():
        for i in range(5):
            new_window.update_idletasks() # para atualizar visualmente a barra de progresso
            pb1['value'] += 20 # para atualizar o progresso da barra
            time.sleep(1)
        new_window.destroy() # fechar a nova janela
    print('1')
    time.sleep(2)
    new_window = tk.Toplevel() # criando uma nova janela
    time.sleep(2)
    print('2')
    pb1 = Progressbar(new_window, orient=tk.HORIZONTAL, length=100, mode='determinate')
    time.sleep(2)
    print('3')
    pb1.pack(expand=True)
    time.sleep(2)
    print('4')
    tk.Button(new_window, text='Start', command=step).pack()

window = tk.Tk()

tk.Button(window, text='Abrir janela de progresso', command=open_new_window).pack()

window.mainloop()
