def inverte_subseq(seq, ini, count):
    # Extraí a subsequência original
    subseq = seq[ini:ini+count]
    
    # Inverte a subsequência
    subseq_invertida = subseq[::-1] ##Cria uma nova lista que é a subsequência original invertida.
    #Notacao slicing: sequencia[inicio:fim:passo]

    # Substitui a subsequência na lista original
    seq[ini:ini+count] = subseq_invertida
    # Retorna a subsequência original]
    #return seq
    return subseq

def main():
    print(inverte_subseq([1, 2, 3, 4], 1, 2))
main()

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# assert inverte_subseq(nums, 1, 3) == [2, 3, 4]
# assert nums == [1, 4, 3, 2, 5, 6, 7, 8]

# Slicing com Passo
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista[1:7:2])  # Imprime [2, 4, 6]
# 1:7:2: Acessa os elementos do índice 1 até o índice 6, pulando de 2 em 2.

# Slicing com Passo Negativo
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(lista[7:2:-1])  # Imprime [8, 7, 6, 5, 4]
# # 7:2:-1: Acessa os elementos do índice 7 até o índice 3, indo de trás para frente.



#  start:stop: Acessa a parte da sequência do índice start até stop-1.
# start:stop:step: Acessa a parte da sequência do índice start até stop-1, pulando de step em step.
# [::-1]: Inverte a sequência.
# start:stop:-1: Acessa a parte da sequência do índice start até stop+1 em ordem reversa.




#PROBLEMA
# # Inverte subsequência

# Escreva a função `inverte_subseq(seq, ini, count)` que inverte a
# ordem de `count` elementos a partir do índice `ini` da lista `seq`.
# Espera-se que a função tenha efeito colateral e retorne uma cópia da
# subsequência original especificada.

# Veja o arquivo de testes fornecido para exemplos de uso da função.
