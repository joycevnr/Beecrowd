def meu_reverse(sequencia):
    left = 0
    right = len(sequencia) - 1
    
    while left < right:
        # Troca os elementos nas posições left e right
        sequencia[left], sequencia[right] = sequencia[right], sequencia[left]
        left += 1
        right -= 1

# Testes
seq1 = [1, 2, 3, 4, 5]
meu_reverse(seq1)
assert seq1 == [5, 4, 3, 2, 1]

seq2 = ["A", "B"]
meu_reverse(seq2)
assert seq2 == ["B", "A"]




# # Meu Reverse

# Escreva a função `meu_reverse(sequencia)` que recebe uma sequência mutável como parâmetro e 
# inverte os elementos dessa sequência apenas com trocas de posições dos seus elementos.

# Note que esta função possui efeito colateral e não deve retonar a sequência invertida.

# Não é permitido o uso de lista auxiliar.

# ## Exemplo 1

# ```
# seq1 = [1, 2, 3, 4, 5]
# meu_reverse(seq1)
# assert seq1 == [5, 4, 3, 2, 1]
# ```

# ## Exemplo 2

# ```
# seq2 = ["A", "B"]
# meu_reverse(seq2)
# assert seq2 == ["B", "A"]
# ```

# <small>Wilkerson Andrade</small>
