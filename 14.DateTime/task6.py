def remainder (num1,num2):
    res=num1%num2
    return f'remainder ({num1},{num2}) ---> ({res})'

while True:
    a=int(input())
    b=int(input())
    print(remainder(a,b))