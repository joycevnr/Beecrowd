import sys
media_ssp = float(input())
total = 0

while True:
    valores = input()
    
    if valores == 'fim':
        break
        
    list_valores = [int(x) for x in valores.split()] #split() é usado em strings, não em inteiros
        #total = sum([valor for valor in valores])

    for numero in list_valores:
        total += numero

    media = total / len(list_valores)

    if media < media_ssp / 2:
        break
    
    if media > media_ssp:
        print(valores)

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
