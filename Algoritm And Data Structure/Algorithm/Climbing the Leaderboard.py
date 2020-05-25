from collections import Counter

#binary search solution
def binary_search(l,v,f,b):
    while f<=b:
        mid=(f+b)//2
        if l[mid]==v:
            print(mid+1)
            break
        elif v>l[mid]:
            b=mid-1
        else:
            f=mid+1
    else:
        print(f+1)


#ordinart search solution
def ordinary_search(score,alice):
    start=0
    ans=[]
    for i in alice[::-1]:
        value=i
        for i in range(start,len(score)):
            if score[i]<value:
                ans.append(i+1)
                start=i
                break
            elif score[i]==value:
                ans.append(i+1)
                start=i
                break
        else:
            ans.append(i+2)
            start=i-1
    [print(i) for i in ans[::-1]]


if __name__=='__main__':
    input()
    scores=[int(i) for i in input().split()]
    score=list(Counter(scores).keys())

    input()
    start=0
    alice=[int(i) for i in input().split()]

    #ordinary search solution
    ordinary_search(score,alice)
    '''
    #uncomment for binary search solution
    for i in alice:
        binary_search(score,i,0,len(score)-1)
    ''' 
