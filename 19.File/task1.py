n = int(input())
with open("file.txt", "r") as file:
    lin = file.readlines()
    last_lin = lin[-n:]
for i in last_lin:
    print(i.strip())