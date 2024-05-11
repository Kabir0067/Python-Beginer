str1=input().split()
char=input()
list1=[]
cnt=0
for i in range(len(str1)):
    index=str(str1[i])
    for j in index:
        if j == char:
            cnt+=1
print(cnt)  