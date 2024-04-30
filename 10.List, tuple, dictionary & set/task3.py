list1=[10,20,30,40,50,60,70,80,90,100]
new_list=[]
for i in range(len(list1)):
    if list1[i]<=50:
        new_list.append(list1[i])
print(new_list)