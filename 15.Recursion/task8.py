def sum_of_n_number(lst, num):
    summ = 0
    for i in range(num):
        summ += lst[i]
    return summ

lst = [9, 8, 7, 6]
num = 3
result = sum_of_n_number(lst, num)
print(result) 
