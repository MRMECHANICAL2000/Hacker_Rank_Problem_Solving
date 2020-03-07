input()
x=sorted(list(map(int,input().split())))

countt=0
val=0
for i in x: 
    if (x.count(i)>countt):
        countt=x.count(i)
        val=i
    while i in x:
        x.remove(i)
        

print(val)