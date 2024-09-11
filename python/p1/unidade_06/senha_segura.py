def senha_segura(senha):
    for i in range(len(senha)):
        numero = int(senha[i])
        if i % 2 == 0:  
            if numero % 2 == 0:  # verifica se o número é par
                return 'Senha insegura'
        else:  
            if numero % 2 != 0:  # verifica se o número é ímpar
                return 'Senha insegura'
    
    return 'Senha segura'

assert senha_segura("12346") == "Senha insegura"
assert senha_segura("125638") == "Senha segura"