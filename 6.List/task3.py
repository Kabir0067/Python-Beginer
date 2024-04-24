My_List=input().split()
c=0
for i in range(0,len(My_List)):
    if int(My_List[i])>0:
        c+=1
print(c)