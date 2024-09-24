                                               
##isertion_sort
def inserir(valor, lista):
    lista.append(valor)
    pos_valor = len(lista) -1
    
    # Troca as posições enquanto não chegar à posição 0
    while pos_valor != 0:
        lista[pos_valor-1], lista[pos_valor] = lista[pos_valor], lista[pos_valor-1]
        pos_valor -= 1
        
    # print(lista)


def reorganiza(nums1, nums2):
    pares = []
    impares = []
    
    for num in range(len(nums1)-1, -1, -1):
        if nums1[num] % 2 == 0:
            pares.append(nums1[num])
            nums1.pop(num)

    for num in range(len(nums2)-1, -1, -1):
        if nums2[num] % 2 != 0:
            impares.append(nums2[num])
            
            nums2.pop(num)
    #print("impar", impares)

    for num in range(len(impares)-1, -1, -1):
        # print(impares[num])
        nums1.append(impares[num])
        
    # print("impares", impares)
    # print("nums1", nums1)
    
    #pares
    for num in pares:
        # print(num)
        inserir(num, nums2)


# # Teste
nums1 = [1, 3, 8, 1, 4]
nums2 = [8, 10, 2, 9, 3, 2, 11]
reorganiza(nums1, nums2)
# print(nums1)  # [1, 3, 1, 9, 3, 11]
# print(nums2)  # [8, 4, 8, 10, 2, 2]



# def reorganiza(nums1, nums2):
#     pares = []
#     impares = []

#     # Processa nums1
#     for num in nums1:
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)

#     # Processa nums2
#     for num in nums2:
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)
#     #Atualiza nums1 e nums2
#     nums1[:] = impares
#     nums2[:] = pares




# Reorganiza pares e ímpares

# Escreva a função `reorganiza(nums1, nums2)` que recebe duas
# listas de inteiros e as reorganiza movendo todos os ímpares
# para a primeira lista e todos os pares para a segunda.
# Contudo, os elementos de `nums1` devem ser deixados antes dos
# elementos de `nums2` nas duas listas e, por fim, os números
# devem ser mantidos na ordem relativa original.

# ## Exemplo

# Por exemplo, suponha que as listas sejam:
# * `nums1 = [1, 3, 8, 1, 4]` e
# * `nums2 = [8, 10, 2, 9, 3, 2, 11]`

# A função deve mover todos os ímpares para `nums1` e os pares
# para `nums2`, fazendo com que, ao final, fiquem assim:

# * `nums1 = [1, 3, 1, 9, 3, 11]`
# * `nums2 = [8, 4, 8, 10, 2, 2]`

# Observe que os valores `8` e `4` que constavam originalmente
# em `nums1` foram movidos pro início de `nums2`. Já os valores
# `9`, `3` e `11`, originalmente em `nums2` foram movidos pro
# final de `nums1`.

# > Este caso de teste foi fornecido no arquivo de testes.

# ## Observação

# Leia o teste fornecido e observe que a função tem efeito
# colateral e altera as listas originais. Além disso, é
# importante que opere **em tempo linear** (o famoso **O(n)**)
# em relação ao total de elementos nas duas listas.
