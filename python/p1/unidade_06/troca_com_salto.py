def troca_com_salto(lista, salto):
    trocas = 0
    for i in range(len(lista)-salto):
        if lista[i] > lista[i+salto]:
            lista[i], lista[i+salto] = lista[i+salto], lista[i]
            trocas += 1
    return trocas

l = [3, 2, -1, 4, 0, 5, 7, 1]
assert troca_com_salto(l, 4) == 2
assert l == [0, 2, -1, 1, 3, 5, 7, 4]