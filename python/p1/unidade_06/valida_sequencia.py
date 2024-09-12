def valida_seq(nums):
    for i in range(len(nums)):
        if nums[i] % 2 != 0 and (i+1) % 2 == 0:
            return i
        elif nums[i] % 3 != 0 and (i+1) % 3 == 0:
            return i

print(valida_seq([1, 2, 2, 4, 5, 6]))
        
            
assert valida_seq([11, 8, 9, 4, 11, 6]) is None
assert valida_seq([11, 8, 9, 4, 11, 10]) == 5
assert valida_seq([1, 2, 2, 4, 5, 6]) == 2



# # Valida Sequência

# Em uma dada aplicação, uma sequência de números inteiros gerados
# em uma certa etapa do processo só são válidos se duas condições
# puderem ser verificadas: i) todos os valores em posições pares da
# sequência devem ser eles próprios pares; e ii) todos os valores
# em posições múltiplas de 3 devem ser eles próprios múltiplos de
# três. Por exemplo, a sequência 11, 8, 9, 4, 11, 6 é válida: i)
# porque os valores nas posições pares são pares (8, na posição 2;
# 4 na posição 4; e 6 na posição 6); e ii) porque os valores nas
# posições múltiplas de 3 são múltiplos de 3 (9, na posição 3; e
# 6 na posição 6).

# Escreva a função `valida_seq(nums)` que recebe a lista de
# inteiros produzida na primeira etapa do processo e faz sua
# validação. Se a sequência é válida, a função deve retornar
# `None`; e se a sequência for inválida, deve retornar o índice
# (não a posição) do primeiro elemento que invalida a posição. Por
# exemplo, se a sequência 11, 8, 9, 4, 11, 10 for passada pra a
# função, ela deve retornar `5` para indicar que o valor 10 que
# está na 6a posição da lista invalida uma das condições (neste
# caso, porque 10 não é múltiplo de 3).

# Veja o arquivo de testes fornecido para compreender melhor a
# função.
