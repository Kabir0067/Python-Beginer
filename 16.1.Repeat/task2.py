def foiz(num1,num2):
    res=num1-((num2/100)*num1)
    return f'Dis ({num1,num2}) ---> ({res})'

while True:
    a=int(input())
    b=int(input())
    print(foiz(a,b))