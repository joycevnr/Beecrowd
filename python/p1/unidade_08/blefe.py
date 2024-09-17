def blefe(array):
    differences = [0] * len(array)
    
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            differences[i] = array[i] - array[i - 1]
            array[i] = array[i - 1]
    
    return differences

a1 = [9, 4, 5, 3, 1]
assert blefe(a1) == [0, 0, 1, 0, 0]
assert a1 == [9, 4, 4, 3, 1]


a2 = [15, 9, 4, 5, 2, 1, 3, 4]
assert blefe(a2) == [0, 0, 0, 1, 0, 0, 2, 3]
assert a2 == [15, 9, 4, 4, 2, 1, 1, 1]

# A ideia a ser utilizada na implementação de `blefe` é reduzir os
# valores que interfiram na ordem, forçando-os a manterem a ordem.
# Assim, se um elemento não é menor que o anterior, ele deve ser
# substituído por valor igual ao anterior, garantindo a ordem. O
# processo deve ser repetido até o final do array.
