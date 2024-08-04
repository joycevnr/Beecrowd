#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for IMPAR, desconsidereo.

soma = 0
for i in range(6):
    num = int(input())
    if num % 2 == 0:
        soma += num
   
print(soma)

 #with sequence
 
# seq = []
# soma = 0
# for i in range(6):
#     num = int(input())
#     seq += [num] #seq.append(num)
#     if seq[i] % 2 == 0:
#         soma += num
   
# print(soma)