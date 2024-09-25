def triplets(lista):
    # Contagem de dígitos de 0 a 9
    contagem = [0] * 10  # Inicializa uma lista de contagem com 10 zeros

    # Contar ocorrências de cada dígito na lista
    for num in lista:
        contagem[num] += 1

    # Remove dígitos que aparecem exatamente 3 vezes
    i = 0
    while i < len(lista):
        print(contagem[lista[i]])
        if contagem[lista[i]] == 3:
            lista.pop(i)  # Remove o elemento
        else:
            i += 1  # Apenas avança se não removeu

# Teste da função
digitos = [1, 1, 2, 2, 5, 1]
triplets(digitos)
assert digitos == [2, 2, 5]          
            

    

# digitos = [1, 1, 2, 2, 5, 1]
# triplets(digitos)
# assert triplets(digitos) == None
# assert digitos == [2, 2, 5]


# # Remove Dígitos com 3 Ocorrências

# Escreva a função `triplets(lista)` que recebe uma lista de
# dígitos (inteiros entre 0 e 9, inclusive) como parâmetro e que
# remove dessa lista todos os dígitos que aparecem **exatamente
# três vezes**. A função não deve retornar nada e deve ter efeito
# colateral.
