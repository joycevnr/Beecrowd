def reducoes(seq):
    lista = []
    if len(seq) == 1 or len(seq) == 0:
        return lista
    
    for i in range(len(seq)-1):
        reducao = seq[i] - seq[i+1]
        if reducao >= 0:
            lista.append(reducao)
        elif reducao < 0:
            lista.append(0)
            
    return lista

print(reducoes([4, 2, 0, 6, 3, 4]))
                    
assert reducoes([4, 2, 0, 6, 3, 4]) == [2, 2, 0, 3, 0]
assert reducoes([3, 0, 3, 6, 1]) == [3, 0, 0, 5]
   

# # Reduções

# Escreva a função `reducoes(seq)` que retorna uma lista
# contendo os valores das reduções (diferenças) entre cada dois
# valores consecutivos da sequência de inteiros `seq`. Caso a
# diferença entre dois valores consecutivas seja negativa
# (ou não seja uma redução), o valor 0 deve ser registrado na
# lista resultante. Se a sequência for vazia ou se só tiver um
# elemento, uma lista vazia deve ser retornada.

# # Exemplos

# Veja os asserts abaixo, como exemplos da semântica da função:

# ```
# assert reducoes([4, 2, 0, 6, 3, 4]) == [2, 2, 0, 3, 0]
# assert reducoes([3, 0, 3, 6, 1]) == [3, 0, 0, 5]
# ```
