from datetime import datetime
my_list=[]
cnt=0

#####################################################################

def add_task ():
    global cnt
    cnt+=1
    my_dict={
        "id":cnt,
        "user_name":input("Input your name --->  "),
        "task_name":input("Input task name --->  "),
        "due_date":input("input due date --->  "),
        "is_completed": False,
        "craeted_at":datetime.now()
    }
    my_list.append(my_dict)
    
#####################################################################

def get_task():
    for i in my_list:
        for key,value in i.items():
            print(key,value)
        print("-"*60)
        
#####################################################################

def get_by_id(id):
    for i in my_list:
        if i["id"] == id:
            for key,value in i.items():
                print(key,value)
    print("-"*60)  
         
#####################################################################

def delete_by_id(id):
    for i in my_list:
        if i["id"] == id:
            my_list.pop(my_list.index(i))
         
#####################################################################

def edit_by_id(id):
    for i in my_list:
        if i["id"] == id:
            i["user_name"] = input("Input new user name --->  ")
            i["task_name"] = input("Input new task name --->  ")
            i["due_date"] = input("Input new due date --->  ")
            break

#####################################################################

def todays_tasks():
    td_task="today"
    for i in my_list:
        if i["due_date"]==td_task:
            for key,value in i.items():
                print(key,value)
            print("-"*60)
#####################################################################

def filter_by_user(us_name):
    for i in my_list:
        if i["user_name"] == us_name:
            for key, value in i.items():
                print(key, value)
            print("-"*60)

#####################################################################

while True:
    print("#"*60)
    print("1. Add task")
    print("2. Get task")
    print("3. Get by id")
    print("4. Delit by id")
    print("5. Edit by id")
    print("6. Todays tasks")
    print("7. Filter by user")
    print("8. Exit")
    print("#"*60)
    
    choice = input("Enter your choice -->  ")
    print("--"*30)
    match choice:
        case "1":
            add_task()
        case "2":
            get_task()
        case "3":
            num = int(input("Enter id -->  "))
            get_by_id(num)
        case "4":
            num = int(input("Enter  id-->  "))
            delete_by_id(num)
        case "5":
            num = int(input("Enter id: -->  "))
            edit_by_id(num)
        case "6":
            todays_tasks()
        case "7":
            user_name = input("Enter user name -->  ")
            filter_by_user(user_name)
        case "8":
            break
        case _:
            print("Eror comand.")