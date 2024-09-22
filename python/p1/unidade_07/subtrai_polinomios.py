##Falta corrigir

def subtrai_polinomios(p1, p2):
    lista = []
    m = len(p1) if len(p1) >= len(p2) else len(p2) #comprimento máximo

    lista = [0] * m

    # Subtrai os coeficientes dos polinômios
    for i in range(len(p1)):
        lista[i] += p1[i]
    for i in range(len(p2)):
        lista[i] -= p2[i]

    # Remove os zeros à direita
    while lista and lista[-1] == 0:
        lista.pop()

    return lista


# def subtrai_polinomios(p1, p2):
#     lista = []
#     m = len(p1) - 1
#     for i in range(m):
#         subtracao = p1[i] - p2[i]
#         if subtracao != 0:
#             lista.append(subtracao)
#     restante = len(p2) - len(p1) 
#     for i in range(restante, -1, -1):
#         lista.append(p2[i])
#     return lista


p1 = [-5, 4, 3]
p2 = [-1, 0, 2, 0, 0, 0, 5]
print(subtrai_polinomios(p1, p2))


# # Subtração de Polinomios

# Um software matemático representa polinômios de uma única variável através de listas que contêm os coeficientes em ordem crescente de grau. Por exemplo, o polinômio p1(x) = 3x2 + 4x - 5 é representado pela lista [-5, 4, 3], indicando que os coeficientes são -5, 4 e 3, para os monômios de grau 0, 1 e 2, respectivamente. O polinômio p2(x) = 5x6 + 2x2 - 1 é representado pela lista [-1, 0, 2, 0, 0, 0, 5], dado que os coeficientes de grau 1, 3, 4 e 5 são iguais a zero.

# Pede-se que você escreva a função `subtrai_polinomios(p1, p2)` sem efeito colateral que retorna a lista que representa o polinômio resultante da subtração do polinômio p2 de p1, ou p1 - p2. A função deve retornar a representação reduzida do polinômio, isto é, sem os coeficientes zero desnecessários (veja o exemplo).

# Relembre que os coeficientes do polinômio diferença são dados pela diferença dos coeficientes de mesmo grau dos polinômios sendo subtraídos. Assim, p1 - p2, no exemplo acima seria igual a -5x6 + x2 + 4x -4.

# def test_exemplo_1():
#     p1 = [-5, 4, 3]
#     p2 = [-1, 0, 2, 0, 0, 0, 5]
#     assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]

# def test_exemplo_2():
#     p1 = [-5, 4, 3]  # 3x2 + 4x - 5
#     p2 = [-4, 2, 3]  # 3x2 + 2x - 4
#     assert subtrai_polinomios(p1, p2) == [-1, 2]  # 2x - 1
