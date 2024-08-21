ano_atual = int(input("Ano atual? "))
ano_nascimento = int(input("Ano de nascimento? "))
idade = ano_atual - ano_nascimento

print(f"Idade calculada: {idade} anos")

if idade == 14 or idade == 15:
    pais  = str(input("Com os pais? "))

if idade >= 16:
    print("Entrada permitida")  
elif idade < 16 and idade >= 14:
   print("Entrada proibida para menores de 16 anos sem os pais")
else:
   print("Entrada proibida para menores de 14 anos")


