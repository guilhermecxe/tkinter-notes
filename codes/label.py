import tkinter as tk

# Criando a janela que roda a aplicação
window = tk.Tk()

# Criando uma label de texto
greeting = tk.Label(text='Hello World!',
                    foreground="white",
                    background="#34A2FE",
                    width=10,
                    height=10)
# foreground se refere à cor do texto da label
# background se refere à cor do background da label

# Altura e largura é medido por unidades de texto,
# ou caracteres, onde cada unidade é referente à
# largura e altura de um 0

# Ao invés de foreground e background pode ser usado
# fg e bg, respectivamente


# .pack "empacota" as labels criadas, fazendo com que
# a janela tenha apenas o tamanho necessário para
# exibir as labels
greeting.pack()

# Loop para rodar a aplicação
window.mainloop()
