import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry('500x500')

columns = ('time', 'pontos', 'jogos')

'''
show='headings' esconde a primeira coluna, a coluna #0.
Mais opções de show:
'tree': mostra a coluna #0
'tree headings': mostra #0 e linha header. Esse é o padrão
'': não mostra nem #0 nem as headers
'''
tree = ttk.Treeview(window, columns=columns,
                       show='headings')

tree.heading('time', text='Time')
tree.heading('pontos', text='Pontos')
tree.heading('jogos', text='Jogos')

rows = [
    ('Corinthians', '6', '2'),
    ('Flamengo', '2', '2'),
    ('Santos', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ('Palmeiras', '1', '2'),
    ]

for row in rows:
    tree.insert('', tk.END, values=row)
    
tree.grid(row=0, column=0)

scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

window.mainloop()
