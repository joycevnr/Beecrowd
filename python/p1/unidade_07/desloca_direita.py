def desloca(lista, origem, destino):
    lista.append(lista[origem])
    lista.pop(origem)
    print('remove', lista)
    #insert
    i = len(lista) -1
    while i != destino:
        lista[i], lista[i-1] = lista[i-1], lista[i]
        i -= 1 
    
    # for i in range(len(lista)-1, -1, -1):
    #     if i != destino:
    #         lista[i], lista[i-1] = lista[i-1], lista[i]
    #     else: break
        
        print(lista)

l1 = [2,6,9,11,13,5]
desloca(l1, 2, 4)
assert l1 == [2,6,11,13,9,5]

# def desloca(lista, origem, destino):
#     # Salva o valor que será movido
#     valor = lista[origem]
    
#     # Desloca os elementos para a esquerda
#     for i in range(origem, destino):
#         lista[i] = lista[i + 1]
#         print(lista)
    
#     # Coloca o valor na posição de destino
#     lista[destino] = valor

# Testes



# l1 = [0,1,2,3,4,5,6]
# desloca(l1, 4, 6)
# assert l1 == [0,1,2,3,5,6,4]

# # Desloca o elemento para a direita

# Implemente a função `desloca(lista, origem, destino)` que move o elemento na posição 
# **origem** para a posição **destino** recebidas como argumento. Assuma que **origem** e 
# **destino** são índices válidos e **origem** sempre é menor do que **destino**. Isto 
# é, o deslocamento é para a direita.

# Note também que não basta apenas trocar **origem** por **destino**, é preciso deslocar os 
# elementos entre essas duas posições. Veja os exemplos de asserts para melhor entendimento 
# da questão.

# A função tem efeito colateral e não é permitido criar outra lista.
