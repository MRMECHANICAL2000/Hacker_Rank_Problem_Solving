length=int(input())
cloud=[int(i) for i in input().split()]
a=0
c=0
while a+2<length:
    if cloud[a+1]==1 or cloud[a+2]==0:
        a+=2
    else:
        a+=1
    c+=1
if a+1<length:
    c+=1
print(c)
