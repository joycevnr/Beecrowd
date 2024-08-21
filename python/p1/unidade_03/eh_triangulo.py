lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

cond1 = (lado1 + lado2 > lado3) and (lado1 - lado2 < lado3)
cond2 = (lado1 + lado3 > lado2) and (lado1 - lado3 < lado2)
cond3 = (lado2 + lado3 > lado1) and (lado2 - lado3 < lado1)

if cond1 and cond2 and cond3:
    perimetro = lado1 + lado2 + lado3
    print(f"triangulo valido. {perimetro}")
else:
    print("triangulo invalido.")


"""
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

# Verifique as condições para ser um triângulo válido
#A função abs() é usada para obter o valor absoluto/não-negativo de um número.
cond1 = (lado1 + lado2 > lado3) and (abs(lado1 - lado2) < lado3)
cond2 = (lado1 + lado3 > lado2) and (abs(lado1 - lado3) < lado2)
cond3 = (lado2 + lado3 > lado1) and (abs(lado2 - lado3) < lado1)

if cond1 and cond2 and cond3:
    perimetro = lado1 + lado2 + lado3
    print(f"triangulo valido. {perimetro}")
else:
    print("triangulo invalido.")

"""