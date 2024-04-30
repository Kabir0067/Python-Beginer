list1=[10,20,60,30,20,40,30,60,70,80]
list2=[]
for i in list1:
     if list1.count(i) > 1 and i not in list2:
        list2.append(i)
print(list2)
