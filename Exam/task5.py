def palindrom(i):
    i = str(i) 
    return i == i[::-1]

a=int(input())
print(palindrom(a))