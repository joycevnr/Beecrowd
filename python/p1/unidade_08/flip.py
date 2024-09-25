def flip(array, iini, ifim):
    while ifim > iini:
        array[iini], array[ifim] = array[ifim], array[iini]
        ifim -= 1
        iini += 1
        
a = [10, 20, 30, 40, 50, 60]
flip(a, 2, 4)
assert a == [10, 20, 50, 40, 30, 60]
##for i in range(inicio, inicio+((abs(inicio-fim)/2)):