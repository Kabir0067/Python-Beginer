def animals_foot (chickens,cows,pigs):
    res1=chickens*2
    res2=(cows*4)+(pigs*4)
    resultat=res1+res2
    return f"Animals ({chickens,cows,pigs}) ---> ({resultat})"

while True:
    a=int(input())
    b=int(input())
    c=int(input())
    print(animals_foot(a,b,c))