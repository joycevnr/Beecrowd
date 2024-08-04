lista_de_strings = ["3", "4", "5"]
iterador = map(int, lista_de_strings)  # Aplica a função int a cada elemento

print(iterador) # O iterador não possui os valores visíveis diretamente; ele precisa ser convertido ou percorrido para gerar os valores reais.
# Saída: <map object at 0x...>


# Aqui, map(int, lista_de_strings) cria um iterador que aplica a função int a cada string na lista lista_de_strings. O resultado não é uma lista, mas um iterador.


# O que é um Iterador?
# Um iterador é um objeto que permite percorrer uma sequência de valores sem armazenar todos eles na memória. 
# Ele produz valores um de cada vez, à medida que são solicitados. 
# Isso é útil para trabalhar com grandes conjuntos de dados ou para economizar memória.