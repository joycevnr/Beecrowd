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

# PROBLEMA
# Acima da média (Criminalidade)

# Um delegado precisa fazer um relatório anual das ocorrências
# registradas em sua delegacia. Para facilitar a escrita do relatório,
# ele deseja selecionar os meses em que a média de ocorrências por dia
# for maior que a média estabelecida pela secretaria de segurança pública (ssp).

# Pede-se que você escreva um programa que leia a média mensal estabelecida pela secretaria
# de segurança pública e várias sequencias de valores
# que representam a quantidade de ocorrências registradas por dia na delegacia. 
# Seu programa deve imprimir na saída apenas as sequências cuja média mensal é maior 
# que o estabelecido.

# Você não deve assumir que serão lidos 30 ou 31 registros por linha. Tipicamente, 
# os delegados esquecem de registrar ou dados são perdidos.

# ## Entrada de dados

# A entrada consiste em um texto contendo: 1) na primeira linha
# o valor da média mensal estabelecida pela ssp; 2) nas linhas
# seguintes, as sequências de valores a serem processados; 3)
# uma linha contendo a palavra 'fim', indicando o fim
# da entrada. 

# Importante: o programa também deve parar de ler a
# entrada quando receber uma sequência de valores cuja média
# seja 2 vezes menor que o valor limite indicado na primeira
# linha da entrada. Todos os valores são expressos em
# número de ocorrências, como inteiros. No entanto, a média é expressa
# como float.

# ## Saída de dados

# A saída consiste em uma linha para cada sequência cuja média seja 
# maior que o valor limite. Cada uma das linhas contém os
# mesmos valores lidos da entrada.

# ## Exemplos de execução

#     $ python joao.py
#     100.0
#     77 72 65
#     101 110
#     fim
#     101 110

#     $ python joao.py
#     20.0
#     120 110 12
#     9 8
#     120 110 12
