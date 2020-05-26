n,k,q=list(map(int,input().split()))
s=list(map(int,input().split()))
for i in range(q):
    m=int(input())
    print (s[m-(k%n)])
