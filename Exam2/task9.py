qad = [165, 163,160, 160, 157, 157, 155, 154]
b = int(input())
a = 1
for i in qad:
    if i >= b:
         a += 1
    else:
       break
print(a)