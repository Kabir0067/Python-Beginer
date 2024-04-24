a=int(input())   
b=int(input())
c=0   #hisobkunak
while a>0:  #a to vaqte ki az 0 kalon aast
     i=a%10     #i baroi raqami oxirona giriftan
     if i==b:    #agar oxinron raqami giriftashuda == raqami doda shuda boshad 
         c+=1    #yakto yakto hisob kunad
     a=a//10      #baroi raqami oxironro udalit kardan
print(c)     #raqami hisobkardaro chop mekunem
