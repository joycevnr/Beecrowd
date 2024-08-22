# Escreva um programa que identifica se uma dada sequência de valores inteiros está duplicada e imprime a lista deduplicada, ou seja, contendo apenas os valores não duplicados. Uma lista é dita duplicada se os valores da primeira metade forem exatamente iguais aos valores da segunda metade da lista em diante.
## NÃO PASSOU NO P1-TEST
# Lê a lista de inteiros da entrada
lista = [int(x) for x in input().split()]

# Verifica se a lista tem menos de dois elementos
if len(lista) < 2:
    # Se tiver apenas um elemento, imprime diretamente
    if len(lista) == 1:
        print(lista[0])
    else:
        print("")  # Se a lista estiver vazia, imprime uma linha vazia
else:
    # Calcula a metade da lista
    metade = len(lista) // 2

    # Flag para indicar se a lista está duplicada
    flag = True

    # Nova lista para armazenar a primeira metade se estiver duplicada
    nova_lista = []

    # Compara elementos das duas metades da lista
    for i in range(metade):
        if lista[i] == lista[metade + i]:
            nova_lista.append(lista[i])
        else:
            flag = False
            break

    # Prepara a saída com base na flag
    if flag:
        x = nova_lista
    else:
        x = lista

    # Prepara a string de saída
    if len(x) == 1:
        print(x[0])
    else:
        alt = str(x[0])
        for i in range(1, len(x)):
            alt += ' ' + str(x[i])
        print(alt)
