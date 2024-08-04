n = int(input(''))
contador = 0

for c in range(0, n):
    num = str(input())
    for e in range(len(num) - 1): 
        if int(num[e]) % 2 == 0 and int(num[e + 1]) % 2 == 0:
            contador += 1
            break

print(contador)

# o número lido tem que ser tratado como uma string para acessar cada caractere individualmente.
# a principal dúvida acredito que seja no segundo for:
# len(num): Retorna o comprimento da string.
# range(len(num) - 1): com o comprimento de num é preciso tirar 1, porque como acesso o próximo dígito com num[i + 1], então preciso parar antes do último índice para evitar um erro.