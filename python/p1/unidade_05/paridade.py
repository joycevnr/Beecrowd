while True:
    valor = input()
    qtd = 0
    for elem in valor:
        if elem == '1':
            qtd +=1
    if qtd % 2 != 0:
        print('ERRO: ' + valor)
        break