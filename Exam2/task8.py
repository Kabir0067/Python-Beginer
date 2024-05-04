lst = [1, 2, 2, 3, 3, 3]

list_new = []
for i in lst:
    if i not in list_new:
        list_new.append(i)

print(len(list_new)) 

