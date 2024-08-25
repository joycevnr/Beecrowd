def ler_valores_ate_soma_minima(min_soma):
    soma = 0
    valores = []
    while soma < min_soma:
        valor = int(input())
        soma += valor
        valores.append(valor)
    return soma, valores

def calcular_media(soma, contador):
    return soma / contador if contador > 0 else 0

def contar_acima_da_media(valores, media):
    maiores = 0
    for valor in valores:
        if valor > media:
            maiores += 1
    return maiores

def main():
    MIN_SOMA = 999
    soma, valores = ler_valores_ate_soma_minima(MIN_SOMA)
    
    contador = len(valores)
    media = calcular_media(soma, contador)
    maiores = contar_acima_da_media(valores, media)
    
    print(soma)
    print(f"{media:.2f}")
    print(maiores)

if __name__ == "__main__":
    main()
