list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 = []
list4=[]
list5=[]
for i in range(1,len(list1),2):
    list3.append(list1[i])
    list5.append(list1[i])
for j in range(0,len(list2),2):
    list4.append(list2[j])
    list5.append(list2[j])
print(f'Element at odd-index positions from list one \n {list3}')
print(f'Element at even-index positions from list two\n {list4}')
print(f'Printing Final third list\n {list5}')



    