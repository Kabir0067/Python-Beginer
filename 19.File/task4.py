cnt=0
my_list=[]
with open("file.txt","r") as file:
    for i in file:
        my_list.append(i)
    for j in my_list:
            cnt+=1
    print(f'Lens = {cnt} ')