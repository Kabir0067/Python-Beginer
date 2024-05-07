def polygon_angles (num1):
    res=(num1-2)*180
    return f'Sum polygon ({num1}) ---> ({res})'

while True:
    a=int(input())
    print(polygon_angles(a))