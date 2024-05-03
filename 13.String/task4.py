def palindrome (var):
    if var==var[::-1]:
       
        return 'Yes: given number is palindrome'
    else:
        
        return 'No: given number is not palindrome'
    
var=input()
print(palindrome(var))