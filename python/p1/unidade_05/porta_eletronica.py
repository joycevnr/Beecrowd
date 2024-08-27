lista_reg = []

def registro():
    while True:
        entrada = input()
        if entrada == 'S':
            break
        if entrada[0] == 'R':
            lista_reg.append(entrada[2])
        if entrada[0] == 'P':
            pesquisa(entrada[2], lista_reg)

def pesquisa(entrada, lista):
    contador = 0
    for i in range(len(lista)):
        if entrada == lista[i]:
            contador += 1
    print(contador)


registro()


# # Porta Eletrônica

# Numa empresa, cada funcionário é identificado por um código composto de uma
# letra maiúscula seguida por 5 dígitos. Um exemplo seria o código `A12345`.
# Funcionários da mesma categoria são identificados pelo caractere inicial do
# código. Ou seja, `A12345k` pertence à categoria `A`.

# Pede-se que você faça um programa _interativo_ que simule um terminal de
# controle de ponto dos funcionários desta empresa. Seu programa deve ter duas
# operações: registro de ponto e pesquisa de categoria.

# O registro é feito através das linhas que começam com o caractere `R` (de
# _registro_) seguidas do código do funcionário. Exemplo: `R A12345`. A pesquisa,
# por outro lado, é marcada por uma linha que começa com o caractere `P` (de
# _pesquisa_) seguido da letra que representa esta categoria. Exemplo: `P A`.

# Assim, sempre que houver uma consulta (por exemplo, `P A`), o seu programa deve
# imprimir na tela a quantidade de registros de pontos de funcionários daquela
# categoria.

# > Observe que um mesmo funcionário pode registrar mais de uma vez o ponto. E
# > cada registro deste mesmo funcionário deve ser contabilizado no total de cada
# > categoria. Seu programa deve encerrar ao encontrar uma linha com o caractere
# > `S` (de _saída_). Veja o exemplo de uso.

# # Exemplo

# ```
# $ python exemplo.py
# R A12345
# R A12345
# P A
# 2
# R A00007
# P A
# 3
# R B90000
# P B
# 1
# R B90001
# P B
# 2
# S
# ```
