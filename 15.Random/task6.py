def hours_min_to_sec (hours,minuts):
    res=((hours*60)+minuts)*60
    return f'Convert ({hours,minuts}) ---> ({res})'

while True:
    a=int(input())
    b=int(input())
    print(hours_min_to_sec(a,b))