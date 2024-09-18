def adicionar_elemento_posicao(lista, posicao, elemento):
    nova_lista = []
    for i in range(len(lista) + 1):
        if i == posicao:
            nova_lista.append(elemento)
        if i < len(lista):
            nova_lista.append(lista[i])
    return nova_lista


def insere_nome(aluno1, duplas, aluno2):
    posicao = None
    for i in range(len(duplas)):
        if duplas[i] == aluno2:
            posicao = i
            break

    if posicao is not None:
        duplas[:] = adicionar_elemento_posicao(duplas, posicao, aluno1)
    else:
        duplas.append(aluno1)
    

duplas = ['joel', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('gil', duplas, 'juliano') == None
assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('marta', duplas, 'vera') == None
assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta']

# # Organizando as Duplas do Projeto

# O projeto em duplas é uma das principais atividades da disciplina
# de Programação 1. Para fazer o projeto, o aluno precisa
# ter passado da unidade 6 (a disciplina é dividida em 10
# unidades). Como a disciplina de Programação 1 adota a
# idéia de que cada aluno avance no seu ritmo, é comum que
# a permissão para cada aluno fazer o projeto se dê em momentos
# diferentes. Alguns, portanto, só definem suas duplas 
# tardiamente.

# Para tentar organizar as duplas, os professores da disciplina
# mantem uma lista de alunos organizada de tal forma que quando o
# prazo final da definição das duplas é alcançado, todas as
# duplas estão em posições adjacentes desta lista. A idéia
# é inserir de forma organizada. Quando um novo aluno se torna 
# apto a fazer o projeto, ele indica quem é seu companheiro de
# dupla e seu nome é inserido na lista imediatamente antes do
# nome do seu companheiro. Caso o seu parceiro da dupla ainda não
# esteja apto ao projeto e, portanto, seu nome não está na lista,
# o novo aluno é inserido no final da lista.

# Escreva a função `insere_nome(aluno1, duplas, aluno2)`
# que inscreve o `aluno1` na lista `duplas`,
# tendo como parceiro o `aluno2`. A função não retorna
# nada, apenas atualiza o conteúdo da lista `duplas`.

# ## Atenção

# Não é permitido usar funções de ordenação disponíveis em Python e nem implementar
# nenhum algoritmo de ordenação conhecido. Não é permitido também usar insert(). 
# Adicionar elemento apenas com append().
