#without forming result matrix
from math import ceil, sqrt
s = input().strip()
c = ceil(sqrt(len(s)))
print(' '.join(map(lambda x: s[x::c], range(c))))

#forming matrix and printing result
"""
import math
s=input()
matrix=[]
r,c=math.floor(math.sqrt(len(s))),math.ceil(math.sqrt(len(s)))
if r*c<len(s):
    r=c
c1=0
c2=c
for i in range(r):
    matrix.append(s[c1:c2])
    c1,c2=c2,c2+c
for i in range(c):
    string=""
    n=len(matrix[-1])
    for j in range(r):
        if i<n:
            string+=str(matrix[j][i])
            
        elif j<r-1:
            string+=str(matrix[j][i])        
    print(string,end=" ")
"""
