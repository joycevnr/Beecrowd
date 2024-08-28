# Inicialização das contagens
peso_count = 0
combustivel_count = 0
altitude_count = 0

# Leitura e processamento das entradas
while True:
    linha = input()
    
    # Separar os valores usando split
    valores = linha.split()
    
    # Converter valores para inteiros
    peso = int(valores[0])
    combustivel = int(valores[1])
    altitude = int(valores[2])
    
    # Verificar se algum dado é negativo
    if peso < 0:
        print("dado inconsistente. peso negativo.")
        break
    elif combustivel < 0:
        print("dado inconsistente. combustível negativo.")
        peso_count += 1
        break
    elif altitude < 0:
        print("dado inconsistente. altitude negativa.")
        combustivel_count += 1
        peso_count += 1
        break
    
    # Se todos os dados são válidos, incrementar os contadores
    peso_count += 1
    combustivel_count += 1
    altitude_count += 1

# Imprimir os resultados
print(f"peso: {peso_count}")
print(f"combustível: {combustivel_count}")
print(f"altitude: {altitude_count}")


#  Caixa Preta Descartando Leituras

# Na análise dos dados de uma caixa preta é muito importante detectar 
# o momento em que houve falha na coleta de dados do peso, combustível 
# e altitude. Se qualquer um desses elementos for negativo, considera-se 
# que a partir daquele momento (incluindo o dado negativo) 
# as medições não são confiáveis e a leitura deve ser interrompida, 
# considerando apenas os valores válidos para análise.

# Faça um programa que leia várias medições de peso, combustível e altitude 
# e determine o momento em que os dados passaram a ser considerados inválidos, 
# além de determinar quantos dados válidos
# foram lidos de cada categoria (peso, combustível e altitude)

# ## Entrada

# Seu programa deverá ler as medições até que um dos valores lidos seja negativo.
# Em cada linha, são lidos peso, combustível e altitude (separados por espaço).

# ## Saída

# Na saída, seu programa deve imprimir uma mesagem detalhando qual dado 
# foi considerado inválido, e a quantidade de dados válidos lidos para 
# cada categoria.

# Dependendo do dado inválido, a mensagem pode variar. Veja
# as três mensagens possíveis abaixo:

# ```
#     - dado inconsistente. peso negativo.
#     - dado inconsistente. combustível negativo.
#     - dado inconsistente. altitude negativa.
# ```

# ## Restrições e Recursos permitidos

# É permitido utilizar a função split. 
# Não é permitido utilizar a função map.

# ## Exemplo de execução

# ```
# $ python solution.py
# 10 2 3
# 3 1 -1
# dado inconsistente. altitude negativa.
# peso: 2
# combustível: 2
# altitude: 1
# ```
# ```
# $ python solution.py
# 1 2 4
# -1 2 3
# dado inconsistente. peso negativo.
# peso: 1
# combustível: 1
# altitude: 1
# ```
