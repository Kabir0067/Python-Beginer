num=int(input())
a=0
while num>0:
    res=num%10
    a=a*10+res
    print(res,end=' ')
    num=num//10

