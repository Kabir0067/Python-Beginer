def power(a, b):
    if b == 0:
        return 1
    else:
        return a**b 
    
a = float(input())
b = int(input())
result = power(a, b)
print(result)
