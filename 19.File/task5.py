my_list=["Salom mardum", "hello world", "Tajikistan ba pesh","Soft club"]
with open("fille.txt","w") as file:
    for i in my_list:
        file.write(i +"\n")
    print("operation successfully")
        