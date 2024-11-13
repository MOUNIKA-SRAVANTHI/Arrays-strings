def zero_count(l,k):
    if(l==k):
        return 0
    elif(k==0):
        return l
    else:
        empt=k+1
        first_zero=(l-k)//empt
        nxt_zero=(l-k)%empt
        if(nxt_zero>1):
            return first_zero+1
        else:
            return first_zero
l=int(input("enter str len"))
k=int(input("enter  no of ones"))
print(zero_count(l,k))
