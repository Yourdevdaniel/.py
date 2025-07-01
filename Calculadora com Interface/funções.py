from tkinter import END
import math


def adicionar(campo, valor):
    campo.insert(END, valor)

def limpar(campo):
    campo.delete(0, END)

def calcular(entrada, historico):
    expressao = entrada.get()
    try:
        resultado = eval(expressao)
        entrada.delete(0, END)
        entrada.insert(0, resultado)
        historico.insert(END, f'{expressao} = {resultado}')
    except:
        entrada.delete(0, END)
        entrada.insert(0, 'Error')

def porcentagem(entrada, historico):
    expressao = entrada.get()
    try:
        resultado = float(expressao) / 100
        entrada.delete(0, END)
        entrada.insert(0, resultado)
        historico.insert(END, f'{expressao}% = {resultado}')
    except:
        entrada.delete(0, END)
        entrada.insert(0, 'Error')

def raizquadrada(entrada, historico):
    expressao = entrada.get()
    try:
        numero = float(expressao)
        resultado = math.sqrt(numero)
        entrada.delete(0, END)
        entrada.insert(0, resultado)
        historico.insert(END, f'√{expressao} = {resultado}')
    except:
        entrada.delete(0, END)
        entrada.insert(0, 'Error')






