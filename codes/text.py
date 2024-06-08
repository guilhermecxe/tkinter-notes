import tkinter as tk

window = tk.Tk()

# Criando uma caixa de texto
text_box = tk.Text()

# Como a caixa de texto é como uma matriz é preciso especificar índices
# e colunas para realizar operações sobre o texto.
# As linhas começam com 1 e as colunas começam com 0

# Especificando que eu quero do primeiro caractere da primeira linha
# até o segundo caractere da primeira linha
button1 = tk.Button(text='Obter os dois primeiros caracteres',
                    command=lambda: print(text_box.get('1.0', '1.2')))

# Especificando que eu quero todo o texto dentro da caixa de texto
button2 = tk.Button(text='Obter todo o texto',
                    command=lambda: print(text_box.get('1.0', tk.END)))

# Inserindo uma string ao final do texto
button3 = tk.Button(text='Inserir Python em uma nova linha',
                    command=lambda: text_box.insert(tk.END, "\nPython"))

text_box.pack()
button1.pack()
button2.pack()
button3.pack()

window.mainloop()
