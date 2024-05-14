def occuren(start, end, digit):
    cnt=0
    while start<=end:
        number=start
        while number>0:
            if number%10==digit:
                cnt+=1
            number//=10
        start+=1
    return cnt

start, end, digit = int(input()),int(input()),int(input())
print(occuren(start, end, digit))