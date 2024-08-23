while True:
    valor = input()
    
    if valor == 'fim':
        break

    if len(valor) != 8:
        print('Tente novamente.')
        continue
    
    # Verifica se a sequência pode ser separada em dois números válidos em BCD
    primeiro_digito = valor[:4]
    segundo_digito = valor[4:]
    
    try:
        # Convertendo os 4 primeiros bits e os 4 últimos bits para decimal
        digito_1 = int(primeiro_digito, 2)
        digito_2 = int(segundo_digito, 2)
        
        # Verifica se os valores convertidos estão entre 0 e 9 (números válidos em BCD)
        if digito_1 > 9 or digito_2 > 9:
            print('BCD inválido.')
        else:
            print(f'{digito_1}{digito_2}')
    except ValueError:
        print('BCD inválido.')

# # Binary Coded Decimal

# Escreva um programa que verifica se uma sequência de 8
# bits informada pelo usuário é um número válido no
# formato BCD (*Binary Coded Decimal*). Se a seqüência
# for um número em BCD, o valor
# decimal correspondente deve ser impresso.

# A representação BCD de um número
# decimal de dois algarimos requer apenas a justaposição
# da representação binária de cada algarismo no tamanho de
# 4 bits. Veja a tabela abaixo.

# ────────┬──────
#  digito │ BCD
# ────────┼──────
#       0 │ 0000
#       1 │ 0001
#       2 │ 0010
#       3 │ 0011
#       4 │ 0100
#       5 │ 0101
#       6 │ 0110
#       7 │ 0111
#       8 │ 1000
#       9 │ 1001
# ────────┴──────


# Por exemplo: Considere o  número decimal 23. Sabendo
# que a representação binária de 2 com 4 bits é 0010 e a
# de 3 é 0011. A representação em BCD de _23_ é dada por
# 00100011.

# Se o usuário informar uma sequência de 8 bits que
# corresponda a um número BCD válido, o programa deve informar
# o valor decimal correspondente ao número. Se o usuário
# informar uma sequência com 8 bits que não corresponda a um BCD
# válido, o programa deve informar BCD inválido.. Se a
# sequência informada pelo usuário tiver mais ou menos que 8
# bits, o programa deve apresentar ao usuário a mensagem Tente
# novamente..

# O programa só para de receber novas seqências quando o
# usuário informar a palavra fim na entrada. Para fins de
# simplicidade, considere que as sequências informadas pelos
# usuários são compostas exclusivamente por zeros e uns (a
# exceção, obviamente, é a da palavra "fim"). 

# DICA: A expressão int('11', 2) calcula o valor decimal da
# sequência de bits 11, na base 2. Teste!
