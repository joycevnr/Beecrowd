def multiplica_lista(n, lista):
    new_lista = []
    for i in range(n):
        new_lista += lista.copy()
    return new_lista
    


nomes = ['joao', 'pedro']
print(multiplica_lista(3, nomes))
#assert multiplica_lista(2, nomes) == ['joao', 'pedro', 'joao', 'pedro']

# # Multiplica Lista

# Python é uma linguagem que facilita muito a vida do programador. Uma dessas
# facilidades é a multiplicação de uma lista por um número inteiro N. Nesse caso,
# uma nova lista é produzida contendo N repetições dos elementos da lista
# original.  Por exemplo, 

# ```
# >> 2 * [2,3]
# >> [2, 3, 2, 3]
# ```

# Acontece que você não é um programador em Python. Você é um programador. Isso
# significa, entre outras coisas, que você deve entender e saber implementar essa
# ideia.

# Pede-se que você implemente a função `multiplica_lista(n,lista)` seguindo as
# especificações acima. Naturalmente, você não pode usar o operador de
# multiplicação. Além disso, a lista original deve manter-se inalterada após a
# chamada da função.

# Obs.: Lembre que se `N == 0`, uma lista vazia deve ser produzida.


# # Exemplo de uso da função

# ```
# nomes = ['joao', 'pedro']
# assert multiplica_lista(2, nomes) == ['joao', 'pedro', 'joao', 'pedro']
# ```

