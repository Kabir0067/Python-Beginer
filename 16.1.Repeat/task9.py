def get_index(list1,number):
    list2=[]
    for i in range(len(list1)):
        if list1[i]==number:
            list2.append(i)
    return list2

list1=input().split()
list2=list(map(int,list1))
num=int(input())
print(get_index(list2,num))
