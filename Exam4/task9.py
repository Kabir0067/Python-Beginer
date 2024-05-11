def power1(n, x):
    if x == 0:
        return 1
    elif x < 0:
        return 1 / power1(n, -x)
    else:
        return n * power1(n, x - 1)
 
n=int(input())
x=int(input())
print(power1(n,x))
    


