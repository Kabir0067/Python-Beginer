def sum_odd_and_even(num_list):
    sum_odd,sum_even = 0,0
    for i in num_list:
        if int(i)%2 == 0:
            sum_odd += int(i)
        else:
            sum_even +=int(i) 
    my_list=[sum_odd,sum_even]
    return f'Sum odd and even ({num_list}) ---> {my_list}'


my_list=input().split()
print(sum_odd_and_even(my_list))