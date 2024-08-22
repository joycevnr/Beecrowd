contador_vogais = 0
contador_consoantes = 0
vogais = 'aeiou'
palavras = 1

while True:
    palavra = input().lower()
    for letra in palavra:
        if letra in vogais:
            contador_vogais += 1
        else:
            contador_consoantes += 1
    if contador_consoantes < contador_vogais:
        palavras += 1
    else:
        break

print(palavras)