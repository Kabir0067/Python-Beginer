string1='/*Jon is @developer & musician'
string2=''
for i in string1:
    if i=='@' or i=='#' or i=='$' or i=='%' or i=='&' or i=='*' or i=='/':
        print(string2,end='')
        string2=""
    else:
       string2+=i
print(string2,end="")        


