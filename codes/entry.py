import tkinter as tk

window = tk.Tk()

label = tk.Label(text='Name')

# Entry é usado para o usuário inserir uma pequena quantidade
# de texto
entry = tk.Entry(width=15)

# Obtendo o texto presente no elemento entry
button1 = tk.Button(
    text='Enviar',
    command=lambda: print(entry.get()))

# Deletando o primeiro dígito no elemento entry
button2 = tk.Button(
    text='Deletar primeiro dígito',
    command=lambda: entry.delete(0))

# Deletando os dois primeiros dígitos no elemento entry
button3 = tk.Button(
    text='Deletar os dois primeiros dígitos',
    command=lambda: entry.delete(0, 2))

# Deletando todo o texto no elemento entry
button4 = tk.Button(
    text='Deletar tudo',
    command=lambda: entry.delete(0, tk.END))

# Inserindo um texto na posição especificada
button5 = tk.Button(
    text='Inserir "Python"',
    command=lambda: entry.insert(tk.END, "Python"))

label.pack()
entry.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

window.mainloop()
