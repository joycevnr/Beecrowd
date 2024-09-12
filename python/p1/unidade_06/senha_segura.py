def senha_segura(senha):
    for i in range(len(senha)):
        numero = int(senha[i])
        if i % 2 == 0:  #índices pares correspondem a posições ímpares na senha
            if numero % 2 == 0:  # verifica se o número é par
                return 'Senha insegura'
        else:  #posição par na senha
            if numero % 2 != 0:  # verifica se o número é ímpar
                return 'Senha insegura'
    
    return 'Senha segura'

assert senha_segura("12346") == "Senha insegura"
assert senha_segura("125638") == "Senha segura"

# # Senha Segura

# Os cartões de crédito com chip (smartcards) requerem de seus usuários
# uma senha numérica para que a transação financeira seja efetivada. Esta
# senha é fornecida para os usuários pela administradora de cartões e pode
# variar de tamanho dependendo da bandeira ou banco do cliente. As senhas
# obedecem uma lei de formação com o objetivo de torná-las mais seguras. 
# Uma senha segura é composta por um número de pelo menos 4 dígitos, cujos
# algarismos nas posições ímpares são todos ímpares e que os algarismos nas
# posições pares são todos pares. Por exemplo: Considere a senha segura 7852.
# O primeiro algarismo (7) e o terceiro algarismo (5) são ímpares. O segundo 
# algarismo (8) e o quarto algarismo (2) são pares. Crie uma função que recebe
# uma senha numérica e verifica se essa senha é segura ou insegura.
    
# ## Exemplo de assert

# ```
# assert senha_segura("12346") == "Senha insegura"
# assert senha_segura("125638") == "Senha segura"
# ```
