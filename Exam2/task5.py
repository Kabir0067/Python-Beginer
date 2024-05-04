list1 = input().split()
dict1 = {}
for i in list1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

maxx = max(dict1.values())

for i,c in dict1.items():
    if c == maxx:
        print(i)
        break