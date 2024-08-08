import math

# Leitura dos valores de entrada
angulo_inicial = float(input())
delta = float(input())
N = int(input())

# Impressão do cabeçalho da tabela
print("|Angulo| Seno|Cosseno|")

# Cálculo e impressão dos valores de seno e cosseno para cada ângulo
for i in range(N):
    angulo = angulo_inicial + i * delta
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    print(f"|{angulo:6.1f}|{seno:7.5f}|{cosseno:7.5f}|")
