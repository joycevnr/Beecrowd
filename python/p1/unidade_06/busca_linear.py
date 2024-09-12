def busca(seq, valor):
    for i in range(len(seq)):
        if seq[i] == valor:
            return i
    else:
        return -1

print(busca([8, 9, 2, 3, 6, 10, 7, 9], 6))
seq = [8, 9, 2, 3, 6, 10, 7, 9]
assert busca(seq, 6) == 4
assert busca(seq, 4) == -1
assert busca(seq, 9) == 1


# # Busca Linear

# Escreva a função `busca(seq, valor)` que implementa o algoritmo
# de busca linear. Em caso de elementos repetidos, deve-se
# buscar o primeiro da lista. Veja os asserts abaixo, para
# entender a semântica da função.

# ## Exemplos e asserts

# ```
# seq = [8, 9, 2, 3, 6, 10, 7, 9]
# assert busca(seq, 6) == 4
# assert busca(seq, 4) == -1
# assert busca(seq, 9) == 1
# ```

# ## Restrições

# Desnecessário dizer que nenhuma função de python que itere
# sobre listas pode ser usada nesta questão. Observe que o
# sistema de testes pode indicar sucesso, neste caso, mas a
# resposta estará errada, de qualquer forma.
