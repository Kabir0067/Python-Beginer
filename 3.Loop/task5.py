a=int(input())
c=0
while a>0:
    i=a%10
    c+=i
    a=a//10
print(c)