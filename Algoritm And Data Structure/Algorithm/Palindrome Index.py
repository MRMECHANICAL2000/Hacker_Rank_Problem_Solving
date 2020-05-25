def ispalindrome(string):
    s=string
    rs=string[::-1]
    for i in range(round(len(s)/2)):
        if s[i]!=rs[i]:
            new_string=s[:i]+s[i+1:]
            rev_new_string=rs[:i]+rs[i+1:]
            if new_string==new_string[::-1]:
                print(i)
                break
            elif rev_new_string==rev_new_string[::-1]:
                print(len(s)-1-i)
                break
    else:
        print(-1)
if __name__=='__main__':
    for i in range(int(input())):
        string=input()
        if string==string[::-1]:
            print(-1)
        else:
            ispalindrome(string)
