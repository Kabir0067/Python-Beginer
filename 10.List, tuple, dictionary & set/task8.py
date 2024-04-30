list1 = [12, 75, 150, 180, 145, 525, 50]
for i in list1:
    if i > 500:
        break 
    elif i > 150:
        continue 
    elif i % 5 == 0:
        print(i) 
