import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
    )
    if not filepath:
        return

    txt_edit.delete('1.0', tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f'Simple Text Editor - {filepath}')

def save_file():
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
    )

    if not filepath:
        return

    with open(filepath, 'w') as output_file:
        text = txt_edit.get('1.0', tk.END)
        output_file.write(text)

window = tk.Tk()
window.title('Simple Text Editor')

window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frm_buttons = tk.Frame()
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save", command=save_file)

txt_edit = tk.Text()

btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)
frm_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()
