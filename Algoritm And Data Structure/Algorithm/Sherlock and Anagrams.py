from itertools import combinations
from collections import Counter

for _ in range(int(input())):
    string=list(input())
    anagram=0
    if max([string.count(i) for i in set(string)])>1:
        for i in range(1,len(string)):
            combo=[]
            [combo.append("".join(sorted(string[x:x+i]))) for x in range(0,len(string)-i+1)]        
            b=Counter(combo)
            for j in b.values():
                anagram+=int(j*(j-1)/2)
    print(anagram)
            
            
