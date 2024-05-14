def function (x,n):
    for i in n:
        if i==x:
            return True
    return False


print(function("a",['a',1,2,3,'b']))
print(function("c",['a',1,2,3,'b']))

        