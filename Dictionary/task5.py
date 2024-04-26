my_dict={
    'name': "Kelly",
    'age': 25,
    'salary': 8000,
    'city': "New York"
}
rem = ['name', 'salary']

for i in rem:
    if i in my_dict:
        del my_dict[i]
        
        
print(my_dict)
  
