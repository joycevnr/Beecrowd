def ultimo_indice(num, lista):
    ind = -1
    for i in range(len(lista)):
        if lista[i] == num:
            ind = i
    return ind

print(ultimo_indice(42, [15,2,13,11,14,2]))  

assert ultimo_indice(2, [15,2,13,11,14,2]) == 5
assert ultimo_indice(42, [15,2,13,11,14,2]) == -1
 
#ou

# def ultimo_indice(num, lista):
#     for i in range(len(lista) - 1, -1, -1):  # começa do final da lista
#         if lista[i] == num:
#             return i  # Retorna o primeiro índice encontrado a partir do final
#     return -1  

# # Último Índice

# Escreva a função `ultimo_indice(num, lista)` que recebe um
# inteiro e uma lista de inteiros e que retorna o índice da
# última ocorrência de `num` na `lista`.

# Caso `num` não esteja na lista, a função deve retornar -1.

# ## Exemplos de asserts

# ```
# assert ultimo_indice(2, [15,2,13,11,14,2]) == 5
# assert ultimo_indice(42, [15,2,13,11,14,2]) == -1
# ```
