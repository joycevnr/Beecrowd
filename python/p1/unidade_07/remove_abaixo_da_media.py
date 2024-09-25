def media(l1):
    soma = 0
    
    for i in l1:
        soma += i
    media = soma/len(l1)
    return media
        
        

def remove_abaixo_media(l1):
    medias = media(l1)
    for i in range(len(l1)-1, -1, -1):
        if l1[i] < medias:
            l1.pop(i)
    return l1
    
    
    
l1 = [1, 1, 1, 1]
remove_abaixo_media(l1)
assert l1 == [1, 1, 1, 1]

l1 = [1, 1, 1, -1, 1]
remove_abaixo_media(l1)
assert l1 == [1, 1, 1, 1]
    

# Remove abaixo da média
#        Escreva a função remove_abaixo_media(l1) que remove da lista passada como parâmetro os elementos abaixo da média
#        (calculada a partir de todos os elementos da lista).

#    Restrições
#        É proibido usar as seguintes funções ou recursos da linguagem: sum, remove e del.

#    Exemplos e Asserts
#               l1 = [1, 1, 1, 1]
#               remove_abaixo_media(l1)
#               assert l1 == [1, 1, 1, 1]

#               l1 = [1, 1, 1, -1, 1]
#               remove_abaixo_media(l1)
#               assert l1 == [1, 1, 1, 1]
