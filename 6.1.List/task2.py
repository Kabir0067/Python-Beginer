my_list=input().split()
number=int(input())
res=[]
for i in range(1,number+1):
    for j in my_list:
        res.append(f'{j}{i}')
print(res)