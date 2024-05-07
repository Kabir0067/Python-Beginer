from datetime import datetime
def  strftime2 (data):
    input_data = datetime.strptime(data, '%d/%m/%Y')
    output_data = input_data.strftime('%Y%m%d')
    return f'Format date({data}) ---> ({output_data})'


print("Бо ин тарз дохил кунед 11/12/2024")
input_data=input()
print(strftime2(input_data))


