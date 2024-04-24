My_List=input().split()
for i in range(0,len(My_List)):
    if int(My_List[i])*int(My_List[i+1])>0:
        print(My_List[i],My_List[i+1])
        break