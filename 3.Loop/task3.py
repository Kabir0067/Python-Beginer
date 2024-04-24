import math
a=int(input())
b=int(input())
while a<=b:
    k=math.sqrt(a)
    if k==int(k):
        print(a)
    a+=1 
    