#Python-3
#1 using slising

```
n,k,q=list(map(int,input().split()))
a=list(map(int,input().split()))
a=a[-k%n:]+a[:-k%n]
[print(a[int(input())]) for i in range(q)] 

```

#2 using math

```

n,k,q=list(map(int,input().split()))
s=list(map(int,input().split()))
for i in range(q):
    m=int(input())
    print (s[m-(k%n)])
```        
