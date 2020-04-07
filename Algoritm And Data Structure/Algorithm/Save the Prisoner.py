# using condition
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    if b+c<=a:
        print(b+c-1)
    else: 
        b=(b-(a-c+1))%a
        if b==0:
            print(a)
        else:
            print(b)

# Using Math
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    q=(c+b-1)%a 
    if q:
      print(q)
    else:
      print(a) 
