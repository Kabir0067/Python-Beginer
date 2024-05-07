def calc_age (year):
    res=year*365
    return f'Calc_age ({year}) ---> ({res})'

while True:
    a=int(input())  
    print(calc_age(a))