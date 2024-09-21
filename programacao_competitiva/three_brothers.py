entrada = input().split()

if '1' in entrada and '2' in entrada:
    print('3')
elif '1' in entrada and '3' in entrada:
    print('2')
elif '2' in entrada and '3' in entrada:
    print('1')
    
# tres_irmaos - {1, 2, 3}
# lista = set(map(int, input().split()))

# diferenca = tres_irmaos - lista
# print(diferenca)