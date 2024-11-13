def longest_string(s):
    l=0
    res=0
    set1=set() #creating a set to store visited characters
    for r in range(len(s)):
        if s[r] not in set1:  # if character not in set1 we simple add a character into the set1 
            set1.add(s[r])
            res=max(res,r-l+1) # updating res to identify the length 
        else:
            while s[r] in set1:
                set1.discard(s[l])
                l+=1
            set1.add(s[r])
            res=max(res,r-l+1)
    return res
s="abccdacbbbc"
print(longest_string(s))
