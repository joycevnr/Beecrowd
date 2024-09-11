def caixa_registradora(lista, meta):
    soma = 0
    comissao = 0
    for i in range(len(lista)):
        soma += lista[i]
        if lista[i] < 1000:
            comissao += lista[i] * 0.05
        elif 1000 <= lista[i] < 5000:
            comissao += lista[i] * 0.1
        elif lista[i] >= 5000:
            comissao += lista[i] * 0.15
    #valor_if_verdadeiro if condição else valor_if_falso
    status = 'Lucro' if soma - comissao >= meta else 'Prejuizo'
    
    return f'{soma:.1f}, {comissao:.1f}, {status}'

lista = [1000, 2000, 5000, 2500, 950]
print(caixa_registradora(lista, 2000))
        