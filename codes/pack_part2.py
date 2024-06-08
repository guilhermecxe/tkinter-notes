import tkinter as tk

window = tk.Tk()

# Todos os frames se expandem para todos os lado quando a janela aumenta
# de tamanho, algo responsivo

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(master=window, width=10, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH, expand=True)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, expand=True)

window.mainloop()
