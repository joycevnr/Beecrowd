def acordes(musica_1, musica_2):
    l= musica_1 + musica_2
    unicos = []
    for acorde in l:
        existe = False
       # for i in range(len(l)-1, -1, -1):
        for unico in unicos:
            if acorde == unico:
                existe = True
                break
        if not existe:
            unicos.append(acorde)

    return unicos

m1 = ['c', 'd', 'dm']
m2 = ['c', 'a']
print(acordes(m1, m2))


#print(acordes(m1, m2))
# assert acordes(m1, m2) == ['c', 'd', 'dm', 'a']
# assert m1 == ['c', 'd', 'dm']
# assert m2 == ['c', 'a']

# m1 = ['c', 'd']
# m2 = ['c', 'a']
# assert acordes(m1, m2) == ['c', 'd', 'a']
