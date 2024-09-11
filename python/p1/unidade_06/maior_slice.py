def maior_slice(lista):
    maior = []
    atual = []
    
    for i in range(len(lista)):
        if not atual or lista[i] > atual[-1]:
            atual.append(lista[i])
        else:
            if len(atual) > len(maior):
                maior = atual
            atual = [lista[i]]
    
    # Verificar a última subsequência
    if len(atual) > len(maior):
        maior = atual
    
    return maior



lista = [7, 6, 2, 9, 10]
print(maior_slice(lista))

# assert maior_slice([1, 2, 3, 4, 2, 0, 1]) == [1, 2, 3, 4]
# assert maior_slice([7, 6, 2, 9, 10]) == [2, 9, 10]
# assert maior_slice([7, 8, 9, 1, 2, 3, 0]) == [1, 2, 3]                                                                                                                                                             