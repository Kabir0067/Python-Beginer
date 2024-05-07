def increments (num1):
    res=num1+1
    return f'Adition ({num1}) ---> ({res})'

while True:
    a=int(input())
    print(increments(a))