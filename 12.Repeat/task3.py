my_list=[11,45,8,11,23,45,23,45,89]
cnt={}
for i in my_list:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
for k,v in cnt.items():
    print(cnt)
    break