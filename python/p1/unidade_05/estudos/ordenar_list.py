def selection_sort_descending(arr):
    # Percorre toda a lista
    for i in range(len(arr)):
        # Encontra o maior elemento na parte não ordenada da lista
        max_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        # Troca o elemento encontrado com o primeiro elemento da parte não ordenada
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        # arr[i]: Representa o elemento na posição atual i da lista.
        #arr[max_idx]: Representa o maior elemento encontrado na parte não ordenada.
        #Depois que o maior elemento é encontrado, ele é trocado de lugar com o primeiro elemento da parte não ordenada (arr[i]).
        

    return arr


# Comparar e trocar: Em cada iteração, o algoritmo compara cada par de elementos adjacentes. Se um elemento é maior que o próximo, eles trocam de lugar.
# algoritmo de ordenação por bolha (bubble sort). Esse algoritmo é mais fácil de entender e implementar, embora não seja o mais eficiente para listas grandes.
# Exemplo de uso
# my_list = [int(x) for x in input().split()]
# sorted_list = selection_sort_descending(my_list)
# print(sorted_list)


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # Últimos i elementos já estão ordenados
#         for j in range(0, n-i-1):
#             # Troca se o elemento encontrado for maior que o próximo
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# # Exemplo de uso
# my_list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# sorted_list2 = bubble_sort(my_list2)
# print(sorted_list2)
