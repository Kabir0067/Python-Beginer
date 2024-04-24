def find_min():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    m = a
    
    if b<m:
        m=b
    elif c<m:
        m=c
    elif d<m:
        m=d
    print(m)


find_min()