k = int(input())
seq = input().split()

for i in range(len(seq) - 1):
    if int(seq[i]) + int(seq[i + 1]) == k:
        print(f"{seq[i]} {seq[i + 1]}") 