import random
txt='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890/_@#$%'
len_password = int(input())
pasword=''.join(random.sample(txt,len_password))
print(pasword)
    



   


