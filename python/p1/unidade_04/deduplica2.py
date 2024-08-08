valores = input()
lista = [int(x) for x in valores.split()]
flag = True
nova_lista = []

if len(lista) % 2 != 0:
    print(valores)
else:
    metade = len(lista) // 2
    j = metade
    for i in range(metade):
        if lista[i] == lista[i + 1]:
            nova_lista.append(lista[i])
            flag = True
        else:
            flag = False 
            break 
    
    if flag:
        alt = nova_lista[0]
        for i in range(1, len(nova_lista) - 1):
             alt += ' ' + nova_lista[i]
             print(alt)
    else:
        print(valores)