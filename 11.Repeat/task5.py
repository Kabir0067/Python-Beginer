list1=[1,2,3]
list2=[4,5,6]
list3=[10,11,12]
list4=[7,8,9]

sum1=sum(list1)
sum2=sum(list2)
sum3=sum(list3)
sum4=sum(list4)

if sum1>=sum2 and sum1>=sum3 and sum1>=sum4:
    print(list1)
elif sum2>=sum1 and sum2>=sum3 and sum2>=sum4:
    print(list2)
elif sum3>=sum1 and sum3>=sum2 and sum3>=sum4:
    print(list3)
else:
    print(list4)

