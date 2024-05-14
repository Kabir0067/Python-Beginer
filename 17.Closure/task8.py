def function(n):
    n_str=str(n)
    od_num='13579'
    for i in n_str:
        if i not in od_num:
            return False
        
    return True


print(function(1357))
print(function(1358))