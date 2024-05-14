def function(sentens):
    pst_set=set()
    for i in sentens.lower():
        if i.isalpha():
            pst_set.add(i)
       
    return len(pst_set)==26
    
    
sentens1="The quick brown fox jumps over the lazy dog"
print(function(sentens1))

    