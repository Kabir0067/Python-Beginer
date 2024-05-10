def vowels_to_char(txt, chr):
    vowels = "AEIOUYaeiouy"
    new_txt = ""   
    for i in txt:
        if i not in vowels:
            new_txt += i 
        else:
           new_txt+=char
    return new_txt

txt = input()
char = input()
print(vowels_to_char(txt, char))




