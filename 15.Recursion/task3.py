def sum_factorial (num1):
    summ=1
    for i in range(1,num1+1):
        summ*=i
    return summ
        
num=int(input())
res=0
for i in range(1,num+1):
    res+=sum_factorial(i)
print(res)