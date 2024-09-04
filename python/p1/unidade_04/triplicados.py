lista = input().split()
valores_unicos = []
contagem = []

for numero in lista:
    encontrado = False
    for i in range(len(valores_unicos)):
        if valores_unicos[i] == numero:
            contagem[i] += 1
            encontrado = True
            break
    if not encontrado:
        valores_unicos.append(numero)
        contagem.append(1)

# verificar quais números aparecem exatamente três vezes
triplicados = []
for i in range(len(contagem)):
    if contagem[i] == 3:
        triplicados.append(valores_unicos[i])

for i in range(len(triplicados)):
    print(triplicados[i])


#da AI:
# # Percorrer a lista original
# for numero in lista:
#     if numero in valores_unicos:
#         # Se o número já estiver na lista de valores únicos, incrementa a contagem
#         indice = valores_unicos.index(numero)
#         contagem[indice] += 1
#     else:
#         # Se o número não estiver na lista de valores únicos, adiciona-o
#         valores_unicos.append(numero)
#         contagem.append(1)

# # Verificar quais números aparecem exatamente três vezes
# triplicados = []
# for i in range(len(contagem)):
#     if contagem[i] == 3:
#         triplicados.append(valores_unicos[i])

# print(triplicados)

#erro:

# for i in range(len(seq) -1):
#     if seq[i] == seq[i+1]:
#         valor = seq[i]
#         if valor == seq[i]:
#             triplicado = valor
#             ##triplicados.append(valor)
#     triplicados.append(triplicado)


# print(triplicados)
# for i in range(len(triplicados)):
#     print(triplicados[i])
        
        