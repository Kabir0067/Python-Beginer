def corona(num1,num2,num3):
    cnt=0
    for i in range(1,num1+1):
        res=num1-num2
        num3-=res
        cnt+=1
        if num3<=0:
            break
    return cnt

a=int(input())
b=int(input())
c=int(input())
print(corona(a,b,c))