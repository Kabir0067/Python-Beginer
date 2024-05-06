string1 = "Emma-is-a-date-scientist"
string2 = ""
for i in string1:
    if i == "-":
        print(string2)  
        string2 = "" 
    else:
        string2 += i  
print(string2)
