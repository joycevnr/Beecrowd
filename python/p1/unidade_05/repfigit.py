entrada = input()
if 9 < int(entrada) < 100:
    valores = []
    t0 = str(entrada[0])
    t1= str(entrada[1])
    valores.append(int(t0))
    valores.append(int(t1))

    i = valores[-1]
    while i < int(entrada):
        new_valor = valores[-1] + valores[-2]
        if new_valor < int(entrada):
            valores.append(new_valor)
        i =  valores[-1]
    i = 0
    while i < len(valores):
        print(f'T{i} = {valores[i]}')
        i+=1
    print('---')
    print(f'{entrada} é um repfigit.' if valores[-1] == int(entrada) else f'{entrada} não é um repfigit.')
