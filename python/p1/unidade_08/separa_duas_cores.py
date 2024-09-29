def separa_duas_cores(array, cor1, cor2):
    c = 0
    for i in range(len(array)):
        if array[i] == cor1:
             for j in range(i, c+0, -1):
                array[j], array[j-1] = array[j-1], array[j]
             c+=1

##colocar no final    
# def separa_duas_cores(array, cor1, cor2):
#     c = 0
#     for i in range(len(array)):
#         if array[i] == cor1:
#              for j in range(i, len(array)-1, +1):
#                 array[j], array[j+1] = array[j+1], array[j]
#              c+=1
#     print(array)
             
             
array = ['a', 'a', 'b', 'a', 'b']
separa_duas_cores(array, 'b', 'a')
assert array == [ 'b', 'b', 'a', 'a', 'a']


array = [0, 1, 0]
separa_duas_cores(array, 0, 1)
assert array == [0, 0, 1]

array = [0, 1, 0]
separa_duas_cores(array, 1, 0)
assert array == [1, 0, 0]
 

# # Organiza Array com Duas Cores

# Escreva a função `separa_duas_cores(array, cor1, cor2)` que
# recebe um array que contém apenas elementos de dois
# valores distintos (aqui chamados de cores). A função deve
# alterar o array fornecido, trazendo todos os elementos da `cor1` para o início do array e deixando todos os elementos da `cor2` no final do array. Assumir que o array contém pelo menos um elemento.

# ## Use a API de Arrays

# Observe que esta questão é sobre arrays. Logo, embora o tipo
# efetivamente recebido pela função seja uma lista, você deve
# processá-lo como um array, restringindo-se às operações da API
# de arrays.

# Naturalmente, você também não deve utilizar nenhuma função de
# ordenação de Python nem mesmo deve usar qualquer um dos
# algoritmos clássicos de ordenação (quicksort, selectionsort,
# bubblesort, por exemplo).

# ## Exemplo e Assert

# Leia os exemplos fornecidos.

# <small>Atualizada por Dalton, em 10/abr/2024</small>
