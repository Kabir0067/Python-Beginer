def string(list1,str1):
    ind=-1
    for i in range(len(list1)):
        if list1[i]==str1:
            ind=i
            break
    return ind


a=input().split()
b=input()
print(string(a,b))

