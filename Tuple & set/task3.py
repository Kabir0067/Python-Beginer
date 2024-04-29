list1=input().split()
list2=input().split()
new_list=[]
for i in list1:
  for j in list2:
      new_list.append(i)
      new_list.append(j)
print(new_list)