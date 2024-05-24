valor = float(input())
saldo = 0
if valor > 0:
  saldo += valor
  print(f"Deposito realizado com sucesso!")
  print(f"Saldo atual: R$ {saldo:.2f}")
elif valor < 0:
  print(f"Valor invalido! Digite um valor maior que zero.")
else:
   print(f"Encerrando o programa...")