def odd_integer(list1):
    cnt=0
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i] == list1[j]:
                cnt += 1
        if cnt % 2 != 0:
            return list1[i]


list1 = [1, 1, -2, 5, 5,4, 4, -1, -2, 0]
print(odd_integer(list1))
