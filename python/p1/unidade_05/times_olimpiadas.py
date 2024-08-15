import sys
jogadores = []

while True:
    try:
        jogador = input()
        if jogador == '-':
            break
        jogadores.append(jogador)
    except:
        sys.exit(1)

if len(jogadores) == 11:
    print("Modalidade -> Futebol")
elif len(jogadores) == 5:
    print("Modalidade -> Basquete")
elif len(jogadores) == 6:
    print("Modalidade -> Vôlei")
elif len(jogadores) == 7:
    print("Modalidade -> Handebol")
else:
    print("Equipe Inválida")
