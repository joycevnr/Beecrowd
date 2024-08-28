while True:
    registro = input()
    contador = 0
    total = [] 
    if registro == 'fim':
        break

    partes = registro.split()
    resultado = partes[1]

    for i in resultado:
        if i == 'l' or i == 'z':
            contador += 1
        elif i == 'p':
            if contador > 0:
                total.append(str(contador))
            contador = 0
    if contador > 0:  # Adiciona o último período se terminar sem 'p'
        total.append(str(contador))


    ##SAÍDA
    if total == []: ## o mesmo que if not total:
        print(f"{partes[0]}: 0")
    else:
        alt = total[0]
        for i in range(1, len(total)):
            alt += ' + ' + total[i]
        print(f"{partes[0]}: {alt}") 


# # Viabilidade das Filiais

# Uma empresa de grande porte costuma fazer estudo de viabilidade
# de suas filiais. O processo simplificado do estudo de viabilidade
# de uma filial é baseado na análise dos lucros e prejuízos da
# filial por um período de tempo. Nesse processo,
# convencionalmente, se usa a letra 'l' pra indicar que a filial
# teve lucro no mês, a letra 'p' pra indicar prejuízo e a letra 'z'
# para indicar que a filial não teve nem lucro nem prejuízo. A
# filial é viável quando ela não apresenta prejuízo.


# ## Um exemplo

# Considere a sequência de registros durante um periodo da filial 1:

# ```
# Filial_1 llpzzllllzzppplppzzl
# ```

# É possível verificar que a Filial 1 esteve viável nos 2 primeiros
# meses, depois em mais 8 meses, depois em 1 mês e, por fim, nos 3
# últimos meses do período usado no exemplo acima.

# Em resumo, poderíamos utilizar a sequência abaixo pra indicar os
# períodos de viabilidade da Filial 1.
# ```
# 2 8 1 3
# ```

# Escreva um programa que produz um relatório de viabilidade de um
# conjunto de filiais.

# ## Entrada

# Seu programa deve ler uma sequência de registros de resultados
# de uma série de filiais. Cada linha é o registro durante um certo
# período de uma filial.  Nenhum espaço separa os registros. A
# palavra `fim` funciona como sentinela e indica o fim dos registros.

# O exemplo abaixo mostra 4 séries de registros e a sentinela 
# indicando fim da entrada.

# ```
# Filial_1 llpzzllllzzppplppzzl
# Filial_2 ppllllllpzzzpllzl
# Filial_3 lllllllllpzzzpplllp 
# Filial_4 pppppp
# fim
# ```

# ## Saída

# Para cada sequência de registro de uma filial, o programa deve 
# imprimir os períodos de viabilidade da filial. Se não houver 
# nenhum período de viabilidade, apenas a indicação de 0 deve ser 
# apresentada para a filial.

# Abaixo, a saída gerada pelo programa para a entrada acima.

# ```
# Filial_1: 2 + 8 + 1 + 3
# Filial_2: 6 + 3 + 4
# Filial_3: 9 + 3 + 3
# Filial_4: 0
# ```

# ## Restrições

# Não é permitido usar as facilidades de python para contagem de 
# caracteres específicos em strings, tal como o método `count` ou 
# equivalentes. 

# **Observação** Só é permitido usar o `split()` para separar no
# espaço em branco.

# <small>Jorge Figueiredo</small>
