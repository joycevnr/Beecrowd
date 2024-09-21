def tem_afinidade(l1, l2):
    contador = 0
    if len(l1) >= len(l2):
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] == l2[j]:
                    contador += 1
    elif len(l1) < len(l2):
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] == l2[j]:
                    contador += 1
    
    if contador >= 3:
        return True
    else:
        return False
                    
        


l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True


# # Afinidade Musical

# Uma métrica utilizada pelo facebook para sugerir
# amigos a um determinado usuário é utilizar o conceito
# de afinidade musical. A ideia é simples. A partir de
# duas listas de artistas que dois usuários gostam, 
# o sistema considera que há afinidade musical
# se os dois gostam de 3 ou mais artistas iguais.

# Implemente a função `tem_afinidade(l1, l2)` que retorna
# verdadeiro caso os usuários possuam afinidade e 
# falso, caso contrário.

# ## Exemplos de asserts

# ```
# l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
# l2 = ['zeze', 'joao', 'u2', 'jquest']
# assert tem_afinidade(l1, l2) == True
# ```


# def tem_afinidade(l1, l2):
#     # Converte as listas em conjuntos para eliminar duplicatas e facilitar a interseção
#     intersecao = set(l1) & set(l2)  # Interseção dos dois conjuntos, 
#     return len(intersecao) >= 3  

# l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
# l2 = ['zeze', 'joao', 'u2', 'jquest']
# assert tem_afinidade(l1, l2) == True


#Operador & (Interseção de Conjuntos):
# Uso: Utilizado entre dois conjuntos (set) para encontrar a interseção.
# Sintaxe: set1 & set2
# Tipo de Operação: Operação de conjuntos que retorna um novo conjunto contendo apenas os elementos que estão em ambos os conjuntos.