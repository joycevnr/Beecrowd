def gerar_e_imprimir_sequencia(limite):
    numero = 1  # Primeiro número da sequência
    soma = 0    # Soma acumulada dos números
    sequencia = []  # Lista para armazenar os números da sequência
    
    # Gera os números da sequência enquanto a soma for menor que o limite
    while soma + numero < limite:
        sequencia.append(numero)
        soma += numero
        numero *= 2  # Próximo número é o dobro do atual
    
    for num in sequencia:
        print(num, end=' ')

limite = int(input("Digite um número natural como limite: "))
gerar_e_imprimir_sequencia(limite)
