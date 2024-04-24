def xor(x, y):
    return (x or y) and not (x and y)
x = int(input())
y = int(input())
result = xor(x, y)

print(int(result))
