def sum_five(list1):
    num=0
    for i in list1:
        if i>5:
            num+=i
    return num

a=input().split()
b=list(map(int,a))
print(sum_five(b))