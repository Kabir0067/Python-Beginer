my_dict = {
    "Physics": 82,
    "Math": 65,
    "History": 75
}
mini = min(my_dict, key=my_dict.get)
print(mini)
