a=int(input())
b=int(input())
c=int(input())
if a<=b and b<=c:
    print(a,b,c) 
elif b<=a and a<=c:
    print(b,a,c) 
elif c<=a and a<=b:
    print(c,a,b) 
elif c<=b and b<=a:
    print(c,b,a)
elif a<=c and c<=b:
    print(a,c,b)
else:
    print(b,c,a)
    