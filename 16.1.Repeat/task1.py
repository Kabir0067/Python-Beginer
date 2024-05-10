def formating (my_string):
    res_str=(my_string[0:2]+'...' ' ') *2 + " "+ my_string+'?'
    return f'Stutter ({my_string}) ---> "{res_str}"'


a="incredible"
print(formating(a))