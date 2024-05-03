def divisible_by_5(list1, result = []):
  result=[]
  for i in  list1 :
    num=int(i)
    if  num % 5 == 0:
      result.append(num)
  return result

list2 = input("Given list is: ").split()
res = divisible_by_5(list2)
print("Divisible by 5")
print("\n".join(map(str,res)))
