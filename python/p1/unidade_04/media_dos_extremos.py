lista = []
acima = 0
abaixo = 0

total = int(input("Digite o número total de elementos: "))

for _ in range(total):
    numero = int(input())
    lista.append(numero)
    
    if len(lista) == 1:
        menor = maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

# Calcula a média dos extremos
media = (menor + maior) / 2

# Conta quantos números estão acima e abaixo da média
for numero in lista:
    if numero > media:
        acima += 1
    elif numero < media:
        abaixo += 1

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Média dos extremos: {media:.2f}")
print(f"{abaixo} número(s) abaixo da média")
print(f"{acima} número(s) acima da média")
