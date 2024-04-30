a=int(input())
for i in range(1,a+1,1):
    for j in range(a,i-1,-1):
        print(i, end=' ')
    print()