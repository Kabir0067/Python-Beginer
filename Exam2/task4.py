list1 = [-1 ,2, 3, -1, -2,] 
for i in range(len(list1) - 1):
    if list1[i] * list1[i + 1] > 0:
        print(list1[i], list1[i + 1])
        break

