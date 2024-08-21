n = int(input())
total = []
valido = 0 
consistente = True
# medicoes igual a peso, combutivel e altitude
for i in range(n):
    lista = [float(x) for x in input().split()]
    if consistente:
        valido += 3
        if lista[0] < 0:
            print('dado inconsistente. peso negativo.')
            valido -= 3
            consistente = False
        elif lista[1] < 0:
            print('dado inconsistente. combustível negativo.')
            valido -= 2
            consistente = False
        elif lista[2] < 0:
            print('dado inconsistente. altitude negativa.')
            valido -= 1
            consistente = False


print(f"{valido} dados válidos.")
