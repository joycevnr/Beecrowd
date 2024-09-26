def verificar_maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if maior < lista[i]:
            maior = lista[i]
    return maior


def remove_divisores_do_maior(lista):
    maior = verificar_maior(lista)
    remove = []
    for i in range(len(lista)):
        if maior % lista[i] == 0:
            remove.append(lista[i])

    for elem in remove:
        for i in range(len(lista)-1, -1, -1):
            if elem == lista[i]:
                lista.pop(i)

    





nums = [6, 9, 10, 3, 5]
assert  remove_divisores_do_maior(nums) == None
assert nums == [6, 9, 3]


nums = [10, 20, 5, 24, 30]
assert remove_divisores_do_maior(nums) == None
assert nums == [20, 24]
