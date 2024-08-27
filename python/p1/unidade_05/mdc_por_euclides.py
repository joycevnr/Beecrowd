menor = float(input())
maior = float(input())

while menor != 0:
    resto = maior % menor
    maior = menor
    menor = resto


print(f"{maior:.0f}")
