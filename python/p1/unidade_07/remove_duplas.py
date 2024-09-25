def remove_duplas(lista):
    for i in range(len(lista) -1, -1, -1):
        qtd = 0
        for j in range(len(lista) -1, -1, -1):
            if lista[i] == lista[j]:
                qtd += 1
                ult = j
        if qtd == 2:
            lista.pop(i)
            lista.pop(ult)

            
    return lista



lista = [1, 1, 3, 2, 1, 3, 4, 5, 6, 6, 6]
print(remove_duplas(lista))