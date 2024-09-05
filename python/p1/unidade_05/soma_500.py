while True:
    soma, contador_entrada = 0, 0
    entrada = int(input())

    if soma > 500:
        break

    if entrada > 0:
        soma += entrada
        contador_entrada += 1

media = soma / contador_entrada
print(soma)
print('f{media:.2f}')
print(contador_entrada)
