my_str = input().split()
for i in my_str:
    udalit = ""
    for j in i:
        if j != udalit[-1:]:
            udalit += j
    print(udalit)
