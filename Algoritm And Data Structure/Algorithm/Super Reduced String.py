def superReducedString(s):
    s=list(s)
    s.append(",")
    for i in range(len(list(s))-2,-1,-1):
        if s[i]==s[i+1]:
            s.pop(i+1)
            s.pop(i)
    s.pop()
    if len(s)>0:
        return("".join(s))
    return ("Empty String")
