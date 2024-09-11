#REVER-testes

def maioridade_penal(nomes, idades):
    nome = nomes.split()
    idade = [int(x) for x in idades.split()]
    maiores = []
    for i in range(len(idade)):
        if idade[i] >= 18:
            maiores.append(nome[i])
    if len(maiores) > 0:
        lista = maiores[0]
        for i in range(1, len(maiores)):
            lista += ' ' + maiores[i]
    else:
        lista = ''
    return lista

    
assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
assert maioridade_penal("Jansen Italo Ana","14 11 1") == ''
assert maioridade_penal("Jansen Italo Ana","14 18 1") == 'Italo'
# # Maioridade Penal Função

# Escreva uma função chamada `maioridade_penal` que informe o nome das pessoas
# que atingiram a maioridade penal (idade >= 18). O programa recebe duas strings.
# A primeira com nomes de pessoas e a segunda com as idades destas pessoas
# (separadas por espaço). O programa retorna uma string com os nomes das pessoas
# que atingiram a maioridade penal, na mesma ordem em que foram recebidos na
# entrada. Assuma que a quantidade de pessoas e de idades será sempre igual. Caso
# não haja pessoas 'maiores de idade' o programa  deve retornar uma string vazia.
    
# ## Exemplo de assert

# ```
# assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
# ```
