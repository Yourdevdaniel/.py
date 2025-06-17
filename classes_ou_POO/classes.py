class Ficha: # Convenção é usar a primeira letra maiúscula para classes
    def __init__(self, nome, idade, estado_civil, sexualidade, telefone, pais, cidade, sexo):
        self.nome = nome
        self.idade = idade
        self.estado_civil = estado_civil
        self.sexualidade = sexualidade
        self.telefone = telefone
        self.pais = pais
        self.cidade = cidade
        self.sexo = sexo

    def exibir_ficha(self):
        print("--------------------------")
        print("Dados da Ficha")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"Estado Civil: {self.estado_civil}")
        print(f"Sexualidade: {self.sexualidade}")
        print(f"Telefone: {self.telefone}")
        print(f"País: {self.pais}")
        print(f"Cidade: {self.cidade}")
        print("Fim da Ficha")
        print("--------------------------")

def fazer_ficha():
    print("Preencha seus dados para a ficha:")
    nome_input = input("Nome: ")
    idade_input = int(input("Idade: ")) # Converte para int
    estado_civil_input = input("Estado Civil: ")
    sexualidade_input = input("Sexualidade: ")
    sexo_input = input("Sexo: ")
    telefone_input = input("Telefone: ")
    pais_input = input("País: ")
    cidade_input = input("Cidade: ")
    return nome_input, idade_input, estado_civil_input, sexualidade_input, \
           telefone_input, pais_input, cidade_input, sexo_input

# --- A PARTE QUE FALTAVA (ou que estava incorreta) ESTÁ AQUI ---

# 1. CHAMA a função fazer_ficha() para que ela colete os dados
#    E armazena o que ela "devolve" (a tupla de dados) na variável 'dados_coletados'.
dados_coletados = fazer_ficha()

# 2. DESEMPACOTA os dados coletados da tupla para variáveis individuais.
#    A ordem aqui importa e deve ser a mesma do 'return' da função!
nome_final, idade_final, estado_civil_final, sexualidade_final, \
telefone_final, pais_final, cidade_final, sexo_final = dados_coletados

# 3. CRIA o objeto da classe Ficha usando as variáveis que agora existem FORA da função.
nova_ficha = Ficha(nome_final, idade_final, estado_civil_final,
                   sexualidade_final, telefone_final, pais_final, cidade_final, sexo_final)

# 4. EXIBE a ficha.
nova_ficha.exibir_ficha()