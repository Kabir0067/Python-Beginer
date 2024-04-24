def fibonachi(n):
    a = [0, 1]
    while len(a) < n:
        a.append(a[-1] + a[-2])
    return a

n = int(input())
result = fibonachi(n)
print(result)
