from datetime import datetime,timedelta

day=datetime.strptime(input("bo in tarz dokhil kuned --->DD.MM.YY ---> "), "%d.%m.%Y")

pareruz=day-timedelta(days=2)
fardo=day+timedelta(days=2)
print(pareruz,"\n",day,"\n",fardo)



