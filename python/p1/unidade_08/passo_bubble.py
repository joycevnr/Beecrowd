def passo_bubble(seq):
    trocas = 0
    for i in range(len(seq)-1):
        #for i in range(len(seq) -1 -j):
        if seq[i] > seq[i+1]:
            seq[i], seq[i+1] = seq[i+1], seq[i]
                #break
            trocas += 1
    return trocas


seq = [3, 1, 5, 9, 4]
assert passo_bubble(seq) == 2
assert seq == [1, 3, 5, 4, 9]


# # Um Passo Bubble

# Escreva a função `passo_bubble(seq)` que recebe uma lista de numeros inteiros e que faz um passo (apenas um passo!) do algoritmo bubble sort, trocando dois a dois valores vizinhos que estejam fora de ordem crescente.

# ## Semântica da função

# A função deve ter efeito colateral e deve retornar o número
# de trocas realizadas. Veja os exemplos de asserts no arquivo
# de testes fornecido.
