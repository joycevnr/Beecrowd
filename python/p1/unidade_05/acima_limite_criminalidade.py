# #Passou notest
def lista_medias(lista):
    # Calcula a soma dos elementos da lista
    soma_ocorrencias = 0
    for i in range(len(lista)):
        soma_ocorrencias += int(lista[i])
        
    # Calcula a média
    media = soma_ocorrencias / len(lista)
    
    return media

def main():
    linhas = []
    media_ssp = float(input())
    
    while True:
        ocorrencias = input()
        if ocorrencias == "fim":
            break
        
        # Calcula a média das ocorrências
        media = lista_medias(ocorrencias.split())
        if (media * 2) < media_ssp:
            break
        if media > media_ssp:
            linhas.append(ocorrencias)
            
    for e in linhas:
        print(e)

main()

### Não passou no test, pois só pode imprimir os valores após digitar fim 
# media_ssp = float(input())

# while True:
#     valores = input()
#     total = 0
#     if valores == 'fim':
#         break
        
#     list_valores = [int(x) for x in valores.split()] #split() é usado em strings, não em inteiros
#     #total = sum([valor for valor in valores])
#     #print(list_valores)

#     for numero in list_valores:
#         total += numero

#     media = total / len(list_valores)

#     if media < media_ssp / 2:
#         break
#     if media > media_ssp:
#         print(valores)

# import sys

# def ler_media_ssp():
#     return float(input())

# def ler_valores():

#     return input()

# def processar_valores(valores):
#     return [int(x) for x in valores.split()]

# def calcular_media(valores):
#     total = sum(valores)
#     return total / len(valores)

# def main():
#     media_ssp = ler_media_ssp()
#     total = 0
    
#     while True:
#         valores = ler_valores()
        
#         if valores == 'fim':
#             break
        
#         list_valores = processar_valores(valores)
        
#         media = calcular_media(list_valores)

#         if media < media_ssp / 2:
#             break
        
#         if media > media_ssp:
#             print(valores)

# if __name__ == "__main__":
#     main()
