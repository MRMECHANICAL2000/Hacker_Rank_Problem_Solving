aa,k,q=list(map(int,input().split()))
a=list(map(int,input().split()))
a=a[-k%aa:]+a[:-k%aa]
[print(a[int(input())]) for i in range(q)] 
