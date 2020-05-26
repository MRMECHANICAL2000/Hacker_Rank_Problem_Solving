from collections import deque
length=int(input())
x=list(map(int,input().split()))
y=sorted(x)
a=[]
for i in range(length):
    if x[i]!=y[i]:
        a.append(i)
if len(a)==2:
    x[a[0]],x[a[1]]=x[a[1]],x[a[0]]
    if x==y:
        print("yes")
        print("swap {} {}".format(a[0]+1,a[-1]+1))
else:
    x=x[:a[0]]+x[a[0]:a[-1]+1][::-1]+x[a[-1]+1:]
    if x==y:
        print("yes")
        print("reverse {} {}".format(a[0]+1,a[-1]+1))
if x!=y:
    print("no")
        
