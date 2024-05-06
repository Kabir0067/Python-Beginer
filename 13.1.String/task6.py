string1='/*Jon is @developer & musician!!'
a='#'
str2=''
for i in  string1:
    if i=='@' or i=='#' or i=='$' or i=='%' or i=='&' or i=='*' or i=='/' or i=='!':
        str2+=a
    else:
       str2+=i 
print(str2)

