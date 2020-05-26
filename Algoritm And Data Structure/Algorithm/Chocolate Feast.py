for _ in range(int(input())):
    n,c,m=list(map(int,input().split()))
    choc=0
    wrap=int(n/c)
    choc+=wrap
    while wrap>=m:
        choc+=int(wrap/m)
        wrap=int(wrap%m)+int(wrap/m)
    print(choc)
