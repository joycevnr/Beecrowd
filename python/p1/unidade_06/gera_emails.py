def email(nome):
    nome = nome.split()
    email = nome[0].lower() + '.' + nome[-1].lower() + '@ccc.ufcg.edu.br'
    return email

def gera_emails(nomes):
    emails = []
    for nome in nomes:
        emails.append(email(nome))
    return emails

print(gera_emails(['Mariana Silva Lima', 'Joao Arthur', 'Pedro Alvares Cabral']))

nomes = ['Mariana Silva Lima', 'Joao Arthur', 'Pedro Alvares Cabral']
emails = ['mariana.lima@ccc.ufcg.edu.br', 'joao.arthur@ccc.ufcg.edu.br', 'pedro.cabral@ccc.ufcg.edu.br']



# # Gera emails

# O coordenador de computação precisa gerar emails para os feras de cada 
# período a partir de seus nomes. O padrão do email gerado é 
# *primeiro_nome.segundo_nome@ccc.ufcg.edu.br*. Implemente uma função que 
# receba uma lista contendo os nomes dos feras e retorna uma nova lista 
# contendo os emails gerados.

# Você pode assumir que os nomes completos são compostos de pelo menos dois nomes.

# ## Exemplos de uso da função

# ```
# nomes = ['Mariana Silva Lima', 'Joao Arthur', 'Pedro Alvares Cabral']
# emails = ['mariana.lima@ccc.ufcg.edu.br', 'joao.arthur@ccc.ufcg.edu.br', 'pedro.cabral@ccc.ufcg.edu.br']
# assert gera_emails(nomes) == emails
# ```

# ## Recursos

# É permitido usar as função split e lower.
