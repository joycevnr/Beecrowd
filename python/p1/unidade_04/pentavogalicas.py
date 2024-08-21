entrada = input().lower()
palavras = entrada.split()
contador_pentavogalicas = 0

# Para cada palavra na lista de palavras
for palavra in palavras:
    # Inicializa variáveis booleanas para verificar a presença de cada vogal
    tem_a = tem_e = tem_i = tem_o = tem_u = False

    # Verifica cada letra da palavra
    for letra in palavra:
        if letra == 'a':
            tem_a = True
        elif letra == 'e':
            tem_e = True
        elif letra == 'i':
            tem_i = True
        elif letra == 'o':
            tem_o = True
        elif letra == 'u':
            tem_u = True

    # Verifica se todas as cinco vogais estão presentes
    if tem_a and tem_e and tem_i and tem_o and tem_u:
        contador_pentavogalicas += 1

print(f'Quantidade de pentavogalicas: {contador_pentavogalicas}')
