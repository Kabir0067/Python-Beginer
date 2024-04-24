def pow():
    a = float(input())
    n = int(input())
    if n < 0:
        return False
    else:
        return a ** n

g = float(input())
f = int(input())
result = pow(g, f)
print(result)
