list1 = input().split()      
list2 = input().split()      
new = []
for i in range(len(list1)):
    new.append(list1[i] + list2[i])
print(new)