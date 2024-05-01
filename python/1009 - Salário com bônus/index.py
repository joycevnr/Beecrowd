name = type(input())
fixed_salary = float(input())
sales = float(input())

salary = fixed_salary +  (sales * 15 / 100 )

print(f'TOTAL = R$ {salary:.2f}')