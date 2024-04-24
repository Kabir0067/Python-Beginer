# Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
# Входные данные
# Программа получает на вход три числа: a, b, n.    10   15  2  ooo 20   30

rubley=int(input())
kopeka=int(input())
pirojki=int(input())
a=rubley*100+kopeka
b=a*pirojki
c=b//100
f=b%100
print(c, f)