def remove_consecutivas(lista1):
    remove = []
    for elem in lista1:
        for letra in range(len(elem)-1):
            if elem[letra].lower() == elem[letra+1].lower():
                remove.append(elem)
    #print(remove)
    for i in remove:
        for j in range(len(lista1)-1, -1, -1):
            if i.lower() == lista1[j].lower():
                lista1.pop(j)


lista1 = ['AaSs']
assert remove_consecutivas(lista1) == None
assert lista1 == []

lista1 = ['anna', 'arara', 'tv',   'bacia', 'maaar', 'canna']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'tv',  'bacia']

lista1 = ['arara', 'arroba',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'bacia']
