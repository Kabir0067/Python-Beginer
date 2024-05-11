def  determines (num1):
    s=7+5+1
    c=0
    while num1>0:
        i=num1%10
        c+=i
        num1=num1//10
    if c==s:
        return True
    else:
        return False
  
while True:  
    num=int(input())
    print(determines(num))   

