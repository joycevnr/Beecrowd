def filas_de_atendimento(pacientes, num_medicos):
    # Cria uma lista de listas para armazenar as filas dos médicos
    filas = [[] for _ in range(num_medicos)]
    
    # Inicializa o índice do médico
    medico_index = 0
    
    # Distribui os pacientes nas filas dos médicos
    for paciente in pacientes:
        filas[medico_index].append(paciente)
        medico_index = (medico_index + 1) % num_medicos  # Move para o próximo médico
    
    return filas


pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
assert filas_de_atendimento(pacientes, 3) == [
    ['Andre', 'Carlos'],
    ['Antonio', 'Claudia'],
    ['Bianca']
]

pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos']
assert filas_de_atendimento(pacientes, 2) == [
    ['Andre', 'Bianca'],
    ['Antonio', 'Carlos']
]

# # % num_medicos: Garante que o índice se mantenha dentro do intervalo válido de filas, retornando ao início quando necessário.
# Exemplo:

# Suponha que há 3 médicos e o medico_index atual é 2 (o terceiro médico).
# Passo 1: Incrementa o índice: 2 + 1 resulta em 3.
# Passo 2: Aplica o módulo: 3 % 3 resulta em 0.
# O resultado 0 faz com que o índice volte ao início da lista de médicos, permitindo a distribuição cíclica.