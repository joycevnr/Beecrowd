# Lê a entrada do usuário
entrada = input()

# Separa a entrada em palavras, considerando múltiplos espaços
palavras = entrada.split()

# Inicializa o contador de palavras pentavogálicas
contador_pentavogalicas = 0

# Para cada palavra na lista de palavras
for palavra in palavras:
    # Inicializa uma lista para rastrear a presença de cada vogal
    presenca_vogais = [False] * 5  # [a, e, i, o, u]

    # Verifica cada letra da palavra
    for letra in palavra:
        if letra == 'a':
            presenca_vogais[0] = True
        elif letra == 'e':
            presenca_vogais[1] = True
        elif letra == 'i':
            presenca_vogais[2] = True
        elif letra == 'o':
            presenca_vogais[3] = True
        elif letra == 'u':
            presenca_vogais[4] = True

    # Verifica se todas as cinco vogais estão presentes
    if all(presenca_vogais):
        contador_pentavogalicas += 1

# Exibe a quantidade de palavras pentavogálicas
print(f'Quantidade de pentavogalicas: {contador_pentavogalicas}')
