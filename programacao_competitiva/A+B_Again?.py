# qtd = int(input())
# somas = []
# if 1 <= int(qtd) <= 90:
#     for i in range(qtd):
#         valores = input()
#         if 10 <= int(valores) <= 99:
#             soma = int(valores[0]) + int(valores[1])
#             somas.append(soma)
#         else:
#             break

# for i in range(len(somas)):
#     print(somas[i])

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    digit_sum = (n // 10) + (n % 10)
    print(digit_sum)
