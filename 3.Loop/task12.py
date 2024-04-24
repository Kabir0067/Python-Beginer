a=int(input())
z,n,p,k=0,0,0,0
while k<a:
    num=int(input())
    if num == 0:
        z += 1
    elif num < 0:
        n += 1
    else:
        p += 1
    k+=1   
print(z,p,n)