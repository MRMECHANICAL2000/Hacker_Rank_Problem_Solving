x=int(input())
a=[int(i) for i in input().split()]
maxx=a[0]
minn=a[0]
hig=0
low=0
for i in range(x):
    if a[i]>maxx:
        maxx=a[i]
        hig+=1
    elif a[i]<minn:
        minn=a[i]
        low+=1
print(hig,low)
