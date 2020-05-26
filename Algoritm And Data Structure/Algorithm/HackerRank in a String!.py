for _ in range(int(input())):
    string=list(input())
    a=0
    check=0
    for i in list("hackerrank"):
        if i in string[a:]:
            a=string.index(i,a)+1
        else:
            check=1
            print("NO")
            break
    if check==0:
        print("YES")
