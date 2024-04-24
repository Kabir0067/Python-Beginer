My_List=input().split()
for i in range(0,len(My_List)):
    if int(My_List[i]>My_List[i-1]):
        print(My_List[i], end=" ")