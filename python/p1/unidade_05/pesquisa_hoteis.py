# # Pesquisa Hotéis

# Durante a escolha de um hotel, um usuário, tipicamente, usa alguns
# critérios para decidir qual empresa escolher. Faça um programa que leia
# uma sequência de registros de um determinado tipo de quarto de hotel e permita ao usuário pesquisar
# o quarto mais adequado de acordo com algum dos seguintes critérios: valor, tamanho e
# conforto.

# ## Entrada

# O programa deve ler registros até que a string '---' seja lida.
# Um registro possui os seguintes campos (separados por vírgula):
# valor,tamanho,conforto,empresa. Por exemplo: 200.10,2,12,ibis.

# Você pode considerar que nenhum dos valores é igual ou menor do que 0.

# Depois da leitura dos registros, deve ler uma sequencia de operações de pesquisa até que 
# a palavra 'fim' seja lida.

# As operações de pesquisa são determinadas pelas seguintes palavras:

# ```
#     - valor
#     - tamanho
#     - conforto
# ```

# ## Saída

# Sempre que seu programa ler uma pesquisa, ele deve imprimir o nome da empresa que
# oferta o melhor quarto de acordo com o critério escolhido. O melhor quarto por valor é,
# naturalmente, o de menor valor. O melhor quarto por tamanho é o maior. O mesmo
# acontece com o critério conforto. 

# **Importante.** Assuma que não há empate em nenhum critério.


# ## Exemplo de execução

# ```
# $python solution.py
# 2000.0,1,16,h1
# 4000.0,4,7,h2
# 1900.0,6,23,h3
# 1500.0,3,5,h4
# 8000.0,0,1,h5
# ---
# valor
# h4
# tamanho
# h3
# conforto
# h3
# fim
# ```

# ## Restrições e Recursos

# É permitido utilizar a função split.
