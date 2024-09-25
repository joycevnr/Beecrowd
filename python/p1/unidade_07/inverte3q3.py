def inverte3a3(s):
    pedaços = []
    flag = 0  

    # Dividindo a string em pedaços de 3 caracteres manualmente
    pedaco = ''
    for i in range(len(s)):
        pedaco += s[i]
        flag += 1
        
        if flag == 3:
            pedaços.append(pedaco)
            pedaco = ''  # Reseta o pedaço para começar um novo
            flag = 0  # Reseta o flag

    # Adiciona o último pedaço se houver caracteres restantes
    if pedaco:
        pedaços.append(pedaco)
    
    new_string = ''  # Inicializa a nova string fora do loop

    # Invertendo a ordem dos pedaços manualmente
    for i in range(len(pedaços) - 1, -1, -1):
        new_string += pedaços[i]
    
    return new_string

# Teste
s = "abcdefghijklm"
print(inverte3a3(s))  # Saída esperada: "ijklmdefabc"

assert inverte3a3("abcdef") == "defabc"



# assert inverte3a3("abcdef") == "defabc"

# def inverte3a3(s):
#     pedaços = []
    
#     for i in range(0, len(s), 3):
        
#         pedaços.append(s[i:i+3])
#         # pedaços = ['abc', 'def']
#         new_string = ''
#     for i in range(len(pedaços) - 1, -1, -1):
#         # range(start, stop, step)
#         # Por exemplo, se pedaços tem 4 elementos, len(pedaços) - 1 é 3.
#         new_string += pedaços[i]
    
#     return new_string



# assert inverte3a3("abcdef") == "defabc"

# # Sequencia Invertida 3 a 3

# Escreva a função `inverte3a3(s)` que recebe uma _string_
# `s` de caracteres e retorna uma _string_ que corresponde à
# _inversão 3 a 3_ dos caracteres de `s`.

# A chamada _inversão 3 a 3_ consiste em inverter a ordem dos
# _tokens_ (pedaços) de `s` de tamanho 3. Assim, por exemplo, se
# `s` for `abcdef` a _string_ retornada deve ser `defabc`, porque
# os tokens `abc` e `def` são invertidas. Outro exemplo seria
# `abcdefghijkl` que resultaria em `jklghidefabc`. Perceba que o _token_
# `abc` que era o primeiro de `s` é o último na _string_
# resultante. E que `cde`, que era o segundo, se torna o penúltimo
# (ou segundo de trás pra frente) na _string_ resultante.

# ## Detalhes e restrições

# 1. Você pode assumir que a _string_ `s` tem tamanho múltiplo de 3.
# 2. Você não deve utilizar _slices_.

# ## Exemplo

# ```python
# assert inverte3a3("abcdef") == "defabc"
# ```
