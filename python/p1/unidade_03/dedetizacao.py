servico = input().upper()

if servico == 'M' or servico == 'T':
    area = float(input())

if servico == 'M':
    total = 1.50 * area
elif servico == 'T':
    total = 1.80 * area
elif servico == 'R':
    total = 30.00

print(f"R$ {total:.2f}")
if total >= 300:
    print('* Inclui ralos')

