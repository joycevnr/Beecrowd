def subtrai_polinomios(p1, p2):
    i = 0
    j = 0
    lista = []

    if len(p1) == 0 and len(p2) == 0:
        return lista

    while i < len(p1) or j < len(p2):
        if len(p1) >= len(p2):
            if j < len(p2):
                lista.append(p1[i] - p2[j])
            else:
                lista.append(p1[i])
        elif len(p2) > len(p1):
            if i < len(p1):
                lista.append(p1[i] - p2[j])
            else:
                lista.append(-(p2[j]))

        i += 1
        j += 1

    for k in range(len(lista) - 1, -1, -1):
        if lista[k] == 0:
            lista.pop(k)
        else:
            break

    if len(lista) == 0:
        lista = [0]

    return lista



# def subtrai_polinomios(p1, p2):
#     lista = []
#     m = len(p1) if len(p1) >= len(p2) else len(p2) #comprimento máximo

#     lista = [0] * m

#     # Subtrai os coeficientes dos polinômios
#     for i in range(len(p1)):
#         lista[i] += p1[i]
#     for i in range(len(p2)):
#         lista[i] -= p2[i]

    
#     # Remove os zeros à direita

#     while lista and lista[-1] == 0:
#         lista.pop()
        
#     if len(lista) == 0:
#         lista = [0]

#     return lista


# p1 = [-5, 4, 3]
# p2 = [-1, 0, 2, 0, 0, 0, 5, 0, 0]
# assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]

# p1 = [1, 0]
# p2 = [1]
# assert subtrai_polinomios(p1, p2) == [0]


# Subtração de Polinomios
#        Um  software matemático representa polinômios de uma única variável através de listas que contêm os coeficientes em ordem crescente
#        de grau.  Por exemplo, o polinômio p1(x) = 3x2 + 4x - 5 é representado pela lista [-5, 4, 3], indicando que os coeficientes são -5,
#        4  e 3, para os monômios de grau 0, 1 e 2, respectivamente.  O polinômio p2(x) = 5x6 + 2x2 - 1 é representado pela lista [-1, 0, 2,
#        0, 0, 0, 5], dado que os coeficientes de grau 1, 3, 4 e 5 são iguais a zero.

#        Pede-se que você escreva a função subtrai_polinomios(p1, p2) sem efeito colateral que retorna a lista que  representa  o  polinômio
#        resultante  da  subtração do polinômio p2 de p1, ou p1 - p2.  A função deve retornar a representação reduzida do polinômio, isto é,
#        sem os coeficientes zero desnecessários (veja o exemplo).

#        Relembre que os coeficientes do polinômio diferença são dados pela diferença dos coeficientes de mesmo grau  dos  polinômios  sendo
#        subtraídos.  Assim, p1 - p2, no exemplo acima seria igual a -5x6 + x2 + 4x -4.

#    Exemplos e Asserts
#        Veja o arquivo de testes fornecido.

#        Dalton Serey Atualizado por Dalton Serey em 18/04/2024
