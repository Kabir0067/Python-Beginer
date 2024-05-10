def string_4_6(string):
    if string.isdigit() and (len(string) == 4 or len(string) == 6):
        return True
    else:
        return False

string = input()
print(string_4_6(string))
