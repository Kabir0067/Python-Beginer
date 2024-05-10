def number_string_validation(elmn1,elmn2):
    if elmn1>= 0 and elmn2>=0:
        return str(elmn1) + str(elmn2)
    elif isinstance(elmn1, str) and isinstance(elmn2, str): 
        return  int(elmn1)+int(elmn2)
    else:
        return None


