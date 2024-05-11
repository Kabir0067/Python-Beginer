def reversed_str(string1):
    # if len(string1)==0:
    #     return string1
    # else:
    #     return reversed_str(string1[:1]+string1[0])
    str1=string1[::-1]
    return str1
    
a=input()
print(reversed_str(a))