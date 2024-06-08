import tkinter as tk

window = tk.Tk()

'''
grid é um sistema de posicionamento, assim como pack e place,
mas grid funciona como uma tabela onde se especifica a linha e a coluna
onde o elemento será posicionado.
'''

for i in range(3):
    '''
    .columnconfigure e .rowconfigure são usados para descrever o que acontece
    dentro de um grid quando a janela é redimensionada.
    Estamos definindo um loop que percorre 3 linhas e 3 colunas e aproveitando
    o primeiro loop para definir as configurações de cada linha e cada coluna
    ao mesmo tempo.
    `weight` diz o "peso" de um elemento ao ser redimensionado, então se um
    elemento tem peso 1 e outro tem peso 2, o primeiro elemento cresce a metade
    do que o outro cresce quando a janela é aumentada.
    `minsize` diz o tamanho mínimo que uma célula do grid deve ter, evitando
    que textos desaparecem quando a janela fica pequena demais.
    '''
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            relief=tk.RAISED,
            borderwidth=1)

        '''
        Para adicionar padding se usa padx ou pady de acordo com a orientação.
        Adicionando padding a esta label diz a distância da label até o frame
        onde ela está contida. E esse espaço é preenchido pela própria label. 
        '''
        label = tk.Label(
            master=frame,
            text=f'{i}x{j}',
            bg='yellow',
            #pady=10
            )

        '''
        Padding à célula de um grid diz a distância que deve haver até a outra
        célula
        '''
        frame.grid(row=i, column=j, padx=10)
        '''
        Padding a este pack diz a distância que deve have entre a borda do frame
        e a label. E este espaço pertence ao frame, diferente do padding
        adicionado à label
        '''
        label.pack(pady=10)
        
window.mainloop()
