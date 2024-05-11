def cnt_sum_vowels(string1):
    my_dict = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
    cnt = 0
    for i in string1.upper():
        if i in my_dict:
            cnt += my_dict[i]
    return cnt

my_str=input()
print(cnt_sum_vowels(my_str))