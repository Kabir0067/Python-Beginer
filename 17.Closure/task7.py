def function (list1):
    if len(list1)<=1:
        return True
    for i in range(1,len(list1)):
        if list1[i]<=list1[i-1]:
            return False
    return True


list1=[1,2,3,4,5,6]
list2=[1,2,3,4,2,3]
print(function(list1))
print(function(list2))

