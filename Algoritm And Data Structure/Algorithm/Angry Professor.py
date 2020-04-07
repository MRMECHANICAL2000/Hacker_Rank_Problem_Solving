for i in range(int(input())):
    a,k=list(map(int,input().split()))
    if k<=sum([1 for i in list(input().split()) if int(i)<=0]):
        print("NO")
    else:
        print("YES")
