def lista_so_com_oposto(lista):
    new_lista = []
    
    for num in lista:
        # Verifica se o oposto está na lista manualmente
        oposto_encontrado = False
        for elemento in lista:
            if elemento == -num:
                oposto_encontrado = True
                break
        
        if oposto_encontrado:
            new_lista.append(num)
    
    # Atualiza a lista original
    lista.clear()  # Limpa a lista original
    lista.extend(new_lista)  # Adiciona os elementos filtrados

# Testes
lista1 = [1, 2, 1, 3, 4, -1, -3, 5]
lista_so_com_oposto(lista1)
print(lista1)  # Deve imprimir [1, 1, -1, -3]
assert lista_so_com_oposto(lista1) == None
assert lista1 == [1, 1, -1, -3]


# # Lista com Números Opostos

# O número oposto de qualquer número n é um número que, se
# somado a n, resulta em 0. Por exemplo, -7 é o número oposto
# de 7 porque 7 + (-7) = 0. Escreva a função
# `lista_so_com_oposto(lista)` que altera a lista de inteiros
# recebida, de forma que sejam mantidos apenas os elementos
# cujos opostos também estejam na lista. A função deve retornar
# None.

# ## Exemplos e Asserts

# ```
# lista1 = [1, 2, 1, 3, 4, -1, -3, 5]
# assert lista_so_com_oposto(lista1) == None
# assert lista1 == [1, 1, 3, -1, -3]
# ```

# <small>Jorge Figueiredo</small>
