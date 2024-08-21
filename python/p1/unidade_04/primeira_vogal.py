# Lê a palavra da entrada do usuário
palavra = input("")

vogais = "aeiouAEIOU"
resultado = "-"

for letra in palavra:
    if letra in vogais:
        resultado = letra
        break  

print(resultado)


# def primeira_vogal(palavra):
#     vogais = "aeiouAEIOU"
#     for letra in palavra:
#         if letra in vogais:
#             return letra
#     return "-"


# palavra = input()

# print(primeira_vogal(palavra))
