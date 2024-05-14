def function(kalima,num):
    list1=[]

    for i in kalima:
        if len(i)>num:
            list1.append(i)
            res=" ".join(list1)

    return f"Filter long words ({kalima}, {num}) ---> {res}"


kalima=input().split()
num=int(input())
print(function(kalima,num))

