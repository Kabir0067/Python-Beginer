def convert_hours(hours):
    second=hours*3600
    return f'How_many_seconds ({hours}) ---> ({second})'

while True:
    a=int(input())
    print(convert_hours(a))