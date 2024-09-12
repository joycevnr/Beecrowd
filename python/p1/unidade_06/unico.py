
def unico(string):
    new_string = ""
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            new_string += string[i]
    if len(string) > 0:  # Verifica se a string não está vazia
        new_string += string[-1]
    return new_string
            
print(unico("aa***xxxzzb+"))
    
assert unico("aa***xxxzzb+++") == "a*xzb+"
#assert unico("aa***xxxzzb+") == "a*xzb+"
assert unico("") == ""

# # Único

# Escreva a função `unico(string)` que recebe uma string e 
# retorna uma string formada  a partir da string original
# pela substituição da sucessão de ocorrências (consecutivas) 
# de um mesmo caractere por esse caractere. Não utilizar nenhuma lista
# auxiliar. Por simplificação, assuma que a string não possui nem 
# caracteres acentuados nem letras maiúsculas.

# ## Exemplos de asserts

# ```
# assert unico("aa***xxxzzb+++") == "a*xzb+"
# assert unico("") == ""
# ```

# outra solucao
def unico(string):
    if not string:  
        return ""
    
    new_string = string[0]  
    for i in range(1, len(string)):  
        if string[i] != string[i-1]:  # Compara o atual com o anterior
            new_string += string[i]
    return new_string

