import random

def khorijkunii_satr(a):
    with open("file.txt","r") as my_file:
        for i in range(a -1):
            my_file.readline()
        line=my_file.readline().strip()
        return line.split()
    
mevagi=khorijkunii_satr(1)
moshin=khorijkunii_satr(2)
sabzavot=khorijkunii_satr(3)


guruh_dict={
    "mevagiho meboshad:":mevagi,
    "nomi moshinho meboshad:":moshin,
    "sabzavotho meboshad:":sabzavot
}

random_guruhho=random.choice(list(guruh_dict.keys()))
random_kalima=random.choice(guruh_dict[random_guruhho])

alomat= ["_"]*len(random_kalima)
kalima=" ".join(alomat)
khod=4
harfi_istifodashuda=[]


print('-'*50)
print(f"Kalima az guruhi {random_guruhho}")
print(f"Kalimaro yobed -->  {kalima}")
print('-'*50)

for i in range(khod):
    if "_" not in alomat:
        print("Tabrik! Shumo kalimao yofted")
        break
    harf=input("Harfro dokhil kuned --->  ").lower()
    
    if harf in harfi_istifodashuda:
        print("In hatf alakay hast lutfan harfi digarro dokhil kuned")
        continue
    
    harfi_istifodashuda.append(harf)
    
    if harf in random_kalima:
        for i, elemt in enumerate(random_kalima):
            if elemt==harf:
                alomat[i]=harf
        print("."*70)
        print(f"harf intikhobkardai shumo  {' '.join(alomat)}  durust ast!")
        print("."*70)
    else:
        print(f"Ishtiboh! SHUMO ({khod-i-1}) sahsi digar dored")
                
else:
    print(f"SHUMO BOY DODED! Kalima in bud {random_kalima} ")