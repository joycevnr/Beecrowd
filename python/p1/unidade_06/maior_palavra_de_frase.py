def maior_palavra(frase):
    maior_palavra = ""
    palavra_atual = ""
    
    for caractere in frase:
        if caractere == " ":  
            if len(palavra_atual) >= len(maior_palavra):
                maior_palavra = palavra_atual
            palavra_atual = ""  
        else:
            palavra_atual += caractere  
    
    # última palavra após o fim do loop
    if len(palavra_atual) >= len(maior_palavra):
        maior_palavra = palavra_atual
    
    return maior_palavra

frase = "eu acredito que seja um bom exemplo"
print(maior_palavra(frase)) 

assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"

# # Maior Palavra de Uma Frase

# Escreva a função `maior_palavra(frase)` que recebe uma 
# frase e retorna a maior palavra da frase. Caso tenha mais 
# de uma palavra com o maior tamanho, a função deve retornar 
# a última delas. Em tempo, considere que a frase possui 
# pelo menos uma palavra e não inclui caracteres especiais ou 
# de acentuação ou de pontuação.

# ## Atenção

# Não é permitido usar `split()`, listas e nenhum função de
# ordenação de Python.

# ## Exemplo e Assert

# ```
# assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"
# ```
