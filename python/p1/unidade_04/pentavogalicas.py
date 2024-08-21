# Lê a entrada do usuário
entrada = input().lower()

# Separa a entrada em palavras, considerando múltiplos espaços
palavras = entrada.split()

# Inicializa o contador de palavras pentavogálicas
contador_pentavogalicas = 0

# Para cada palavra na lista de palavras
for palavra in palavras:
    # Inicializa variáveis booleanas para verificar a presença de cada vogal
    tem_a = tem_e = tem_i = tem_o = tem_u = False

    # Verifica cada letra da palavra
    for letra in palavra:
        if letra == 'a':
            tem_a = True
        elif letra == 'e':
            tem_e = True
        elif letra == 'i':
            tem_i = True
        elif letra == 'o':
            tem_o = True
        elif letra == 'u':
            tem_u = True

    # Verifica se todas as cinco vogais estão presentes
    if tem_a and tem_e and tem_i and tem_o and tem_u:
        contador_pentavogalicas += 1

# Exibe a quantidade de palavras pentavogálicas
print(f'Quantidade de pentavogalicas: {contador_pentavogalicas}')


# # Lê a entrada do usuário
# entrada = input().lower()

# # Separa a entrada em palavras, considerando múltiplos espaços
# palavras = entrada.split()

# # Inicializa o contador de palavras pentavogálicas
# contador_pentavogalicas = 0

# # Para cada palavra na lista de palavras
# for palavra in palavras:
#     # Verifica se todas as cinco vogais estão na palavra
#     if ('a' in palavra and 'e' in palavra and 'i' in palavra and 'o' in palavra and 'u' in palavra):
#         contador_pentavogalicas += 1

# # Exibe a quantidade de palavras pentavogálicas
# print(f'Quantidade de pentavogalicas: {contador_pentavogalicas}')


"""
# Palavras Pentavogalicas

As palavras **pentavogalicas**, também chamadas panvocálicas ou pipistrelos, 
são palavras que contêm as cinco vogais (a, e, i, o, u).
*Juazeiro*, *sequoia*, *Aurelio* são exemplos de pentavogalicas.


Escreva um programa que recebe uma sequencia de palavras e
determina quantas delas são pentavogalicas.

## Entrada

A entrada do programa consiste em uma linha contendo a
sequencia de palavras separadas por um espaço em branco.
Por simplicidade, assumimos que todas as palavras são formadas
por letras minúsculas e sem acentuação.
No exemplo de entrada abaixo, uma sequencia de 5 palavras:
mandinga, juazeiro, cajueiro, sequoia e pirilampo.

```
mandinga juazeiro cajueiro sequoia pirilampo
```

## Saída

A saída é uma mensagem indicando quantas palavras da sequencia
são pentavogalicas. No caso da entrada acima, a saída
produzida seria:

```
Quantidade de pentavogalicas: 3
```

### Atenção
O uso do operador *in* como função de pertencimento só é
permitido para verificar se uma letra é vogal. Não é permitido
usar *in* pra saber se uma letra está numa palavra.


## Exemplo de execução


```
$ python solucao.py
mandinga juazeiro cajueiro sequoia pirilampo
Quantidade de pentavogalicas: 3
```

"""