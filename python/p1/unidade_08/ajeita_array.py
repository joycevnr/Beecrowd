def ordena_par(array):
    i = 0
    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            if array[j] < array[j+1] and array[j+1] % 2 == 0:
                array[j+1], array[j] = array[j], array[j+1]


def ordena_impar(array):
    for i in range(len(array)):   
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1] and array[j] % 2 != 0:
                array[j+1], array[j] = array[j], array[j+1]

def ajeita_array(array):
    ordena_par(array)
    ordena_impar(array)
 #   for i in range(len(array)):



#Escreva a função `ajeita_array(array)` que recebe um array de inteiros e o altera de forma a deixar no início todos os números pares em ordem decrescente seguido dos ímpares em ordem crescente.


arr1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
assert ajeita_array(arr1) == None
assert arr1 == [8, 6, 4, 2, 1, 3, 5, 7, 9]
