def ajusta_prioridades(fila):
    sem_prioridade, com_prioridade = [], []
    for paciente in fila:
        ult = paciente % 10
        if ult >= 6:
            sem_prioridade.append(paciente)
            #fila.pop(i]) --  o tamanho da lista é reduzido, o que faz com que o próximo índice no loop possa acessar um elemento incorreto ou até mesmo causar um IndexError se o índice estiver fora dos limites da lista.
        else:
            com_prioridade.append(paciente)
            
    fila[:] = com_prioridade + sem_prioridade
    # fila.clear() 
    # fila.extend(com_prioridade + sem_prioridade)

    
    #fila[:]: Usamos fila[:] para modificar a lista original diretamente. Isso é importante
    # se colocar fila = ... estou criando uma  nova lista e atribuindo-a à variável fila, mas isso não altera a lista original.
    
    #  Limpa a lista original e adiciona os elementos na nova ordem
    # fila.clear()  # Remove todos os elementos da lista original
    # fila.extend(com_prioridade + sem_prioridade)  # Adiciona os novos elementos


##Pop e remove
#O método pop() remove e retorna o elemento da lista na posição especificada pelo índice. Se nenhum índice for fornecido, ele remove e retorna o último elemento da lista.

# O método remove() remove a primeira ocorrência do valor especificado na lista. Se o valor não estiver presente na lista, ocorrerá um erro ValueError.

fila = [327, 228, 516, 535, 248, 532]
assert ajusta_prioridades(fila) is None
assert fila == [535, 532, 327, 228, 516, 248]

#O operador de módulo retorna o resto da divisão de um número por outro, e quando usado com 10, ele fornece o último dígito de um número decimal.


# # Atendimento prioritário

# Uma clínica médica atende seus pacientes por ordem de chegada e,
# em alguns casos, por ordem de prioridade. Para simplificar,
# contudo, tem apenas dois níveis de prioridade. Quando o paciente
# chega, ele informa seu problema em linhas gerais à recepção e
# recebe um código único que codifica várias informações, além da
# prioridade com que deve ser atendido. A prioridade é fácil de
# decodificar e se resume a atender com maior prioridade todo
# paciente cujo código termine em um dígito menor que 6.

# Por exemplo, suponha que inicialmente chegam 3 pessoas na clínica
# e que recebam, respectivamente, os códigos 327, 228 e 516. Como
# nenhum dos três números termina em um dígito menor que 6, então
# podemos concluir que nenhum deles foi considerado prioritário.
# Assim, se somente eles estivessem na clínica, deveriam ser
# atendidos de acordo com a ordem de chegada:

# ```
# 327 228 516
# ```

# Assuma, contudo, que outros 3 pacientes cheguem à clínica antes
# dos atendimentos serem iniciados e que recebam os códigos: 535,
# 248, 532, respectivamente. Observe que os dígitos finais dos
# códigos do primeiro e do terceiro paciente são menores que 6 e
# que, portanto, ambos são prioritários. O segundo paciente, por
# outro lado, não é prioritário, como se pode deduzir pelo código
# que recebeu que não termina em um dígito abaixo de 6. Assim,
# pelas regras estabelecidas, se esses forem os pacientes no
# momento que forem iniciados os atendimentos, a ordem de
# atendimento, pelos códigos, será:

# ```
# 535 532 327 228 516 248
# ```

# Observe que todos os pacientes prioritários devem ser atendidos
# antes dos pacientes não prioritários. Por outro lado, a ordem
# relativa de atendimento entre eles e entre os pacientes sem
# prioridade deve ser a ordem de chegada. Assim, o paciente 532
# será atendido depois do paciente 535 porque, embora ambos sejam
# prioritários, o paciente 535 chegou antes do paciente 532.

# Pede-se que você implemente a função `ajusta_prioridades(fila)`
# que, dada uma lista com códigos de pacientes na ordem em que
# chegaram, _altere_ a lista de forma que os códigos sejam
# colocados na ordem de prioridade estabelecida pela regra. Por ser
# de efeito colateral, a função não deve retornar nada.


# ## Exemplos de uso da função

# Os _asserts_ abaixo usam os mesmos dados do exemplo acima.

# ```python
# fila = [327, 228, 516, 535, 248, 532]
# assert ajusta_prioridades(fila) is None
# assert fila == [535, 532, 327, 228, 516, 248]
# ```
 
# Este é um segundo exemplo.

# ```python
# fila = [219, 638, 263, 621, 482, 616]
# assert ajusta_prioridades(fila) is None
# assert fila == [263, 621, 482, 219, 638, 616]
# ```

