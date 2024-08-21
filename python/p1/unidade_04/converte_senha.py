palavra = input("")
nova_palavra = palavra[0]
trocas = 0

for letra in palavra[1:]:
    if letra  == 'a' or letra == 'A':
        nova_palavra += '4'
        trocas += 1
    elif letra  == 'e' or letra == 'E':
        nova_palavra += '3'
        trocas += 1
    elif letra  == 'i' or letra == 'I':
        nova_palavra += '1'
        trocas += 1
    elif letra  == 'o' or letra == 'O':
        nova_palavra += '0'
        trocas += 1
    else:
        nova_palavra += letra


print(f"{nova_palavra} ({trocas} troca(s))")
