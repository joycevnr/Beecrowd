soma = 0
contador = 0
while True:
    temp = float(input())
    if 10 <= temp <= 30:
        soma += temp
        contador += 1
    else:
        break

print(f'Temperatura inadequada! {temp:.2f}.')
print(f'{contador} medições lidas dentro do padrão.')
print(f'Média = {(soma/contador):.2f}.')






# # Monitor temperatura

# Um criador de peixes quer monitorar a temperatura do seu aquário, uma vez
# que seus peixes só sobrevivem se a temperatura estiver entre 10.0 e 30.0 graus
# Celsius (incluindo essas temperaturas).

# Para tanto, ele instalou um termômetro que, periodicamente, coleta a temperatura no aquário.
# Pede-se que você implemente um programa que lê uma sequencia de temperaturas e, caso leia uma
# temperatura inadequada, emite um alerta e encerre relatando o resumo das últimas temperaturas válidas lidas. 

# ## Entrada

# O programa deve ler uma quantidade indeterminada de temperaturas. A leitura deve parar quando uma temperatura inadequada for lida.

# *Importante.* Assuma que pelo menos uma temperatura válida foi lida.

# # Saída

# Na saída, seu programa deve imprimir um alerta e um resumo das temperaturas válidas lidas até então.

# # Exemplo

# ```
# $ python monitor.py
# 11.9
# 13.2
# 29.0
# 14.3
# 9.8
# Temperatura inadequada! 9.80.
# 4 medições lidas dentro do padrão.
# Média = 17.10.
# ```
