# def organiza_por_ultimo_digito(fila):
#     c=0
#     for i in range(len(fila)):
#         if fila[i] % 10 < 6:
#             for j in range(i, c+0, -1):
#                 fila[j], fila[j-1] = fila[j-1], fila[j]
#             c+=1


def organiza_por_ultimo_digito(fila):
    c = 0  # Contador de clientes prioritários já movidos
    for i in range(len(fila)):
        if fila[i] % 10 < 6:  # Verifica se o último dígito é menor que 6 (cliente prioritário)
            mover(fila, i, c)  # Move o cliente da posição `i` para a posição `c`
            c += 1  # Incrementa o contador de prioritários

def mover(fila, origem, destino):
    # Move o cliente da posição `origem` para a posição `destino`, deslocando os outros
    for j in range(origem, destino, -1):
        fila[j], fila[j-1] = fila[j-1], fila[j]  # Troca os elementos

contas = [3819, 3318, 2977, 4331, 2282, 1016]
organiza_por_ultimo_digito(contas)
assert contas == [4331, 2282, 3819, 3318, 2977, 1016]
