import tkinter as tk

def increase():
    # Obtém o valor da label lbl_value e o altera
    value = int(lbl_value['text'])
    lbl_value['text'] = f'{value + 1}'

def decrease():
    # Obtém o valor da label lbl_value e o altera
    value = int(lbl_value['text'])
    lbl_value['text'] = f'{value - 1}'

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_value = tk.Label(text='0')
lbl_value.grid(row=0, column=1)

# command diz a função que é executada quando o botão é pressionado
btn_decrease = tk.Button(text='-', command=decrease)
btn_decrease.grid(row=0, column=0, sticky='nsew')

btn_increase = tk.Button(text='+', command=increase)
btn_increase.grid(row=0, column=2, sticky='nsew')

window.mainloop()
