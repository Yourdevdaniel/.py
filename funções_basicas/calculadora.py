
def calculadora():
    while True:
        print("Bem vindo a calculadora basica")

        nu1 = input("digite o primeiro numero: ")
        nu2 = input("digite o segundo numero: ")
        print("temos os seguintes operadores +, -, *, /, %")
        operador = input("escolha o operador: ")

        #verificação de numero

        numero_valido = None
        N1 = 0
        N2 = 0

        try:
            N1 = float(nu1)
            N2 = float(nu2)
            numero_valido = True
        except ValueError:
            numero_valido = None

        if numero_valido is None:
            print("Porfavor digite um numero valido")
            continue

        if operador == "+":
            resultado = N1 + N2
        elif operador == "-":
            resultado = N1 - N2
        elif operador == "*":
            resultado = N1 * N2
        elif operador == "/":
            if N2 == 0:
                print("não é possivel dividir por 0")
                continue
            else:
                resultado = N1 / N2
        elif operador == "%":
            if N2 == 0:
                print("não é possivel dividir por 0")
                continue
            else:
                resultado = N1 % N2
        else:
            print("digite um operador valido")
        
        print("Vamos ao tão esperado resultado")
        print(f"{N1} {operador} {N2} o resultado é {resultado}")
            
        sair = input("Deseja sair do programa? [s]im: ").lower().startswith('s')
    
        if sair:
            break

calculadora()