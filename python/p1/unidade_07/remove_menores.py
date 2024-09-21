def remove_menores(N, lista):
    qtd = 0
    for i in range(len(lista)):
        if lista[i] < N:
            qtd += 1
            #lista.pop(lista[i])
    return qtd

lista = [1, 2, 3, 4, 5]
print(remove_menores(3, lista))

# assert remove_menores(3, lista) == 2
# assert lista == [3, 4, 5]



# # Remove Menores de uma Lista

# Escreva a função <code>remove_menores(N, lista)</code> 
# que recebe um inteiro N e uma lista de inteiros e que 
# elimina da lista todos os valores menores que N. 
# A função retorna o número de elementos eliminados.

# ## Exemplos e Asserts

# ```
# lista = [1, 2, 3, 4, 5]
# assert remove_menores(3, lista) == 2
# assert lista == [3, 4, 5]
# ```
