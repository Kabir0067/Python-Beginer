def ExpensivOrders(my_dict, number):
    new_dict = {}
    for k,v in my_dict.items():
        if v>number:
            new_dict[k] = v
    return new_dict
dict1 = {"a": 50, "b":100, "c": 450}
numb = 125
print(ExpensivOrders(dict1,numb))