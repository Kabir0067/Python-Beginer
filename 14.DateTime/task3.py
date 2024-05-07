def cubes (num1):
    result=num1*num1*num1
    return f'Cubes ({num1}) ---> ({result})'

while True:
    a=int(input())
    print(cubes(a))