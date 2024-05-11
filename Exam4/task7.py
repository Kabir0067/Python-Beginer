def to_list(dict1):
    result = []
    for key, value in dict1.items():
        result.append([key, value])
    return result

my_dict={ "a": 1, "b": 2 }

print(to_list(my_dict))