from itertools import combinations
x,y=[int(i) for i in input().split()]
array=[int(i) for i in input().split()]
a=sum([1 for i in array if i+y in array and i+2*y in array])
print(a)
