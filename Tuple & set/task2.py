my_list = [
    {'Green': '#008000'},
    {'Black': '#000000'},
    {'Blue': '#0000FF'},
    {'Green': '#008000'}  
]
new=[]
for i in my_list:
  if i not in new :
    new.append(i)
print(new)