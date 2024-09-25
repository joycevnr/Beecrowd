def verifica_esteira(esteira, componentes):
    lista = []
    for est in esteira:
        
        for comp in componentes:
            if est == comp:
                lista.append(est)
                break

    # print(lista)
    # print(componentes)
    if lista == componentes:
        return True
    else:
        return False



# def verifica_esteira(esteira, componentes):
#     lista = []
#     for i in esteira:
#         if i in componentes:
#             lista.append(i)
#     print(lista)
#     print(componentes)
#     if lista == componentes:
#         return True
#     else:
#         return False  



# esteira = [2, 1, 3, 4]
# componentes = [2, 4]
# assert verifica_esteira(esteira, componentes)
# assert esteira == [2, 1, 3, 4]
# assert componentes == [2, 4]

esteira = [1, 3, 4]
componentes = [4, 1, 3]
print(verifica_esteira(esteira, componentes))
# assert esteira == [1, 3, 4]

