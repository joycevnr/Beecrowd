def rotdir(array):
    if len(array) != 0:
        ult = array[-1]
        for i in range(len(array)-1, -1, -1):
            array[i] = array[i-1]
        array[0] = ult
        print(array)
    
valores = []
rotdir(valores)
assert valores == []

valores = [10]
rotdir(valores)
assert valores == [10]

valores = [10, 20]
rotdir(valores)
assert valores == [20, 10]

valores = [10, 20, 14, 17, 22, 9, 32]
rotdir(valores)
assert valores == [32, 10, 20, 14, 17, 22, 9]
