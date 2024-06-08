import tkinter as tk

window = tk.Tk()

# Definir um botão é bem parecido com definir uma label,
# no entanto, é possível usar um comando que será
# executado quando o botão for pressionado
button1 = tk.Button(
    text='Click here',
    width=25,
    height=5,
    bg='grey',
    fg='black',
    command=lambda: print('Olá'))

# Mudando o estilo de um botão para solid
# quando não estiver pressionado
button2 = tk.Button(
    text='Click me',
    relief='solid',
    command=lambda: print('Oi'))
    
button1.pack()
button2.pack()

window.mainloop()
