n, m = input().split()

numeros_casas = [int(x) for x in input().split()]

numeros_encomendas = [int(x) for x in input().split()]

casa_indices = {numero: i for i, numero in enumerate(numeros_casas)}

qtd_espacos = 0

indice_inicial = 0

for i in numeros_encomendas:
    indice_i = casa_indices[i]
    qtd_espacos += max(indice_inicial,indice_i) - min(indice_inicial,indice_i)
    indice_inicial = indice_i

print(qtd_espacos)