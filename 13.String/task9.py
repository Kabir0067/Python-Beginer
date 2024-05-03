string = input()
num = int(input())

if num < 0 or num >= len(string):
    print(False)
else:
    new_string = string[:num] + string[num + 1:]

    print("New string:--->", new_string)
