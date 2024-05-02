my_dict = {'jan': 47, 'feb': 52, 'march': 47, 'april': 44, 'may': 52, 'june': 53, 'july': 54}
my_list=[]
for i in my_dict.values():
    if my_dict.values==i:
        del i
    my_list.append(my_dict.copy())
print(list(my_dict.values()))
