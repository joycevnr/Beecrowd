def soma_polinomios(p1, p2):
    # Cria uma lista para o resultado com zeros
    maior = len(p1) if len(p1) > len(p2) else len(p2)
    resultado = [0] * maior
    
    p1 = [0] * (maior - len(p1)) + p1
    p2 = [0] * (maior - len(p2)) + p2

    for i in range(len(resultado)-1, -1, -1):
        resultado[i] += p1[i]

        resultado[i] += p2[i]
    return resultado

# Testes
p1 = [3, 4, -5]
p2 = [5, 0, 0, 0, 2, 0, -1]
print(soma_polinomios(p1, p2))
assert soma_polinomios(p1, p2) == [5, 0, 0, 0, 5, 4, -6]

# Soma Polinômios

# Um software matemático representa polinômios de uma única
# variável através de listas que contêm os coeficientes em ordem
# decrescente de grau. Por exemplo, o polinômio 

# <img height="40px" src="https://latex.codecogs.com/gif.latex?\dpi{200}p_1(x)%20=%203x^2%20%2B%204x%20-%205">

# é representado pela lista `[3, 4, -5]`, indicando que os
# coeficientes dos monômios de grau 2, 1 e 0 são, respectivamente,
# 3, 4 e -5. De forma análoga, a lista `[5, 0, 0, 0, 2, 0, -1]` representa o polinômio

# <img height="40px" src="https://latex.codecogs.com/gif.latex?\dpi{200}p_2(x)%20=%205x^6%20%2B%202x^2%20-%201">

# Observe que os vários zeros na lista correspondem aos
# coeficientes de grau 5, 4, 3 e 1 que não precisamos expressar
# explicitamente na escrita matemática.

# Pede-se que você escreva a função `soma_polinomios(p1, p2)` que
# não tenha efeito colateral e que retorne o polinômio soma dos
# polinômios `p1` e `p2`.

# Relembre que a soma de dois polinômios é
# um polinômio cujos coeficientes são dados pela soma dos
# coeficientes de mesmo grau dos polinômios sendo somados. 

# <img src="http://www.dsc.ufcg.edu.br/~dalton/dropbox/images/soma_polinomios.png" alt="soma polinomios" width="200">
