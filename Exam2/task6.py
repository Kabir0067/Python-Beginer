lst = [1, 2, 2, 3, 3, 3] 
my_dict = {}
for num in lst:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1

for num in lst:
    if my_dict[num] == 1:
        print(num)