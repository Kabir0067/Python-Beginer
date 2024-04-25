my_list=input().split()               # 0,1, 2,3, 4,5
j=0                                   # 1,0, 3,2  5,4
for i in range(0,len(my_list),2):
    j=my_list[i]
    my_list[i]=my_list[i+1]
    my_list[i+1]=j
print(my_list)