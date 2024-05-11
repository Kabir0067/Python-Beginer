from datetime import datetime,timedelta

day=datetime.strptime(input("bo in tarz dokhil kuned --->DD.MM.YY ---> "), "%d.%m.%Y")
panj_ruz_pesh=day-timedelta(days=5)
print(panj_ruz_pesh)



