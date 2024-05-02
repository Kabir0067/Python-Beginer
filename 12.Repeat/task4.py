my_list = [47, 64, 69, 37, 76, 83, 95, 97]
my_dict = {'John': 47, 'Emma': 69, 'Kelley': 76, 'Jason': 97}
new_list = []

for i in my_list:
    for j in my_dict.values():
        if j == i:
            new_list.append(j)

print(new_list)
