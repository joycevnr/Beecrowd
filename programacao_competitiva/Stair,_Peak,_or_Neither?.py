qtd = int(input())

for i in range(qtd):
    valores = input().split()
    if valores[0] < valores[1] < valores[2]:
        print('STAIR')
    elif valores[0] < valores[1] > valores[2]:
        print('PEAK')
    else:
        print('NONE')


# # Read the number of test cases
# qtd = int(input())

# # Iterate through each test case
# for _ in range(qtd):
#     # Read and split the input values
#     valores = list(map(int, input().split()))
    
#     # Extract values
#     a, b, c = valores
    
#     # Determine if it is a stair, peak, or neither
#     if a < b < c:
#         print('STAIR')
#     elif a < b > c:
#         print('PEAK')
#     else:
#         print('NONE')