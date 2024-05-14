my_list = input().split()
new_list = []
n = "*"
for i in range(len(my_list)):
    if len(my_list[i])>4:
        new_list.append(n*len(my_list[i]))
    else:
        new_list.append(my_list[i])
print(" ".join(new_list))