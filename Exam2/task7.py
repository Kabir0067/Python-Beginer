my_list = [7, 6, 5, 4, 3, 2, 1]
k = int(input())
if k < 0 or k >= len(my_list):
    print()
else:
    for i in range(k + 1, len(my_list)):
        my_list[i - 1] = my_list[i]
    my_list.pop()
    print( my_list)