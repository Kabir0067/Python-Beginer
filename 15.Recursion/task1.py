list1 = [1, 2, [3, 4], 5, 6]
suma = 0
for i in list1:
    if isinstance(i, list):
        for j in i:
            suma += j
    else:
        suma += i
print(suma)


