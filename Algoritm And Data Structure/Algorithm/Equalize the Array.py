x=int(input())
y=list(map(int,input().split()))
print(x-max([y.count(i) for i in set(y)]))
