qtd_pares = 0
qtd_impares = 0
pares = []
impares = []
i = 0

while True:
    valor = int(input())
    i += 1
    if valor % 2  == 0:
        pares.append(i)
        qtd_pares += 1
    else:
        impares.append(i)
        qtd_impares += 1


    if  abs(qtd_pares - qtd_impares) > 2:
        break

#verifica maior quantidade

if qtd_pares > qtd_impares:
    print('PARES em maior quantidade')
else:
    print('ÍMPARES em maior quantidade')

#Ordenação
print('ÍMPARES:')
for i in range(len(impares)):
    print(impares[i])
print('PARES:')
for i in range(len(pares)):
    print(pares[i])