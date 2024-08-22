def remove_letras_alternadas(palavra):
    resultado = ""
    for i in range(len(palavra)):
        if i % 2 == 0:
            resultado += palavra[i]
    return resultado

def main():
    palavra = input()
    resultado = remove_letras_alternadas(palavra)
    print(resultado)

main()

## Remove Letras Alternadas

# Escreva um programa que leia uma palavra da primeira linha
# da entrada e imprima as letras da palavra lida,
# alternadamente, começando da primeira letra. Assuma que as
# palavras são grafadas sem acentos e/ou caracteres especiais.

# # Entrada

# O programa deve ler uma palavra da entrada.

# # Saída

# Imprima apenas as letras nas posições 0,2,4...

# # Exemplo de Execução

# ```
# $ python3 solucao.py
# cabelos
# cbls
# ```
