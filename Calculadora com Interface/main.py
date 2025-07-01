from tkinter import *
from tkinter import ttk
from funções import(
    adicionar, calcular, limpar, porcentagem,
    raizquadrada
)
root = Tk()
root.title('Calculadora')
frm = ttk.Frame(root, padding = 10)
frm.grid()

entrada = Entry(frm, width=10)
entrada.grid(column=0, row=1, columnspan=8, pady=5)
ttk.Label(frm, text="Calculadora!").grid(column=0, row=0)
historico = Listbox(frm, height=10, width=30)
historico.grid(column=4, row=1, rowspan=5, padx=(10,0))
scrollbar = Scrollbar(frm, orient=VERTICAL, command=historico.yview)
scrollbar.grid(column=5, row=1, rowspan=5, sticky='ns')
historico.config(yscrollcommand=scrollbar.set)
# Botões
ttk.Button(frm, text='7', command=lambda: adicionar(entrada, '7')).grid(column=0, row=2)
ttk.Button(frm, text='8', command=lambda: adicionar(entrada, '8')).grid(column=1, row=2)
ttk.Button(frm, text='9', command=lambda: adicionar(entrada, '9')).grid(column=2, row=2)
ttk.Button(frm, text='/', command=lambda: adicionar(entrada, '/')).grid(column=3, row=2)
ttk.Button(frm, text='4', command=lambda: adicionar(entrada, '4')).grid(column=0, row=3)
ttk.Button(frm, text='5', command=lambda: adicionar(entrada, '5')).grid(column=1, row=3)
ttk.Button(frm, text='6', command=lambda: adicionar(entrada, '6')).grid(column=2, row=3)
ttk.Button(frm, text='*', command=lambda: adicionar(entrada, '*')).grid(column=3, row=3)
ttk.Button(frm, text='1', command=lambda: adicionar(entrada, '1')).grid(column=0, row=4)
ttk.Button(frm, text='2', command=lambda: adicionar(entrada, '2')).grid(column=1, row=4)
ttk.Button(frm, text='3', command=lambda: adicionar(entrada, '3')).grid(column=2, row=4)
ttk.Button(frm, text='-', command=lambda: adicionar(entrada, '-')).grid(column=3, row=4)
ttk.Button(frm, text='0', command=lambda: adicionar(entrada, '0')).grid(column=0, row=5)
ttk.Button(frm, text='C', command=lambda: limpar(entrada)).grid(column=1, row=5)
ttk.Button(frm, text='=', command=lambda: calcular(entrada, historico)).grid(column=2, row=5)
ttk.Button(frm, text='+', command=lambda: adicionar(entrada, '+')).grid(column=3, row=5)
ttk.Button(frm, text='%', command=lambda: porcentagem(entrada, historico)).grid(column=3, row=5)
ttk.Button(frm, text='√', command=lambda: raizquadrada(entrada, historico)).grid(column=3, row=6)
root.mainloop()