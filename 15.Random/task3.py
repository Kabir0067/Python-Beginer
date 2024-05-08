def football (num1,num2,num3):
    result=(num1*3)+num2
    return f'Football points ({num1,num2,num3}) ---> ({result})'


while True:
    a=int(input())
    b=int(input())
    c=int(input())
    print(football(a,b,c))