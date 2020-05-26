x1,v1,x2,v2=list(map(int,input().split()))

if (x1>x2 and v1<v2) and (x1-x2)%(v2-v1)==0:
    print("YES")
elif (x1<x2 and v1>v2)and (x2-x1)%(v1-v2)==0:
    print("YES")
elif (x1==x2 and v1==v2):
    print("YES")
else:
    print("NO")
