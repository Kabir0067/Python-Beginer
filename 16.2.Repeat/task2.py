my_list = input().split()
cnt=0
for i in range(1,len(my_list)):
    if int(my_list[i-1])<int(my_list[i]):
        cnt+=1
print(cnt)