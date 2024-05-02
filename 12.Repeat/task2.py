my_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
new_list = len(my_list) // 3
list1 = []

for i in range(0, len(my_list), new_list):
    res = my_list[i:i + new_list]
    list1.append(res)

for res in list1:
    print("Chuk ", res) 
    print("After reversing:", res[::-1]) 
    print()
