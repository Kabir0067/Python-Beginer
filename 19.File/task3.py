with open("file.txt", "r") as file:
    my_list = file.read().split()
max_word = my_list[0]  
for i in my_list:
    if len(i) > len(max_word): 
        max_word = i  

print(max_word)
