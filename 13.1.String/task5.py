string1='I am 25 years and 10 months old'
str_numbers=''
for i in string1:
    if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
        str_numbers+=i
print(str_numbers)