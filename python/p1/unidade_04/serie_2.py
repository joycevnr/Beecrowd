for i in range(152, -59, -15):
    print(i/10)







# for (i = 15.2; i >= -7.3; i-= 1.5){
#     console.log(i.toFixed(1))
# }

n = 16.7

while n >= -5.8:
   n -= 1.5
   print(f"{n:.1f}")

# com recursão
def sequencia(num):
    if num >= -5.8:
       num -= 1.5
       print(f"{num:.1f}")
       sequencia(num)

num = 16.7
sequencia(num)
