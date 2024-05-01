list1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
new_list1 = []
new_list2 = []
for i in list1:
    if i != 0:
        new_list1.append(i)
for j in list1:
    if j == 0:
        new_list2.append(j)
        res=new_list1+new_list2
print(res)