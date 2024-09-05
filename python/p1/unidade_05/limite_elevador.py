def peso(razao_maxima):
    total_pessoas = 0
    total_peso = 0.0
    num_adultos = 0
    num_criancas = 0

    while True:
        tipo, peso_str = input().split()
        peso = float(peso_str)

        # Se for adulto
        if tipo == 'a':
            num_adultos += 1
        elif tipo == 'c':  # Se for criança
            num_criancas += 1

        if num_adultos > 0:
            nova_razao = num_criancas / num_adultos

        if num_adultos == 0:
            break
        #coloca a verificaçaõ antes para aí add ou não no peso total e pessoa
        if nova_razao > razao_maxima or (total_peso + peso) > 700.00:
            break
        
        total_pessoas += 1
        total_peso += peso

    print('Limite atingido.')
    print(f'Elevador saiu com {total_pessoas} pessoas e {total_peso:.2f} kg.')

def main():
    razao_maxima = float(input())
    peso(razao_maxima)

if __name__ == "__main__":
    main()