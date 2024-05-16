my_list=[]
with open("file.txt",'r') as file:
    lin_index=file.readlines()
    for i in range(len(lin_index)):
        my_list.append(lin_index[i])
    print(my_list)