a = int(input())
s,k = 0,0
for i in range(1,a+1):
    if a % i == 0:
        s += i
        k += 1
print(k,' ',s)
