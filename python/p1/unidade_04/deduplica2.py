valores = input()
lista = valores.split()
flag = True
nova_lista = []

if len(lista) % 2 != 0:
    print(valores)
else:
    metade = len(lista) // 2
    j = metade
    for i in range(metade):
        if lista[i] == lista[j]:
            nova_lista.append(lista[i])
            flag = True
            j += 1
        else:
            flag = False 
            break 
    
    if flag:
        alt = nova_lista[0]
        for i in range(1, len(nova_lista)):
             alt += ' ' + nova_lista[i]
        print(alt)
    else:
        print(valores)


        """
        # Duplicados

Escreva um programa que identifica se uma dada sequência de valores inteiros está duplicada e imprime a lista deduplicada, ou seja, contendo apenas os valores não duplicados. Uma lista é dita duplicada se os valores da primeira metade forem exatamente iguais aos valores da segunda metade da lista em diante. Assim, por exemplo, é duplicada a lista:

    6 9 3 8 6 9 3 8

Enquanto que estas não são:

    1 2 3 1 2 4
    1 2 3 2 1

## Entrada

A entrada consiste em uma única linha, contendo uma lista de valores inteiros, separados por espaços.

## Saída

A saída consiste em uma linha contendo os valores únicos, caso a lista seja, de fato, duplicada, ou todos os valores da lista, caso a lista não seja duplicada.

## Restrições

- você PODE usar `.split()`
- você NÃO pode usar `map()`
- você NÃO pode usar _slices_
"""