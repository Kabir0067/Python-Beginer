from datetime import datetime,timedelta
def creat(date):
    date1=datetime.strptime(date,'%d/%m/%Y')
    return date1.strftime('%Y%m%d')

date=input("Bo in tarz dokhil kuned DD/MM/YYYY ---->")
print(creat(date))