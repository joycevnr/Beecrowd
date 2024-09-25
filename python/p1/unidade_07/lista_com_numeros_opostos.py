def lista_so_com_oposto(lista):
    for num in range(len(lista) - 1, -1, -1):
        oposto_encontrado = False
        for elem in range(len(lista) - 1, -1, -1):
            if lista[num] + lista[elem] == 0:
                oposto_encontrado = True
                break
        if not oposto_encontrado:
            lista.pop(num)

lista1 = [1, 2, 1, 3, 4, -1, -3, 5]
lista_so_com_oposto(lista1)
print(lista1)

lista2 = [1, 2, 1, 3, 4, -1, -3, 5]
assert lista_so_com_oposto(lista2) == None
assert lista2 == [1, 1, 3, -1, -3]

# # # Lista com Números Opostos

# # O número oposto de qualquer número n é um número que, se
# # somado a n, resulta em 0. Por exemplo, -7 é o número oposto
# # de 7 porque 7 + (-7) = 0. Escreva a função
# # `lista_so_com_oposto(lista)` que altera a lista de inteiros
# # recebida, de forma que sejam mantidos apenas os elementos
# # cujos opostos também estejam na lista. A função deve retornar
# # None.

# # <small>Jorge Figueiredo</small>
