from itertools import combinations
n,k=list(map(int,input().split()))
array=list(map(int,input().split()))
print(sum(1 for i in list(combinations(array,2)) if sum(i)%k==0))
