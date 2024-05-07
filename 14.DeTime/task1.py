def integer_in_minutes (num1):
    result=num1*60
    return f'Convert ({num1}) ---> ({result})'

while True:
    a=int(input())
    print(integer_in_minutes(a))
